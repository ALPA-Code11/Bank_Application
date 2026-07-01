from sqlalchemy import create_engine, Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base


class Manager_model(Base):
    __tablename__ = "Manager_Details"
    id=Column(Integer,primary_key=True)
    manager_name=Column(String)
    cluster_name=Column(String)
    user_id=Column(Integer,ForeignKey("User_Details.user_id"))


    user_details = relationship("User_model", back_populates="manager_profile")
    employees = relationship("Employee_model", back_populates="manager_details") # Ek manager ke under kai employees













