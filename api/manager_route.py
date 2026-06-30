from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from schema.manager_schema import Manager_schema
from  models.manager_model import Manager_model
from database import SessionLocal, engine,Base
# from models.loan_model import loan_data  # <--- Yeh line import mein daal do!

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
   


@router.post("/manager_details")
def manager_details(t:Manager_schema,db:Session=Depends(get_db)):
    m_data=Manager_model(manager_name=t.manager_name)
    db.add(m_data)
    db.commit()
    db.refresh(m_data)
    return{
        "message":"Here is the manager data",
        "details":m_data
    }

@router.get("/manager_get_details")
def manager_get_details(db:Session=Depends(get_db)):
    m_data1=db.query(Manager_model).all()
    return{
        "message":"Here is the entered data of the manager",
        "details":m_data1
    }




 