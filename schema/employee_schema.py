from pydantic import BaseModel

class employee(BaseModel):
    employee_name=str

    model_config = {
        "from_attributes": True
    }