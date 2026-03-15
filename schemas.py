from typing import List
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    email:str
    password:str
    model_config = ConfigDict(from_attributes= True)

class Resource(BaseModel):
    id: int
    title: str
    url: str
    tags: str
    owner_id: int
    model_config= ConfigDict(from_attributes=True)