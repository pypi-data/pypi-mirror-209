# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from pathlib import Path
import pickle
import tarfile
from typing import Dict, List, Tuple, Union

import faiss
from faiss import IndexFlat
from langchain.chat_models.openai import ChatOpenAI
from langchain.docstore.document import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import BaseMessage, HumanMessage, SystemMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import requests

CONTEXT_INDEX_FILENAME = "index.faiss"
CONTEXT_STORE_FILENAME = "store.pickle"


class BaseLLMBot(ABC):
    def __init__(
        self,
        text_chunk_size: int = 1000,
        text_chunk_overlap: int = 250,
        text_separators: List[str] = [" ", ".", ",", ";", ":", "!", "?", "\n"],
        temperature: float = 0,
    ):
        self._stores: Dict[str, FAISS] = None
        self._chat = ChatOpenAI(temperature=temperature)
        self._text_chunk_size = text_chunk_size
        self._text_chunk_overlap = text_chunk_overlap
        self._text_separators = text_separators

    @abstractmethod
    def train(self, name, *args, **kwargs) -> None:
        """
        Builds the index and the vector store from the given data.
        """

    @abstractmethod
    def add_to_index(self, name, *args, **kwargs) -> None:
        """
        Adds the given data to the index and the vector store.
        """

    def fetch_from_index(
        self,
        query: str,
        n_results: int,
        index: str,
        min_score: float = 0.0,
    ) -> Tuple[List[Document], List[float]]:
        """
        Fetches the most relevant documents from the index.

        Args:
            query (str): The query to search for.
            n_results (int): The number of results to return.
            index (str): The index to search in.
            min_score (float): The minimum score a document must have to be returned.
            index_name (str): The name of the index to search in. If None, any index will be
                searched.

        Returns:
            List[Document]: The most relevant documents.
        """
        # Check if we have that index
        if index not in self._stores:
            raise ValueError(f"Index '{index}' does not exist.")
        store = self._stores[index]
        docs_and_scores: List[
            Tuple[Document, float]
        ] = store.similarity_search_with_relevance_scores(query, k=n_results)
        docs: List[Document] = [doc for doc, _ in docs_and_scores]
        scores: List[float] = [score for _, score in docs_and_scores]
        ret_docs: List[Document] = []
        ret_scores: List[float] = []
        for doc, score in zip(docs, scores):
            if score >= min_score:
                ret_docs.append(doc)
                ret_scores.append(score)
        return ret_docs, ret_scores

    def save(self, path: Union[str, Path]) -> None:
        """
        Saves the indexes and the vector stores to the given path.

        Args:
            path (Union[str, Path]): The path to save the index and vector store to.
        """
        # Assert that the path exists
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        # Save the indexes and the vector stores
        indexes_list: List[str] = list(self._stores.keys())
        for index_name in indexes_list:
            # Get store and index from the index name
            store = self._stores[index_name]
            index = store.index
            # Save index
            index_fname = str(path / f"index_{index_name}.faiss")
            faiss.write_index(index, index_fname)
            # Save vector store
            store.index = None
            store_fname = str(path / f"store_{index_name}.pickle")
            with open(store_fname, "wb") as f:
                pickle.dump(store, f)
            store.index = index

    def download(self, url: str, path: Union[str, Path], name: str) -> None:
        """
        Downloads the context (index + vector store) from a given URL and extracts it to the given
        path.

        Args:
            url (str): The URL to download the context from.
            path (Union[str, Path]): The path to extract the context to.
            name (str): The name of the context.
        """
        # Assert that the path exists
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        # Download the model
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Determine compression format based on file extension
        filename = Path(url).name
        if filename.endswith(".tar.gz"):
            mode = "r|gz"
        elif filename.endswith(".tar.bz2"):
            mode = "r|bz2"
        elif filename.endswith(".tar.xz"):
            mode = "r|xz"
        elif filename.endswith(".tar"):
            mode = "r|"
        else:
            raise ValueError(f"Unknown compression format for file: {filename}")

        # Extract the model
        with tarfile.open(fileobj=response.raw, mode=mode) as tar:
            tar.extractall(path=path)

        # Assert that we have the correct files. If we don't, then we need to delete the files
        index_fname = path / CONTEXT_INDEX_FILENAME
        store_fname = path / CONTEXT_STORE_FILENAME
        try:
            assert index_fname.exists() and store_fname.exists()
        except AssertionError as exc:
            index_fname.unlink(missing_ok=True)
            store_fname.unlink(missing_ok=True)
            raise AssertionError(
                f"Either {index_fname} or {store_fname} does not exist."
            ) from exc

        # If filenames are correct, rename them according to the context name
        index_fname.rename(path / f"index_{name}.faiss")
        store_fname.rename(path / f"store_{name}.pickle")

    def load(self, path: Union[str, Path]) -> None:
        """
        Loads the index and the vector store from the given path.

        Args:
            path (Union[str, Path]): The path to load the index and vector store from.
        """
        # Assert that the path exists
        path = Path(path)
        assert path.exists(), f"Path {path} does not exist."

        # Get list of files in the path with `index_` and `store_` prefixes
        index_files = [f for f in path.glob("index_*")]
        store_files = [f for f in path.glob("store_*")]

        # Assert that all files have a corresponding index and store file
        for index_file in index_files:
            store_file = path / f"store_{index_file.stem[6:]}.pickle"
            assert store_file.exists(), f"Store file {store_file} does not exist."
        for store_file in store_files:
            index_file = path / f"index_{store_file.stem[6:]}.faiss"
            assert index_file.exists(), f"Index file {index_file} does not exist."

        # Load the indexes and the vector stores
        self._stores = {}
        for index_file in index_files:
            # Get index name from the index file name
            index_name = index_file.stem[6:]
            # Load index
            index: IndexFlat = faiss.read_index(f"{str(index_file)}.faiss")
            # Load vector store
            store_fname = path / f"store_{index_name}.pickle"
            with open(store_fname, "rb") as f:
                store: FAISS = pickle.load(f)
            store.index = index
            self._stores[index_name] = store

    def build_messages(
        self,
        personality_prompt: str,
        user_message: str,
        use_chat_history: str = None,
        chat_history_prompt: str = "Aqui está o histórico da conversa até agora:",
        number_of_chat_history_docs: int = 2,
        use_context: List[str] = None,
        context_prompt: str = "Aqui estão pedaços de informação que você pode usar:",
        number_of_context_docs: int = 2,
        minimum_similarity: float = 0.0,
    ) -> Tuple[List[BaseMessage], List[Tuple[str, float]]]:
        """
        Builds a list of messages to send to the chatbot.

        Args:
            personality_prompt (str): The prompt to use for the personality.
            user_message (str): The message from the user.
            use_chat_history (str, optional): Which chat history to use. Defaults to None.
            chat_history_prompt (str, optional): The prompt to use for the chat history. Defaults
                to "Aqui está o histórico da conversa até agora:".
            number_of_chat_history_docs (int, optional): The number of chat history documents to
                use. Defaults to 2.
            use_context (List[str], optional): Which contexts to use. Defaults to None.
            context_prompt (str, optional): The prompt to use for the context documents. Defaults
                to "Aqui estão pedaços de informação que você pode usar:".
            number_of_context_docs (int, optional): The number of context documents to use. Defaults
                to 2.
            minimum_similarity (float, optional): The minimum similarity between the user message
                and the context documents. Defaults to 0.0.

        Returns:
            Tuple[List[BaseMessage], List[str]]: A tuple containing the list of messages to send to
                the chatbot and the list of sources of the context documents.
        """
        # Start list of messages with the personality prompt
        messages: List[BaseMessage] = [SystemMessage(content=personality_prompt)]

        # If we are using context, search for context documents and add them to the prompt
        sources: List[Tuple[str, float]] = []
        if use_context:
            messages.append(SystemMessage(content=context_prompt))
            for context_name in use_context:
                if len(sources) >= number_of_context_docs:
                    break
                docs, scores = self.fetch_from_index(
                    query=user_message,
                    n_results=number_of_context_docs,
                    index=context_name,
                    min_score=minimum_similarity,
                )
                # Store sources and their scores
                tmp_sources = list(
                    set(
                        [
                            (str(doc.metadata["source"]), score)
                            for doc, score in zip(docs, scores)
                        ]
                    )
                )
                for doc in docs:
                    messages.append(SystemMessage(content=f"- {doc.page_content}"))
                for tmp_source in tmp_sources:
                    sources.append(tmp_source)
                    if len(sources) >= number_of_context_docs:
                        break

        # If chat history is provided, add messages for it
        if use_chat_history:
            messages.append(SystemMessage(content=chat_history_prompt))
            docs, _ = self.fetch_from_index(
                query=user_message,
                n_results=number_of_chat_history_docs,
                index=use_chat_history,
            )
            for doc in docs:
                messages.append(SystemMessage(content=f"- {doc.page_content}"))
            if use_chat_history in self._stores:
                self._stores[use_chat_history].add_texts(
                    texts=[f"User: {user_message}"],
                    metadatas=[{"source": "user"}],
                )
            else:
                embedding = OpenAIEmbeddings()
                self._stores[use_chat_history] = FAISS.from_texts(
                    texts=[f"User: {user_message}"],
                    embedding=embedding,
                    metadatas=[{"source": "user"}],
                )

        # Add the user message
        messages.append(HumanMessage(content=user_message))

        return messages, sources

    def chat(self, messages: List[BaseMessage], chat_id: str) -> str:
        """
        Sends the given messages to the chatbot and returns the response.

        Args:
            messages (List[BaseMessage]): The messages to send to the chatbot.
        """
        # Send the messages to the chatbot
        ai_message = self._chat(messages)

        # Get the response, add to index and return
        response = ai_message.content
        if chat_id in self._stores:
            self._stores[chat_id].add_texts(
                texts=[f"Bot: {response}"],
                metadatas=[{"source": "bot"}],
            )
        else:
            embedding = OpenAIEmbeddings()
            self._stores[chat_id] = FAISS.from_texts(
                texts=[f"Bot: {response}"],
                embedding=embedding,
                metadatas=[{"source": "bot"}],
            )
        return response


class HTMLBot(BaseLLMBot):
    def train(self, name: str, documents_path: Union[str, Path]) -> None:
        """
        Trains the bot using the given documents.

        Args:
            name (str): The name of the knowledge base.
            documents_path (Union[str, Path]): The path to the documents to use for training.
            text_chunk_size (int, optional): The size of the text chunks to use for training.
                Defaults to 1000.
            text_chunk_overlap (int, optional): The overlap between text chunks. Defaults to 250.
            text_separators (List[str], optional): The list of text separators to use for splitting
                the text into chunks. Defaults to [" ", ".", ",", ";", ":", "!", "?", "\n"].
        """
        # Import stuff (importing here avoids unnecessary dependencies)
        from langchain.document_loaders import BSHTMLLoader

        # Assert that the path exists
        documents_path = Path(documents_path)
        assert documents_path.exists(), f"Path {documents_path} does not exist."

        # Load the knowledge base
        loaders: List[BSHTMLLoader] = []
        for html_file in documents_path.glob("**/*.html"):
            loaders.append(BSHTMLLoader(html_file))
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self._text_chunk_size,
            chunk_overlap=self._text_chunk_overlap,
            separators=self._text_separators,
        )
        docs: List[Document] = []
        for loader in loaders:
            docs.extend(loader.load_and_split(text_splitter=text_splitter))

        # Create the vector store
        embedding = OpenAIEmbeddings()
        self._stores[name] = FAISS.from_documents(documents=docs, embedding=embedding)

    def add_to_index(self, name: str, html_files: List[Union[str, Path]]) -> None:
        """
        Adds the given HTML files to the index.

        Args:
            name (str): The name of the knowledge base.
            html_files (List[Union[str, Path]]): The HTML files to add to the index.
        """
        # Import stuff (importing here avoids unnecessary dependencies)
        from langchain.document_loaders import BSHTMLLoader

        # Assert that all files exist
        html_files: List[Path] = [Path(html_file) for html_file in html_files]
        for html_file in html_files:
            assert html_file.exists(), f"File {html_file} does not exist."

        # Load the files
        loaders: List[BSHTMLLoader] = []
        for html_file in html_files:
            loaders.append(BSHTMLLoader(html_file))
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self._text_chunk_size,
            chunk_overlap=self._text_chunk_overlap,
            separators=self._text_separators,
        )
        docs: List[Document] = []
        for loader in loaders:
            docs.extend(loader.load_and_split(text_splitter=text_splitter))

        # Add the documents to the index
        if name in self._stores:
            self._stores[name].add_documents(documents=docs)
        else:
            embedding = OpenAIEmbeddings()
            self._stores[name] = FAISS.from_documents(
                documents=docs, embedding=embedding
            )


class TextBot(BaseLLMBot):
    def train(self, name: str, texts: List[str], metadatas: List[Dict[str, str]]):
        """
        Trains the bot using the given texts.

        Args:
            name (str): The name of the knowledge base.
            texts (List[str]): The texts to use for training.
            metadatas (List[Dict[str, str]]): The metadata for each text.
        """
        # Assert that lengths match
        assert len(texts) == len(
            metadatas
        ), "Lengths of texts and metadatas do not match."

        # Build documents
        docs: List[Document] = []
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self._text_chunk_size,
            chunk_overlap=self._text_chunk_overlap,
            separators=self._text_separators,
        )
        for text, metadata in zip(texts, metadatas):
            docs_texts = text_splitter.split_text(text=text)
            for doc_text in docs_texts:
                docs.append(Document(page_content=doc_text, metadata=metadata))

        # Create the vector store
        embedding = OpenAIEmbeddings()
        self._stores[name] = FAISS.from_documents(documents=docs, embedding=embedding)

    def add_to_index(
        self, name: str, texts: List[str], metadatas: List[Dict[str, str]]
    ):
        """
        Adds the given texts to the index.

        Args:
            name (str): The name of the knowledge base.
            texts (List[str]): The texts to add to the index.
            metadatas (List[Dict[str, str]]): The metadata for each text.
        """
        # Assert that lengths match
        assert len(texts) == len(
            metadatas
        ), "Lengths of texts and metadatas do not match."

        # Build documents
        docs: List[Document] = []
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self._text_chunk_size,
            chunk_overlap=self._text_chunk_overlap,
            separators=self._text_separators,
        )
        for text, metadata in zip(texts, metadatas):
            docs_texts = text_splitter.split_text(text=text)
            for doc_text in docs_texts:
                docs.append(Document(page_content=doc_text, metadata=metadata))

        # Add the documents to the index
        if name in self._stores:
            self._stores[name].add_documents(documents=docs)
        else:
            embedding = OpenAIEmbeddings()
            self._stores[name] = FAISS.from_documents(
                documents=docs, embedding=embedding
            )
