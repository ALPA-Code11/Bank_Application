from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base


class Manager_model(Base):
    __tablename__="Manager_Details"
    manager_id=Column(Integer,primary_key=True)
    manager_name=Column(String)

    # loan=relationship("loan_data",back_populates="manager_details")
    

