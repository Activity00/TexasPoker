from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Base import BaseModel

DB_CONNECT_STRING = 'mysql+pymysql://root:root@localhost/texaspoker?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)


def init_db():
    import models
    BaseModel.metadata.create_all(engine)


def drop_db():
    import models
    BaseModel.metadata.drop_all(engine)

