from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schema.loan_schema import loan_schema
from models.loan_model import loan_data
from database import SessionLocal, engine,Base
from models.customer_model import Customer_model # Jo aapke customer file/class ka naam ho
from models.employee_model import Employee_model # Jo aapke employee file/class ka naam ho
from models.manager_model import Manager_model


router = APIRouter()



Base.metadata.create_all(bind=engine)
# table  banane ke liye 



# depends
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/loan_details")
def post_loan_details(t:loan_schema,db:Session=Depends(get_db)):
    loan_data1=loan_data(customer_id=t.customer_id,employee_id=t.employee_id,manager_id=t.manager_id,status=t.status)
    db.add(loan_data1)
    db.commit()
    db.refresh(loan_data1)
    return {
        "message":"Here is the customer data",
        "details":loan_data1
    }


@router.get("/loan_details")
def get_loan_details(db:Session=Depends(get_db)):
    loan_data2=db.query(loan_data).all()
    return{
         "message":"Here is the loan data",
        "details":loan_data2
    }







   
