from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base

class Employee_model(Base):
    __tablename__="Employee_Details"
    employee_id=Column(Integer,primary_key=True)
    employee_name=Column(String)
   

#    loan=relationship("loan_data",back_populates="employee_details")
    

