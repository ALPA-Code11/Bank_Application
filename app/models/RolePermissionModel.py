from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class RolePermissionModel(Base):
    __tablename__ = "role_permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Yeh connect karega tumhare Role_model ke role_id se
    role_id = Column(Integer, ForeignKey("Role_Details.role_id", ondelete="CASCADE"), nullable=False)
    
    # Yeh connect karega tumhare Permission_model ke permission_id se
    permission_id = Column(Integer, ForeignKey("Permission_Details.permission_id", ondelete="CASCADE"), nullable=False)