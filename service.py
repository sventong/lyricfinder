# File: service.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# That is the file where NeuralSearcher is stored
from neural_searcher import NeuralSearcher

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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