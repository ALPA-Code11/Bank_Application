from pydantic import BaseModel

class loan_schema(BaseModel):
    customer_id: int
    employee_id: int
    manager_id: int
    status: str

    


    model_config = {
        "from_attributes": True
    }