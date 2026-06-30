from pydantic import BaseModel,EmailStr

class ManagerCreate(BaseModel):
    username:str
    password:str
    cluster_name:str
    manager_name:str
    # E.g., "North-Region", "Lucknow-Cluster" (Ki woh kis area ka head hai)

class ManagerResponse(BaseModel):
    id:int
    manager_name:str
    email:EmailStr
    cluster_name:str




    model_config = {
        "from_attributes": True
    }
