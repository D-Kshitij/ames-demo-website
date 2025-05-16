#JAI SHREE RAM
#this is the code without orm
from operator import indexOf
import time
from turtle import title
from fastapi import FastAPI,Response,status,HTTPException, Depends
from random import randrange
from typing import Optional
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)


class Post(BaseModel):
       title: str
       content: str
       private: bool = True
       #comment: Optional[str] = None #optional is the real highligh, these are things user can proceed without inputting

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

            
my_posts = [{'title':'Family resists intercaste marriage', 'content':'Blah blah blah', 'id':1},
            {'title':'Stubborn parents about higher education', 'content':'I\'m a 19yo girl...', 'id':'2'}]
def find(ide: int):
      for a in my_posts:
            if a['id'] == ide:
                  return(a)       
def find_index(ide: int):
      for i,p in enumerate(my_posts):
            if p['id']==ide:
                  return(i)
app = FastAPI()
@app.get("/")
def main():
    return{'say':'This is your Home Page;',
           'quote':'Smile wideeeeee!'}
@app.get('/test') #testing orm
def random(db:Session = Depends(get_db)): #db-var--session object frm sqlalchemy--= result from get_db--so db becomes session object
      posts = db.query(models.Post).all() #models represent tables
      return{'data':posts}
@app.post('/posts/create', status_code=status.HTTP_201_CREATED) #anytime we create sth we need to have 201
async def create_story(story:Post):
        cursor.execute('''insert into posts(title,content,private) values(%s,%s,%s)''', 
                       (story.title,story.content,story.private))
        conn.commit()
        
        return{'Message':'successfully created your post'}

@app.get('/posts')
async def get_posts():
      cursor.execute('''select * from posts;''')
      posts = cursor.fetchall()
      return(posts)
@app.get('/posts/latest')
def latest_post():
      cursor.execute('''select * from posts order by id desc limit 1''')
      post_l = cursor.fetchone()
      return{'latest post':post_l}
@app.get('/posts/find/{id}')
def find_post(id:int, response: Response): 
      cursor.execute('''select * from posts where id = (%s)''',(id,) ) #this is called parameterized queries
      wanted_post = cursor.fetchone()
      if not wanted_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail = 'Oops we don\'t have that data with us' ) #apparently this is better
            #response.status_code = status.HTTP_404_NOT_FOUND
            #return{'Oops we don\'t have that data with us'}
      else:
            return(f'here\'s the post with id:{id}',wanted_post)
      
@app.delete('/posts/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(id: int):
      cursor.execute('''delete from posts where id = %s returning*;''',(id,))
      deleted_post = cursor.fetchone()
      conn.commit()
      if deleted_post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'could not find the post with id:{id}')     
@app.put('/posts/update/{id}')
async def update_posts(id: int, post: Post ):
      cursor.execute('''update posts set title = %s, content=%s where id=%s returning *;''',(post.title,post.content,id))
      updated_post = cursor.fetchone()
      
      if updated_post== None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'could not find the post with id:{id}')
      else:
            return {
                  "message": "Successfully updated your post!",
                  "updated_post": updated_post
            }
#damn kshitij, nice code till now

       

#i can use mmy find fn, but it returns the entire data there; 



      
      
    
