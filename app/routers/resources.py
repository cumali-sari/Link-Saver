from fastapi import APIRouter, Depends,HTTPException, Request
from app.database import *
from app.schemas import *
from  app.models import*
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import List

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


@router.put("/resources/{id}", response_model= ResourceResponse )
def resource_update(id: int, resource: ResourceUpdate, db = Depends(get_db)):
    res = db.query(Resource).filter(Resource.id== id).first()
    res.title = resource.title
    res.url = resource.url
    res.tags = resource.tags
    res.description = resource.description
    db.commit()
    db.refresh(res)
    return res
@router.delete("/resources/{id}")
def resource_delete(id:int, db= Depends(get_db)):
    try:
        db.query(Resource).filter(Resource.id== id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return "Deleted succesfully"



