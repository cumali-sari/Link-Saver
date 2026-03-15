from fastapi import APIRouter, Depends
from app.database import *
from app.schemas import *
from  app.models import*
from fastapi import HTTPException

router= APIRouter()

@router.get("/resources")
def resources_page():
    pass

@router.post("/resources", response_model= ResourceResponse)
def resource_create(resource: ResourceCreate, db= Depends(get_db)):
    try:
        db_resource= Resource(title= resource.title, 
                              url= resource.url, 
                              tags= resource.tags, 
                              description= resource.description,
                              owner_id="system")
        db.add(db_resource)
        db.commit()
        db.refresh(db_resource)
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



