
from datetime import  datetime
from pydantic import BaseModel, EmailStr
class PostBase(BaseModel):
       title: str
       content: str
       private: bool = True
       Username : str
       #comment: Optional[str] = None #optional is the real highligh, these are things user can proceed without inputting                    
class Createpost(PostBase):
       pass
class Response(PostBase):
       created_at:datetime
       class Config:  #needed bc by default pydantic model expects us to provide a dict, since we are returning data, it comes as a sqlalchemy object
            from_attributes = True
class Get_response(PostBase):
       id: int
       pass 
class User_data(BaseModel):
       email : EmailStr
       password : str
       Username : str
class User_response(BaseModel):
       title: str
       content: str
       created_at:datetime
       class Config: 
            from_attributes = True
class Update(BaseModel):
       title: str
       content: str
       private: bool = True
class User_Input(BaseModel):
       email : EmailStr
       password : str