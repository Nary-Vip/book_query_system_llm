import os
import io
import PyPDF2
from pathlib import Path
import chromadb
import pinecone
import requests
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

class BookQuery:
    def __init__(self, OPEN_AI_KEY, PINECONE_API_KEY, ENVIRONMENT_KEY) -> None:
        os.environ["OPENAI_API_KEY"]=OPEN_AI_KEY
        self.embeddings = OpenAIEmbeddings()
        
        self.chroma_client = chromadb.Client()
        
        pinecone.init(
            api_key=PINECONE_API_KEY,
            environment=ENVIRONMENT_KEY,
        )
        self.index_name = "lanchain"
        self.llm = OpenAI(temperature=0.8)
        print("Intialization Done")
    
    def loadThePDFS(self, pdfLink, filename):
        try:
            print("Load pdf starts")
            res = requests.get(pdfLink)
            response = res.content
            filename = Path(f'books/{filename}.pdf')
            filename.write_bytes(response)
            pdf_reader = PyPDF2.PdfReader(filename)
            raw_text = ""
            for i, page in enumerate(pdf_reader.pages):
                raw_text += page.extract_text()
            
            print(len(raw_text))
            self.data = raw_text
            print("PDF Loaded")
        except Exception as e:
            print(e)


    def docSplitter(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        self.texts = text_splitter.split_text(self.data)
        print(len(self.texts))
        print("Split Done")
    
    def vectorizeAndUpload(self, index_name):
        try:
            # index_list = self.client.list_collections()
            # if index_name not in index_list:
            
            # self.collection = self.chroma_client.create_collection(name=index_name)

            # self.collection.add(
            #     documents=self.texts,
            #     metadatas=[{"source": f"api{i}"} for i in range(1, len(self.texts)+1)],
            #     ids=[f"id{i}" for i in range(1, len(self.texts)+1)]
            # )

            self.docsearch = Chroma.from_texts(self.texts, self.embeddings, metadatas=[{"source": f"Text chunk {i} of {len(self.texts)}"} for i in range(len(self.texts))], persist_directory="db")
            self.docsearch.persist()
            # index_list = pinecone.list_indexes()
            # if index_name not in index_list:
            #     pinecone.create_index(index_name, dimension=1536)
            #     self.docsearch = Pinecone.from_texts([t.page_content for t in self.texts], self.embeddings, index_name=index_name)
    
            # self.index = pinecone.Index(index_name)

            print("Index Created")
        
        except Exception as e:
            print(e)

    def userQuery(self, query):
        try:
            print("resolving query")
            # results = self.collection.query(
            #     query_texts=[query],
            #     n_results=3
            # )
            # query_vector = self.embeddings.embed_query(query)
            docs = self.docsearch.similarity_search(query, k=5)
            # query_res = self.index.query(queries=query_res, top_k=5)
            print("query_res", docs)
            chain = load_qa_chain(self.llm, chain_type="stuff")
            ans = chain.run(question=query, input_documents= docs)
            print("==========")
            print(ans)
            print("==========")
            return ans

        
        except Exception as e:
            print(e)
