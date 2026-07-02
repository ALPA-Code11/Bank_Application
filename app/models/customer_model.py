from sqlalchemy import create_engine, Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base



class Customer_model(Base):
    __tablename__ = "Customer_Details"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User_Details.user_id"))
    employee_id=Column(Integer,ForeignKey("Employee_Details.id"))
    name=Column(String,nullable=False)
    phone=Column(String,unique=True,nullable=False)
    loan_amount=Column(Float)

    user_details = relationship("User_model", back_populates="customer_profile")
    employee_details = relationship("Employee_model", back_populates="customers")
    



















    
    
    