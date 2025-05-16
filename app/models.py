
from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
class Post(Base):
    __tablename__= 'posts'
    id = Column(Integer, primary_key=True, nullable=False) # prim key+ int = serial
    title = Column(String, nullable=False)
    content = Column(String, primary_key=False, nullable=False)
    private = Column(Boolean, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    Username = Column(String,nullable=False)
class User(Base):
    __tablename__ = 'user_data'
    email = Column(String,nullable=False,unique= True)
    id = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    Username = Column(String,nullable=False, unique=True)

