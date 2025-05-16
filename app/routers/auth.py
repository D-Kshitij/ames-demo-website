from .. import schemas,models,utils
from ..database import get_db
from fastapi import status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
router = APIRouter()
@router.post('/login')
def login(cred:schemas.User_Input, db:Session = Depends(get_db)):
    e = cred.email
    info = db.query(models.User).filter(models.User.email == e ).first()
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Oops, we didn\'t find the desired account')
    else:
        if utils.pwd_context.verify(cred.password, info.password):
            return{f'Hey {info.Username}, glad you are here'}
        else:
            return{'Invalid Credentials'}
