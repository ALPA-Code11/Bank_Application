from pydantic import BaseModel

class Employee_schema(BaseModel):
    employee_name:str

    model_config = {
        "from_attributes": True
    }