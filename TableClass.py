import sqlalchemy  
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

engine = sqlalchemy.create_engine('sqlite:///C:\\Users\\user\\python\\hello\\mydb.db')
Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    num = Column(String(50), primary_key=True)
    name = Column(String(50))
    def __init__(self, num, name):
        self.num = num
        self.name = name
    def __repr__(self):
       return "<Students('%s', '%s')>" % (self.num, self.name)

def create_tb(engine):
    Base.metadata.create_all(engine)