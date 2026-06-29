from pydantic import BaseModel

class Manager_schema(BaseModel):
    manager_name:str


    model_config = {
        "from_attributes": True
    }
