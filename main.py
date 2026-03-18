from fastapi import FastAPI
from services.google import get_google_results

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/search")
def search(q: str):
    return {"results": get_google_results(q)}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


