from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base

class customer(Base):
    __tablename__="Customer_Details"
    customer_id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    phone=Column(String)
    loan_amount=Coulmn(Float)


    loan=relationship("loan_data",back_populates="employee_details")
