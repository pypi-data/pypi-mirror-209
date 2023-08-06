"""
LLM Module to implement classes to ask questions on a set of documents
stored in Extended ECM. Optionally a chathistory can be preserved and
provided as context for subsequent asks to the LLM.

Class: ExtendedECMFileLoader
Methods:

__init__ : class initializer
load: download a document from Extended ECM, convert it to text
      and return it

Class: ExtendedECMLoader
Methods:

__init__ : class initializer
load_from_folder: load all documents stored in a defined folder. Optionally also recurse sub-folders.
load_from_node_ids: load documents with given node IDs (list)
load: main method to load a set of documents from Extended ECM and
      converts them to text chunks and load these into a vector database

      
Class: ExtendedECMChat      
Methods:

__init__ : class initializer
ask: ask the LLM a question about the Extended ECM content

"""

__author__ = "Dr. Marc Diefenbruch"
__copyright__ = "Copyright 2023, OpenText"
__credits__ = ["Kai-Philip Gatzweiler"]
__maintainer__ = "Dr. Marc Diefenbruch"
__email__ = "mdiefenb@opentext.com"

import logging
import os
import tempfile

from typing import List

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings  # actually come from OpenAI

# from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI

# from langchain.callbacks import get_openai_callback
from langchain.memory import ConversationBufferMemory

from pyxecm.otcs import OTCS

logger = logging.getLogger(os.path.basename(__file__))

CHROMA_DB_DIRECTORY = "chroma_db/extended_ecm"


class ExtendedECMFileLoader(BaseLoader):
    _otcs_object: OTCS = None
    _node_id = 0

    def __init__(self, otcs_object: object, node_id: int, node_name: str):
        """Initialize with path to directory and how to glob over it."""
        self._node_id = node_id
        self._otcs_object = otcs_object
        self._node_name = node_name

    def load(self) -> List[Document]:
        """Loads a document from Extended ECM into
           a temporary file system location, then
           converts it with the "UnstructuredFileLoader" into
           a plain text representation

        Returns:
            List[Document]: the converted document (list with one item)
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = f"{temp_dir}/{self._node_name}"

            self._otcs_object.downloadDocument(self._node_id, file_path=file_path)

            try:
                loader = UnstructuredFileLoader(file_path)
                document = loader.load()
                # We want the original Extended ECM URL as source:
                if document:
                    document[0].metadata["source"] = (
                        self._otcs_object.csUrl() + "/app/nodes/" + str(self._node_id)
                    )
            except Exception as e:
                logger.warning(e)
                document = []

            return document


class ExtendedECMLoader(BaseLoader):
    """Load defined document set from Extended ECM."""

    _otcs_object: OTCS = None
    _folder_path = []
    _node_ids = []

    _supported_mime_types = {
        "doc": "application/msword",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "xls": "application/vnd.ms-excel",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "pdf": "application/pdf",
    }

    def __init__(
        self,
        otcs_object: object,
        folder_path: list = [],
        node_ids: list = [],
        supported_mime_types: dict = {},
    ):
        """Initialize the class variables."""
        self._otcs_object = otcs_object
        self._folder_path = folder_path
        self._node_ids = node_ids

        if supported_mime_types:
            self._supported_mime_types = supported_mime_types

    # end method definition

    def load_from_folder(
        self, folder_id: int, recursive: bool = True
    ) -> List[Document]:
        """
        Loads all supported document files from the specified folder
        in Extended and returns a list of Document objects.

        Args:
            folder_id: Node ID of the folder.

        Returns:
            List[Document]: A list of Document objects representing
                            the loaded documents.

        """

        docs = []

        # Load the non-container items (-3 = non-container):
        items = self._otcs_object.getSubnodes(folder_id, filter_node_types=-3)
        if items:
            items = items["results"]

            for item in items:
                properties = item["data"]["properties"]
                if properties["type"] == 144 and properties["mime_type"] in list(
                    self._supported_mime_types.values()
                ):
                    item_id = properties["id"]
                    item_name = properties["name"]
                    file_loader = ExtendedECMFileLoader(
                        self._otcs_object, node_id=item_id, node_name=item_name
                    )
                    docs.extend(file_loader.load())
                    logger.info("Number of Documents: {}".format(len(docs)))

        # If we do not want to traverse all sub-folders / workspaces
        # we are done and can return here:
        if not recursive:
            return docs

        # Get children nodes of the current node:
        sub_folders = self._otcs_object.getSubnodes(folder_id, filter_node_types=-1)
        if sub_folders:
            sub_folders = sub_folders["results"]

            for sub_folder in sub_folders:
                properties = sub_folder["data"]["properties"]
                sub_folder_id = properties["id"]
                sub_folder_type = properties["type"]
                # We ony traverse folders (type = 0) and workspaces (type = 848):
                if sub_folder_type == 0 or sub_folder_type == 848:
                    docs += self.load_from_folder(sub_folder_id)
                    logger.info("Number of Documents: {}".format(len(docs)))

        return docs

    # end method definition

    def load_from_node_ids(self) -> List[Document]:
        """
        Loads all supported document files from Extended ECM
        based on their node IDs and returns a list
        of Document objects.

        Args:
            None

        Returns:
            List[Document]: A list of Document objects representing
                            the loaded documents.
        """

        docs = []

        for node_id in self._node_ids:
            node = self._otcs_object.getNode(node_id)
            if not node:
                logging.warning("Cannot find node with ID -> {}".format(node_id))
                continue
            node_type = self._otcs_object.getResultValue(node, "type")
            if not node_type == 144:
                continue
            document_mime_type = self._otcs_object.getResultValue(node, "mime_type")
            if not document_mime_type in list(self._supported_mime_types.values()):
                continue

            document_name = self._otcs_object.getResultValue(node, "name")
            loader = ExtendedECMFileLoader(
                self._otcs_object, node_id=node_id, node_name=document_name
            )
            docs.extend(loader.load())
            logger.info("Number of Documents: {}".format(len(docs)))

        return docs

    # end method definition

    def load(self) -> List[Document]:
        """
        Loads all supported document files from the specified Extended ECM folder
        or node IDs and returns a list of Document objects.

        Returns:
            List[Document]: A list of Document objects
                            representing the loaded documents.
        """

        docs: List[Document] = []

        if self._folder_path:
            folder = self._otcs_object.getNodeByVolumeAndPath(141, self._folder_path)
            if not folder:
                return docs
            folder_id = self._otcs_object.getResultValue(folder, "id")
            docs.extend(self.load_from_folder(folder_id=folder_id))
        if self._node_ids:
            docs.extend(self.load_from_node_ids())

        return docs

    # end method definition


class ExtendedECMChat(object):
    """Ask Extended ECM questions about a configurable set of documents

    Args:
        object: base class
    """

    _otcs_object: OTCS = None
    _folder_path = []
    _node_ids = []

    _supported_mime_types = {
        "doc": "application/msword",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "xls": "application/vnd.ms-excel",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "pdf": "application/pdf",
    }

    _vector_store = None
    _vector_store_file = None
    _document_loader = None
    _text_splitter = None
    _memory = None
    _conversation_memory: bool = False
    _show_sources: bool = False
    _llm = None
    _embeddings = None
    _chat_history = []

    def __init__(
        self,
        otcs_object: object,
        folder_path: list = [],
        node_ids: list = [],
        supported_mime_types: dict = {},
        load_vector_store: bool = True,
        vector_store_path: str = CHROMA_DB_DIRECTORY,
        conversation_memory: bool = False,
        show_sources: bool = False,
        openai_api_key: str = "",
        temperature: float = 0.0
    ):
        """Initialize the class variables."""
        self._otcs_object = otcs_object
        self._folder_path = folder_path
        self._node_ids = node_ids
        if not openai_api_key:
            openai_api_key = os.getenv("OPENAI_API_KEY")
        self._llm = OpenAI(openai_api_key=openai_api_key, temperature=temperature)
        self._vector_store_path = vector_store_path
        self._conversation_memory = conversation_memory
        self._show_sources = show_sources
        if supported_mime_types:
            self._supported_mime_types = supported_mime_types

        logger.info(
            "Initialize Extended ECM Document Loader with folder path -> {} and node IDs -> {}".format(
                self._folder_path, self._node_ids
            )
        )
        self._document_loader = ExtendedECMLoader(
            otcs_object,
            folder_path=self._folder_path,
            node_ids=self._node_ids,
            supported_mime_types=self._supported_mime_types,
        )

        # Create Embeddings
        logger.info("Create embeddings...")
        embeddings = OpenAIEmbeddings()

        if load_vector_store and os.path.exists(self._vector_store_path):
            logger.info(
                "Loading vector store from file -> {}".format(self._vector_store_path)
            )
            # Here we don't pass in the Extended ECM documents
            # but take the chunks from the existing database.
            self._vector_store = Chroma(
                embedding_function=embeddings,
                collection_name="extended_ecm",
                persist_directory=self._vector_store_path,
            )
        else:
            logger.info(
                "Building new vector store from Extended ECM path -> {} and node IDs -> {}. This will take a while depending on the amount of documents...".format(
                    self._folder_path, self._node_ids
                )
            )
            documents = self._document_loader.load()

            if not documents:
                logger.error("No documents found. Exiting.")
                return

            self._text_splitter = CharacterTextSplitter(
                separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
            )
            logger.info("Split documents into chunks...")
            chunks = self._text_splitter.split_documents(documents)

            logger.info("Build vector store and make it persistent...")
            self._vector_store = Chroma.from_documents(
                chunks,
                embeddings,
                collection_name="extended_ecm",
                persist_directory=self._vector_store_path,
            )

            logger.info(
                "Save vector store to file -> {}...".format(self._vector_store_path)
            )
            self._vector_store.persist()

        # if self._conversation_memory:
        #     logger.info("Initialize Conversational Memory...")
        #     self._memory = ConversationBufferMemory(
        #         memory_key="chat_history", return_messages=True
        #     )

    # end method definition

    def get_llm(self):
        return self._llm

    def get_vector_store(self):
        return self._vector_store

    def get_text_splitter(self):
        return self._text_splitter

    def get_memory(self):
        return self._memory

    def ask(self, question: str, with_score: bool = False):
        """Aks Extended ECM a question about content.

        Args:
            question (str): question to ask
        Responses:
            dict: Response ["output_text"]

        """

        if not question:
            return None

        if with_score:
            relevant_documents = self._vector_store.similarity_search_with_score(
                question
            )
        else:
            relevant_documents = self._vector_store.similarity_search(question)

        logger.debug("Relevant document chunks -> {}".format(relevant_documents))

        # if self._conversation_memory:        
        #     chain = ConversationalRetrievalChain.from_llm(
        #         OpenAI(temperature=0),
        #         self._vector_store.as_retriever(),
        #         memory=self._memory,
        #     )
        # else:

        if self._show_sources:
            chain = load_qa_with_sources_chain(self._llm, chain_type="stuff")
        else:
            chain = load_qa_chain(self._llm, chain_type="stuff")

        chain_parameters = {
            "input_documents": relevant_documents,
            "question": question
        }
        if self._conversation_memory:
            chain_parameters["chat_history"] = self._chat_history

        response = chain(
            chain_parameters,
            return_only_outputs=True,
        )
        # response = chain(
        #     {"input_documents": relevant_documents, "question": question},
        #     return_only_outputs=True,
        # )

        if self._conversation_memory:
            self._chat_history.append((question, response["output_text"]))

        return response

    # end method definition
