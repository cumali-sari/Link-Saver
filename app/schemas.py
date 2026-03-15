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


class ResourceCreate(BaseModel):
    title: str
    url: str
    tags: str
    description: str
    model_config= ConfigDict(from_attributes=True)

class ResourceUpdate(BaseModel):
    id: int
    title: str
    url: str
    tags: str
    model_config= ConfigDict(from_attributes=True)

class ResourceResponse(BaseModel):
    id: int
    title: str
    url: str
    tags: str
    model_config= ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email:str
    password:str
    model_config = ConfigDict(from_attributes= True)

class UserLogin(BaseModel):
    email:str
    password:str
    model_config = ConfigDict(from_attributes= True)