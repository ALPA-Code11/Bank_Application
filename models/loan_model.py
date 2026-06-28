from sqlalchemy import create_engine, Column, Integer, String,Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session,relationship
from database import Base


class loan_data(Base):
    __tablename__="loan_data"

    loan_id=Column(Integer,primary_key=True)
    customer_id=Column(Integer,ForeignKey("Customer_Details.customer_id"))
    employee_id=Column(Integer,ForeignKey("Employee_Details.employee_id"))
    manager_id=Column(Integer,ForeignKey("Manager_Details.manager_id"))
    status=Column(String)
    # -yeh khud se de hum 


    # relationship

    customer_details=relationship("customer",back_populates="loan")
    employee_details=relationship("employee",back_populates="loan")
    manager_details=relationship("manager",back_populates="loan")
















    tudent_details = relationship("Student", back_populates="borrows")
    book_details = relationship("Book", back_populates="borrows")
    librarian_details = relationship("Librarian", back_populates="handled_borrows")
    