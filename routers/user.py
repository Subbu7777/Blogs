from fastapi import APIRouter,Depends,status,HTTPException
#from .. import database,schemas,models
#from ..schemas import User,ShowUser
#from ..database import get_db
from schemas import User,ShowUser
from database import get_db
from sqlalchemy.orm import Session
from hashing import Hash
#from repository import user
from .repository import user as dbuser
router=APIRouter()
router=APIRouter(tags=['users'])


@router.post('/user')
def create_user(request:User,db:Session=Depends(get_db)):
    return dbuser.create(request,db)
    # new_user=models.User(name=request.name,email=request.email,password=request.password)
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user

@router.get('/user/{id}',response_model=ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return dbuser.show(id,db)
    # user=db.query(models.User).filter(models.User.id==id)
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return user