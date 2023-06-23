from fastapi import FastAPI
import uvicorn
from fastapi.responses import Response
from pydantic import BaseModel
import requests
from constants import EXAMPLE_PDF

app = FastAPI()

@app.get("/")
def check():
    return Response("API working")



class QueryModel(BaseModel):
    email: str
    query: str
    docUrl: str


@app.post("/userquery")
async def respond():
    book = requests.get(EXAMPLE_PDF)
    with open("local_file.pdf", 'wb')as file:
        file.write(book.content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5600)