from .. import schemas,models,utils
from ..database import get_db
from fastapi import status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix='/users')
@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_user(data:schemas.User_data, db:Session = Depends(get_db)):
      e = data.email
      n = data.Username
      hashed_pwd = utils.pwd(data.password)
      data.password = hashed_pwd
      check = db.query(models.User).filter(models.User.email == e).first()
      check_name = db.query(models.User).filter(models.User.Username == n).first()
      if not check and not check_name:
            new_user = models.User(**data.model_dump())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return{f'Succesfully Created your account {n}'}
      elif check is not None:
            raise HTTPException(status_code=status.HTTP_226_IM_USED,
                                 detail=f'You already have an account with this email {check.Username}')
      elif check_name is not None:
            raise HTTPException(status_code=status.HTTP_226_IM_USED, 
                                detail='This username already exists, please Try with another username')
#what i want to do here is that i want to link posts of 1 user and anyone can get those posts based on whatever id you enter
@router.get('/{name}', response_model=List[schemas.User_response])
def get_users(name:str, db:Session = Depends(get_db)):
      posts = db.query(models.Post).filter(models.Post.Username == name).all()
      if not posts:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'No data from {name}')
      else:
            return posts
      

