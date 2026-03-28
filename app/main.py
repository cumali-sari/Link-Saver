from fastapi import FastAPI, Request
from app.routers import resources, users
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(resources.router)
app.include_router(users.router)

@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}  
    )
