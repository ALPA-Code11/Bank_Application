from pydantic import BaseModel

class manager(BaseModel):
    manager_name:str


    model_config = {
        "from_attributes": True
    }
