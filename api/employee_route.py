from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from schema.employee_schema import Employee_schema
from  models.employee_model import Employee_model
from database import SessionLocal, engine,Base

app=FastAPI()



Base.metadata.create_all(bind=engine)
# table  banane ke liye 



# depends
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
   

@app.post("/employee_details")
def post_employee_details(t:Employee_schema,db:Session=Depends(get_db)):
    e_data=Employee_model(employee_name=t.employee_name)
    db.add(e_data)
    db.commit()
    db.refresh(e_data)
    return {
        "message":"Here is the employee data",
        "details":e_data
    }


@app.get("/employee_details")
def get_employee_details(db:Session=Depends(get_db)):
    e_data1=db.query(Employee_model).all()
    return {
        "message":"Here is the employee data",
        "details":e_data1
    }








