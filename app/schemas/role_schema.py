from  pydantic import BaseModel,Enum

class Role(BaseModel):
    role_name:str
