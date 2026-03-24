from fastapi import APIRouter, Depends, HTTPException, Request
from app.schemas import *
from app.database import *
from app.models import *
from app.auth import *
import bcrypt
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import JSONResponse

router= APIRouter()
BASE_DIR= Path(__file__).resolve().parent.parent
templates= Jinja2Templates(directory= str(BASE_DIR/"templates"))

@router.get("/register")
def login_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
def register(user:UserCreate, db= Depends(get_db)):
    print("email")
 
    if (db.query(User).filter(User.email==user.email).first()):
        raise HTTPException(status_code=400, detail="User already exists.")

    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    db_user= User(email= user.email, password=hashed_pw)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "success"


        

@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(user: UserLogin, db= Depends(get_db)):
    found= db.query(User).filter(User.email==user.email).first()

    if not found or not bcrypt.checkpw(user.password.encode(),found.password.encode()):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = create_access_token(data={"sub": found.email})
    response = JSONResponse(content={"message": "success"})
    response.set_cookie(key="token", value=access_token, httponly=True)
    return response