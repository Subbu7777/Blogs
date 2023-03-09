from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sQLALCHAMY_DATABASE_URL='sqlite:///./blog.db'

engine=create_engine(sQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})

Base=declarative_base()
#SessionLocal=sessionmaker(bind=engine,autoflush=False,auto_commit=False)

SessionLocal=sessionmaker(bind=engine,autoflush=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
#import sqlite3

#con=sqlite3.connect('mydatabase.sqlite')
#cur=con.cursor()
#cur.execute("create table da(id INTEGER  Auto_Increment, title VARCHAR, body VARCHAR, PRIMARY KEY (id))")
#con.commit()
#def update(i,t,b):
 #   ins="insert into da(id,title,body) values(?,?,?)"
  #  a,b,c=i,t,b
   # m=[(a,b,c)]
    #cur.executemany(ins,m)
    #con.commit()