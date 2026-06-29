from pydantic import BaseModel

class Customer_Schema(BaseModel):
    name: str
    email: str
    phone: str
    loan_amount: float

    
