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
    owner_id: str
    description: str
    model_config= ConfigDict(from_attributes=True)


class ResourceCreate(Resource):
    owner_id: str
    title: str
    url: str
    tags: str
    description: str
    model_config= ConfigDict(from_attributes=True)

class ResourceUpdate(BaseModel):
    title: str
    url: str
    tags: str
    description: str
    model_config= ConfigDict(from_attributes=True)

class ResourceResponse(Resource):
    id: int
    owner_id: str
    model_config= ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email:str
    password:str
    model_config = ConfigDict(from_attributes= True)

class UserLogin(BaseModel):
    email:str
    password:str
    model_config = ConfigDict(from_attributes= True)