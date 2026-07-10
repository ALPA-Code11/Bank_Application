from pydantic import BaseModel




class Permission_Create(BaseModel):
    
    permission_name:str




class Permission_Response(BaseModel):
    permission_id:int
    permission_name:str

    class Config:
        from_attributes = True

        




