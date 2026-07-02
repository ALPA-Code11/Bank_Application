from pydantic import BaseModel

class AssignPermission(BaseModel):
    role_id: int
    permission_id: int