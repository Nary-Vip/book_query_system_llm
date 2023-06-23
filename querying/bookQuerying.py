import os
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone


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


# Initialize the pinecone vector store
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=ENVIRONMENT_KEY,
)

index_name = "lanchain"


# Vectorize the pdf data and store it in pinecone atlas with OpenAI Embedder.
docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)


# Get the user query from the API
query = "Mention 2 algorithm is used for density estimation" # Hard code for now

# Similarity search from pinecone embedder doc will return the top K chunks of data that has similar vector semantics with the user query
docs = docsearch.similarity_search(query, k=5)
# Top 5 chunks are selected.

    