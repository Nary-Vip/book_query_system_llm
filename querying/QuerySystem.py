import os
import pinecone
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import OnlinePDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

class BookQuery:
    def __init__(self, OPEN_AI_KEY, PINECONE_API_KEY, ENVIRONMENT_KEY) -> None:
        os.environ["OPENAI_API_KEY"]=OPEN_AI_KEY
        self.embeddings = OpenAIEmbeddings()
        self.pinecone.init(
            api_key=PINECONE_API_KEY,
            environment=ENVIRONMENT_KEY,
        )
        self.index_name = "lanchain"
        self.llm = OpenAI(temperature=0.8)
    
    def loadThePDFS(self, pdfLink):
        loader = OnlinePDFLoader(pdfLink)
        self.data = loader.load()


    def docSplitter(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        self.texts = text_splitter.split_documents(self.data)
    
    def vectorizeAndUpload(self, index_name):
        try:
            self.docsearch = Pinecone.from_texts([t.page_content for t in self.texts], self.embeddings, index_name=index_name)
            return True
        
        except Exception as e:
            print(e)

    def userQuery(self, query):
        try:
            docs = self.docsearch.similarity_search(query, k=5)
            chain = load_qa_chain(self.llm, chain_type="stuff")
            ans = chain.run(question=query, input_documents= docs)
            return ans
        except Exception as e:
            print(e)
