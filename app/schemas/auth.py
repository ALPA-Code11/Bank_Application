from pydantic import BaseModel,EmailStr
from enum import Enum


class UserRole(str,Enum):
    MANAGER = "manager"
    EMPLOYEE = "employee"
    CUSTOMER = "customer"


class RegisterRequest(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:UserRole


class EmployeeRegisterRequest(RegisterRequest):
    manager_id:int



class CustomerRegisterRequest(RegisterRequest):
     employee_id:int
   




class LoginRequest(BaseModel):
    username:str
    password:str

 

    