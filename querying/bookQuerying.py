import os
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Setting up the open ai key
from constants import *
os.environ["OPENAI_API_KEY"]=OPEN_AI_KEY


