from pydantic import BaseModel,EmailStr

class CustomerCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    name:str
    phone:str
    loan_amount:float
    employee_id:int
    # Yeh check karega hamari 50-limit wali conditio

class CustomerResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:str
    loan_amount:str
    employee_id:int


    class Config:
        from_attributes = True




