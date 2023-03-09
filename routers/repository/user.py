from fastapi import APIRouter,Depends,status
from fastapi import FastAPI,Depends,status,Response,HTTPException
import schemas
import models
from typing import List
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from . import blog
from hashing import Hash

def create(request: schemas.User,db:Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user