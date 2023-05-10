# File: main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

# That is the file where NeuralSearcher is stored
from app.neural_searcher import NeuralSearcher

BASE_DIR = Path(__file__).resolve().parent.parent
print(r'base----------',BASE_DIR)

app = FastAPI()

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# Create an instance of the neural searcher
neural_searcher = NeuralSearcher(collection_name='majan_songs')

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.get("/search")
def search(request: Request, q: str):
    return templates.TemplateResponse("search.html", {
        "request": request,
        "somevar": 2,
        "search_str": q,
        "result": neural_searcher.search(text=q)
    })

# @app.get("/api/search")
# def search_startup(q: str):
#     return {
#         "result": neural_searcher.search(text=q)
#     }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)