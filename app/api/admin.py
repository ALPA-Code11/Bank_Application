from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db

from models.role_model import Role_model
from models.permission_model import Permission_model
from models.RolePermissionModel import Role_Permission_Model

from schemas.role_schema import RoleCreate, RoleResponse
from schemas.permission_schema import Permission_Create,Permission_Response
from schemas.role_permission_schema import AssignPermission

router = APIRouter(prefix="/admin", tags=["Admin Operations"]) # Prefix laga diya taaki main.py saaf rahe

@router.post("/roles",status_code=status.HTTP_201_CREATED)
def admin_roles(t:RoleCreate,db:Session=Depends(get_db)):
    existing_role=db.query(Role_model).filter(Role_model.role_name==t.role_name).first()
    if existing_role:
        raise HTTPException(status_code=400,detail=f"Role '{role_name}' already exits!")

    new_role=Role_model(role_name=t.role_name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return {"message": f"Role '{new_role.role_name}' created successfully", "role_id": new_role.role_id}


# Permission route create krna 
@router.post("/permission",response_model=Permission_Response, status_code=status.HTTP_201_CREATED)
def admin_permission(p:Permission_Create,db:Session=Depends(get_db)):
    existing_permission=db.query(Permission_model).filter(Permission_model.permission_name==p.permission_name).first()
    if existing_permission:
        raise HTTPException(status_code=400,details="Permsission already exists!")

    new_permission=Permission_model(permission_name=p.permission_name)
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)

    return new_permission



@router.post("/roles/assign-permission", status_code=status.HTTP_200_OK)
def assign_permission_to_role(t: AssignPermission, db: Session = Depends(get_db)):
    # 🔍 CHECK 1: Kya woh Role database mein sach mein hai?
    role = db.query(Role_model).filter(Role_model.role_id == t.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found!")

    # 🔍 CHECK 2: Kya woh Permission database mein sach mein hai?
    permission = db.query(Permission_model).filter(Permission_model.permission_id == t.permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found!")

    # 🔍 CHECK 3: Kya yeh dono pehle se hi aapas mein linked hain? (Duplicate Check)
    existing_role_permission = db.query(Role_Permission_Model).filter(
        Role_Permission_Model.role_id == t.role_id,
        Role_Permission_Model.permission_id == t.permission_id
    ).first()
    
    if existing_role_permission:
        raise HTTPException(status_code=400, detail="This permission is already assigned to this role!")

    # ✍️ AGAR SAB SAHI HAI, TOH DATABASE MEIN ENTRY DAALO
    new_mapping = Role_Permission_Model(
        role_id=t.role_id, 
        permission_id=t.permission_id
    )
    db.add(new_mapping)
    db.commit()

    return {"message": f"Permission successfully assigned to Role '{role.role_name}'"}



















