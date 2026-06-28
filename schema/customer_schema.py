from pydantic import BaseModel

class customer(BaseModel):
    name: str
    email: str
    phone: str
    loan_amount: float

    
