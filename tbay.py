from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime,Float

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Item(Base):
      
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    __tablename__ = "bidmodel"
    id = Column(Integer,primary_key=True)
    price = Column(Float,nullable=False)
    
    __tablename__ = "usermodel"
    id = Column(Integer,primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    
Base.metadata.create_all(engine)
    
