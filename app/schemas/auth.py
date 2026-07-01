from pydantic import BaseModel,EmailStr
# from enum import Enum


# class UserRole(str,Enum):
#     MANAGER = "manager"
#     EMPLOYEE = "employee"
#     CUSTOMER = "customer"
# It is enum-harcoded value for user role, we can use it in the future if we want to implement role-based access control.


class UserRegisterRequest(BaseModel):
    # sabhi user ke liye common hai 
    username:str
    email:EmailStr
    password:str
    



class EmployeeRegisterRequest(UserRegisterRequest):
    manager_id:int
    employee_name: str



class CustomerRegisterRequest(UserRegisterRequest):
     employee_id:int
    customer_name: str
     phone: str      
     loan_amount: float

   




class LoginRequest(BaseModel):
    username:str
    password:str

 

    