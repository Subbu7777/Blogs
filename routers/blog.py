from fastapi import APIRouter,Depends,status,UploadFile
from fastapi import FastAPI,Depends,status,Response,HTTPException,File
import aiofiles
import schemas
from secrets import token_hex
import models
from typing import List
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from .repository import blog
import oauth2
import database
import uvicorn
import json
import os
import time
import yaml
import shutil
from fastapi.responses import FileResponse
timestr=time.strftime("%Y%m%d-%H%M%S")
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR=os.path.join(BASE_DIR,"uploads")

router=APIRouter(
    prefix="/blog",
)
get_db=database.get_db
router=APIRouter(tags=['Blogs'])

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog,db: Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id : int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.show(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog.destroy(id,db)

@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id :int,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)


# @router.post("/upload")
# def upload(file:UploadFile=File(...)):
#     file_ext=file.filename.split(".").pop()
#     file_name=token_hex(10)
#     file_path=f"{file_name}.{file_ext}"
#     with open(file_path,'wb') as f:
#         content=await file.read()
#         f.write(content)
#     return {'success':True,"file_path":file_path,"message":"file uploaded successfully"}




@router.post("/upload-files")
async def create_upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        destination_file_path = r"C:\Users\stanneeru\Desktop\Blog\uploads"+file.filename #output file path
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(1024):  # async read file chunk
                await out_file.write(content)  # async write file chunk
    return {"Result": "OK", "filenames": [file.filename for file in files]}

#if __name__=="__blog__":
 #   uvicorn.run(router,host="127.0.0.1",port="8000")


