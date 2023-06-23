import os
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

# Setting up the open ai key
from constants import *
os.environ["OPENAI_API_KEY"]=OPEN_AI_KEY

# Load the PDF from the user request
loader = UnstructuredPDFLoader("./pdfs/data_science.pdf")
data = loader.load()


# Logging Part - PENDING
print(len(data))
print(len(data[0].page_content))


# Chunk the text data into smaller documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

# Logging the chunk counts - PENDING 
len(texts)


# Initializing the OpenAI Embedder - 1536 vector length
embeddings = OpenAIEmbeddings()


