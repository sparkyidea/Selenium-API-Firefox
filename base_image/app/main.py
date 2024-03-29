from fastapi import FastAPI
from google_search import google_search

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search/{query}")
async def search(query: str):
    results = google_search(query)
    return {"message": results}