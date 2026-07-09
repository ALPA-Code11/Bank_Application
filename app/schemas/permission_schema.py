from pydantic import BaseModel
from enum import Enum


class Permission(str,Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"



class Permission_Create(BaseModel):
    id:int
    permission_name:Permission




class Permission_Response(BaseModel):
    id:int
    permission_name:Permission

    class Config:
        from_attributes = True

        




