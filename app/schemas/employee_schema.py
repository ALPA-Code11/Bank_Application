from pydantic import BaseModel,EmailStr

# 1. Register karne ke liye Schema

class EmployeeCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    employee_name:str
    manager_id:int


class EmployeeResponse(BaseModel):
    id:int
    username:str
    employee_name:str
    manager_id:int
    email:EmailStr


    class Config:
        from_attributes = True
