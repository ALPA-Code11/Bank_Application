from pydantic import BaseModel
from typing import optional
from enum import Enum

# Loan apply krne ke liye 

class LoanStatus(str,Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"






class LoanCreate(BaseModel):
    loan_amount:float
    loan_type:str
    customer_id:int


# Loan status update krne ke liye schmena 

class LoanStatusUpdate(BaseModel):
    status:LoanStatus


class LoanResposne(BaseModel):
    id:int
    customer_id:int
    loan_amount:float
    loan_type:str
    status:LoanStatus


    class Config:
        from_attributes = True
