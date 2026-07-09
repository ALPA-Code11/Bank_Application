from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base


class Employee_model(Base):
    __tablename__="Employee_Details"
    id=Column(Integer,primary_key=True)
    employee_name=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey("User_Details.user_id"))
    manager_id=Column(Integer,ForeignKey("Manager_Details.id"))


    user_details = relationship("User_model", back_populates="employee_profile")
    manager_details = relationship("Manager_model", back_populates="employees")
    customers = relationship("Customer_model", back_populates="employee_details") # 50-limit check karne ke liye kaam aayega
    


    