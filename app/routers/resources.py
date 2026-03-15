from fastapi import APIRouter, Depends
from app.database import get_db
from app.schemas import ResourceCreate





router= APIRouter()




@router.post("/resources", response_model= ResourceCreate)
def resource_create(resource: ResourceCreate, db= Depends(get_db)):
    db_resource= ResourceCreate(id= resource.id, title= resource.title, url= resource.url, tags= resource.tags)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)




