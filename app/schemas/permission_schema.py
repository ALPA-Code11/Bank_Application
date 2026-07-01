from pydantic import BaseModel
from enum import Enum


class Permission(str,Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"




class PermissionSchema(BaseModel):
    id:int
    permission_name:Permission

    class Config:
        from_attributes = True

        




