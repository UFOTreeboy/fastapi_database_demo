from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

#建立資料表
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(str)
    task = Column(Text)
   

    def __repr__(self):
        return '<Todo %r>' % (self.id)