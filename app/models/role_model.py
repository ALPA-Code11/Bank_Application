from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base



class Role_model(Base):
    __tablename__ = "Role_Details"

    role_id=Column(Integer, primary_key=True, index=True)
    role_name=Column(String,unique=True,nullable=False)


    permissions = relationship("Permission_model", secondary="role_permissions", back_populates="roles")
    
    