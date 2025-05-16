from .. import schemas,models
from ..database import get_db
from fastapi import status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import desc

router = APIRouter( prefix='/posts')
@router.post('/create', status_code=status.HTTP_201_CREATED) #anytime we create sth we need to have 201
async def create_story(story:schemas.Createpost, db:Session = Depends(get_db)):
      new_post = models.Post(**story.model_dump()) # **story.model_dump() unpacks pydantic model story to a dict--
      #same as writing models.Post(title=story.title, content=story.content, private=story.private)
      db.add(new_post)
      db.commit()
      db.refresh(new_post)

      return new_post

@router.get('/', response_model=List[schemas.Get_response]) #we need to return a list of posts
async def get_posts(db:Session = Depends(get_db)):
      posts = db.query(models.Post).all()
      return posts
@router.get('/latest', response_model=schemas.Response)
def latest_post(db:Session = Depends(get_db)):
      post_l = db.query(models.Post).order_by(desc(models.Post.id)).first()
      return post_l
@router.get('/find/{id}', response_model=schemas.Response)
def find_post(id:int, db:Session = Depends(get_db)):
      wanted_post = db.query(models.Post).filter(models.Post.id ==id).first() #can't use one() here bc that has to return one value, and will gen a error if not
      if not wanted_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail = 'Oops we don\'t have that data with us' ) #apparently this is better
            #response.status_code = status.HTTP_404_NOT_FOUND
            #return{'Oops we don\'t have that data with us'}
      else:
            return(wanted_post)
      
@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(id: int,db:Session = Depends(get_db)):
      deleted_post = db.query(models.Post).filter(models.Post.id == id)
      if deleted_post.first() == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'could not find the post with id:{id}')    
      else:
            deleted_post.delete(synchronize_session=False)
            db.commit()
@router.put('/update/{id}')
async def update_posts(id: int, post:schemas.Update,db:Session = Depends(get_db) ):
      post_query = db.query(models.Post).filter(models.Post.id == id)
      updated_post = post_query.first()
      
      if updated_post== None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'could not find the post with id:{id}')
      else:
            post_query.update(post.model_dump(),synchronize_session=False) #accepts dict unlike create posts
            db.commit()
            updated_post = post_query.first()
            return {
                  "message": "Successfully updated your post!",
                  "updated_post": updated_post
            }