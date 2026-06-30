from pydantic import BaseModel,EmailStr
from enum import Enum


class USerRole(str,Enum):
    MANAGER = "manager"
    EMPLOYEE = "employee"
    CUSTOMER = "customer"


class RegisterRequest(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:USerRole


class LoginRequest(BaseModel):
    username:str
    password:str



    