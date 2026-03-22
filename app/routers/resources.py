from fastapi import APIRouter, Depends,HTTPException, Request, Form
from app.database import *
from app.schemas import *
from  app.models import*
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import List
from fastapi.responses import RedirectResponse

router= APIRouter()

BASE_DIR= Path(__file__).resolve().parent.parent
templates= Jinja2Templates(directory=str(BASE_DIR/ "templates"))

@router.get("/resources")
def resources_page(request: Request):
    return templates.TemplateResponse("add_resource.html", {"request": request})

@router.post("/resources", response_model= List[ResourceResponse])
def resource_create(resources: List[ResourceCreate], db= Depends(get_db)):
    try:
        db_resource= [Resource(**resource.model_dump()) for resource in resources]
        db.add_all(db_resource)
        db.commit()
        return db_resource
    except Exception as e:
        print(f"{e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/dashboard")
def bulk_update(
    title: list[str] = Form(...),
    url: list[str] = Form(...),
    tags: list[str] = Form(...),
    description: list[str] = Form(...),
    id: list[int] = Form(...),
    db= Depends(get_db)
):
    for i, t, u, tg, d in zip(id, title, url, tags, description):
        res = db.query(Resource).filter(Resource.id == i).first()
        res.title = t
        res.url = u
        res.tags = tg
        res.description = d

    db.commit()

    return RedirectResponse(url="/dashboard", status_code=303)

@router.delete("/resources/{id}")
def resource_delete(id:int, db= Depends(get_db)):
    
    db.query(Resource).filter(Resource.id== id).delete()
    db.commit()

@router.get("/dashboard")
def read_items(request: Request, db = Depends(get_db)):
    resources= db.query(Resource).all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "resources": resources})


