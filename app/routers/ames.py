from curses.ascii import HT
from fastapi import APIRouter
from datetime import datetime
from .. import schemas,models
from ..database import get_db
from fastapi import status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'],deprecated = "auto")
def pwd(password : str):
    return pwd_context.hash(password)
router = APIRouter()
@router.get('/hello')
async def home():
    return{'Hello world'}
@router.get('/time')
async def time():
    return{"time":datetime.now().strftime("%H:%M:%S")}
@router.post('/login_ames')
def login(data: schemas.User_Input, db:Session = Depends(get_db)):
    e = data.email
    cred = db.query(models.User).filter(models.User.email == e).first()
    if not cred:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Oops, we could not find an account with this email')
    else:
        if pwd_context.verify(data.password, cred.password):
            return {f'{cred.Username}! Glad you are here'}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credentials')


    