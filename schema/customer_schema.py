from pydantic import BaseModel

class Customer_schema(BaseModel):
    name: str
    email: str
    phone: str
    loan_amount: float

    model_config = {
        "from_attributes": True
    }

    
