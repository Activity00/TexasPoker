# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/25 10:50
"""
import json

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/texaspoker')
Base = declarative_base()


def _gen_tuple(self):
    def convert_datetime(value):
        if value:
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return ""

    for col in self.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(self, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(self, col.name))
        else:
            value = getattr(self, col.name)
        yield (col.name, value)


def to_dict(self):
    return dict(self._gen_tuple())


def to_json(self):
    return json.dumps(self.to_dict())


Base._gen_tuple = _gen_tuple
Base.to_dict = to_dict
Base.to_json = to_json


DBSession = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(128), unique=True, nullable=False)
    coin = Column(Integer, default=1000)



