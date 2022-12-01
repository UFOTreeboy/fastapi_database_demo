from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

#建立資料表
class Todo(Base):
    __tablename__ = 'usertask'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)
    
    def __repr__(self):
        return '<Todo %r>' % (self.id)

