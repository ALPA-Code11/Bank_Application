from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db


from model.user_model import User_model
from model.role_model import Role_model
from schema.user_schema import UserRegisterRequest


router=APIRouter()



@router.post("/register/manager",status_code=status.HTTP_201_CREATED)
def register_manager(ud:UserRegisterRequest,db: Session = Depends(get_db)):
    manager_role=db.query(Role_model).filter(Role_model.role_name=="manager").first()


    new_manager=User_model(
        username=ud.username,
        email=ud.email,
        hashed_password=ud.password,
        role_id=manager_role.id,
        

    )

    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)
    return {"message": "Manager registered!"}




@router.post("")


