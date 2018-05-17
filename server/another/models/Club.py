from sqlalchemy import Column, Integer, String, ForeignKey

from models.Base import BaseModel


class Club(BaseModel):
    __tablename__ = 'club'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))
    description = Column(String(30), nullable=True)


class MemberShip(BaseModel):
    __tablename__ = 'club_membership'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))
    club_id = Column(Integer, ForeignKey('club.id', ondelete='CASCADE', onupdate='CASCADE'))
    role = Column(Integer)
    # join_time = Column(Datetime)
