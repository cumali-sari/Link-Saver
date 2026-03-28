from fastapi import FastAPI, Request
from app.routers import resources, users
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(resources.router)
app.include_router(users.router)

BASE_DIR= Path(__file__).resolve().parent
templates= Jinja2Templates(directory=str(BASE_DIR/ "templates"))

@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
