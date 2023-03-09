from fastapi import APIRouter,Depends,status,HTTPException
import schemas
from sqlalchemy.orm import Session
import database
from hashing import Hash
import tokenn
import models
from token import *
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(tags=['Authentication'])

# @router.post('/login')

# def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
#     user=db.query(models.User).filter(models.User.name==request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Invalid credentials")
#     if not Hash.verify(user.password,request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")
    
#     access_token=tokenn.create_access_token(
#         data={"sub":user.email})
#     return {"access_token": access_token,"token_type":"bearer"}


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = tokenn.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/login") 
def hello():
    print("Hello world")