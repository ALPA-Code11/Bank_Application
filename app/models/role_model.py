from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base



class Role_model(Base):
    __tablename__:"Role_Details"
    