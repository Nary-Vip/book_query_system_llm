from fastapi import FastAPI
import uvicorn
from fastapi.responses import Response
from pydantic import BaseModel
import requests
from constants import *
from bookQuery.QuerySystem import BookQuery

app = FastAPI()

@app.get("/")
def check():
    return Response("API working")


class QueryModel(BaseModel):
    email: str
    query: str
    docUrl: str
    index_name: str


@app.post("/userquery")
async def respond(data: QueryModel):
    book = BookQuery(OPEN_AI_KEY, PINECONE_API_KEY, ENVIRONMENT_KEY)
    book.loadThePDFS(data.docUrl, data.index_name)
    book.docSplitter()
    book.vectorizeAndUpload(data.index_name)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5600)