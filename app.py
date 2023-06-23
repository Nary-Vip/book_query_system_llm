from fastapi import FastAPI
import uvicorn
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def check():
    return Response("API working")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5600)