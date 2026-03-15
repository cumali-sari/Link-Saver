from fastapi import FastAPI
from app.routers import resources
app = FastAPI()

app.include_router(resources.router)