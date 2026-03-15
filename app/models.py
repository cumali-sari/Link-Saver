from sqlalchemy import Column, Integer, String
from app.database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email= Column(String)
    password = Column(String)

class Resource(Base):
    __tablename__= "resources"
    id= Column(Integer, primary_key= True)
    title = Column(String)
    url = Column(String)
    tags = Column(String)
    description= Column(String)
    owner_id = Column(String)

Base.metadata.create_all(bind=engine)
