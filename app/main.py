from fastapi import FastAPI
from app.routers import resources
app = FastAPI(docs_url="/resources/docs")

app.include_router(resources.router)