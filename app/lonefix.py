#JAI SHREE RAM
from curses.ascii import HT
from operator import indexOf
import time
from turtle import title
from fastapi import FastAPI,status,HTTPException, Depends
from random import randrange
from typing import List, Optional
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import desc
from . import models,schemas,utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post,users,auth,ames
models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware

while True:
      try:
            conn = psycopg2.connect(host='localhost',user='postgres',password='Kshitij@8167',database='fastapi'
                                    ,cursor_factory=RealDictCursor)#the last one;s to get the column names as well
            cursor = conn.cursor()
            print('Sucessfully established conection')
            break  
      except Exception as error:
            print('Connection could not be established')
            print('error: ',error)   
            time.sleep(2)

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def main():
    return{'say':'This is your Home Page;',
           'quote':'Smile wideeeeee!'}
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(ames.router)
#damn kshitij, nice code till now


      
      
    
