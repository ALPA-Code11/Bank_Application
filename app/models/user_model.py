from sqlalchemy import create_engine, Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base


class User_model(Base):
    __tablename__="User_Details"

    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    role_id = Column(Integer, ForeignKey("Role_Details.role_id", ondelete="RESTRICT"), nullable=False)


    role_id = Column(Integer, ForeignKey("Role_Details.role_id", ondelete="RESTRICT"), nullable=False)

    manager_profile = relationship("Manager_model", back_populates="user_details", uselist=False)
    employee_profile = relationship("Employee_model", back_populates="user_details", uselist=False)
    customer_profile = relationship("Customer_model", back_populates="user_details", uselist=False)







