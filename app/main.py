from fastapi import FastAPI
from bing_search import bing_search

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/{query}")
async def search(query: str):
    results = bing_search(query)
    return {"message": results}