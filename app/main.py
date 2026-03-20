from fastapi import FastAPI
from app.routers import resources, users
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(resources.router)
app.include_router(users.router)

@app.get("/")
def main_page():
    return "Hello"