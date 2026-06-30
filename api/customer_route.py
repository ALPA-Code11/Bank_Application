from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schema.customer_schema import Customer_schema
from models.customer_model import Customer_model
from database import SessionLocal, engine,Base

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


@router.post("/customer_details")
def  post_customer_details(t:Customer_schema,db:Session=Depends(get_db)):
    customer_data=Customer_model(name=t.name,email=t.email,phone=t.phone,loan_amount=t.loan_amount)
    db.add(customer_data)
    db.commit()
    db.refresh(customer_data)
    return {
        "message":"Here is the customer data",
        "details":customer_data
    }


@router.get("/customer_details")
def get_customer_details(db:Session=Depends(get_db)):
    customer_data1=db.query(Customer_model).all()
    return {
        "message":"Here is the customer data",
        "details":customer_data1
    }


    




   



