from fastapi import APIRouter, Depends, HTTPException
from app.schemas import *
from app.database import *
from app.models import *
import bcrypt


router= APIRouter()

@router.get("/register")
def login_page():
    pass

@router.post("/register")
def register(user:UserCreate, db= Depends(get_db)):
    if (db.query(User).filter(User.email==user.email).first()):
        raise HTTPException(status_code=400, detail="User already exists.")

    hashed_pw= bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    
    db_user= User(email= user.email,
                  password=hashed_pw.decode())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "Success"

@router.get("/login")
def login_page():
    pass

@router.post("/login")
def login(user: UserLogin, db= Depends(get_db)):
    found= db.query(User).filter(User.email==user.email).first()

    if not found or not bcrypt.checkpw(user.password.encode(),found.password.encode()):
        raise HTTPException(status_code=400, detail= "Invalid Credentials")
    
    return "Success"