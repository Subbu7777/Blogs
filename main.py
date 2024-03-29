from fastapi import FastAPI,Depends,status,Response,HTTPException
#import sqlite3
import uvicorn
from typing import List
#import database
#import schemas #file name
import models #file name
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
#from .routers.blog import APIRouter
from routers.blog import router as blogrouter
from routers.user import router as userrouter
from routers.authentication import router as authrouter
app=FastAPI()  
#from routers import blog,user,authentication


models.Base.metadata.create_all(engine)

# def get_db():
#    db=SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create(request: schemas.Blog,db: Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     #a=request.ID
#     #b=request.title
#     #c=request.body
#    # database.update(a,b,c)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
# @app.get('/blog',response_model=List[schemas.ShowBlog])

# def all(db: Session=Depends(get_db)):
#    blogs=db.query(models.Blog).all()
#    return blogs

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
# def show(id,response: Response,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id{id} is not available")

    #    response.status_code=status.HTTP_404_NOT_FOUND
    
    #return blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
# def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id{id} not found")
    
#     blog.update(request)
#     db.commit()
#     return 'updated'
# @app.post('/user')
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     new_user=models.User(name=request.name,email=request.email,password=request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

app.include_router(authrouter)
app.include_router(blogrouter)
app.include_router(userrouter)
#app.include_router(APIRouter)
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port="8000")
    

