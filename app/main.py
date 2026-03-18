from fastapi import FastAPI
from app.routers import resources, users


app = FastAPI()

app.include_router(resources.router)
app.include_router(users.router)

@app.get("/")
def main_page():
    return "Hello"