from sqlalchemy import Column, Integer, String, create_engine
from models.Base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(20))
    password = Column(String(32))

    coin = Column(Integer)
    diamond = Column(Integer)
