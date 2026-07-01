from sqlalchemy import create_engine, Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base



class Permission_model(Base):
    __tablename__="Permission_Details"
    permission_id=Column(Integer, primary_key=True, index=True)
    permission_name=Column(String,unique=True,nullable=False)

    roles = relationship("Role_model", secondary="role_permissions", back_populates="permissions")
