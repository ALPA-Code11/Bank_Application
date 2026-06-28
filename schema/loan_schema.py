from pydantic import BaseModel

class loan(BaseModel):
    status:str


    model_config = {
        "from_attributes": True
    }