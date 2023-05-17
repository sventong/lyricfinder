from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from neural_searcher import NeuralSearcher

# Base, parent folder where all the files are in
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize FastAPI app and jinja2 Templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

# Init NeuralSearcher from qdrant cloud
neural_searcher = NeuralSearcher(collection_name='twenty')


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "genre": ["pop", "rap", "rb", "rock"]
    })

@app.get("/search")
# search request returns the best matches by the neural_searcher
def search(request: Request, q: str, genre: str):
    # print(neural_searcher.search(text=q, genre=genre))
    if genre == "" and q == "":
        return templates.TemplateResponse("home.html", {
            "request": request,
            "genre": ["pop", "rap", "rb", "rock"]
        })   
    
    if genre == "":
        genre = ["pop", "rap", "rb", "rock"]
    else:
        genre = [genre]
    return templates.TemplateResponse("search.html", {
        "request": request,
        "genre": ["pop", "rap", "rb", "rock"],
        "result": neural_searcher.search(text=q, genre=genre)
    })


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get('PORT', 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
