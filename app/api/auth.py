from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db


from models.user_model import User_model
from models.role_model import Role_model
from models.manager_model import Manager_model
from models.employee_model import Employee_model
from models.customer_model import Customer_model
from schemas.user_schema import UserRegisterRequest, EmployeeRegisterRequest, CustomerRegisterRequest, UserLoginRequest

from utils import create_token



router = APIRouter(prefix="/auth", tags=["Authentication"])

# JWT Configuration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"











@router.post("/register/manager",status_code=status.HTTP_201_CREATED)
def register_manager(ud:UserRegisterRequest,db: Session = Depends(get_db)):

    # Check karo username duplicate toh nahi hai
    existing_user = db.query(User_model).filter(User_model.username == ud.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken!")

    manager_role=db.query(Role_model).filter(Role_model.role_name=="Manager").first()
    if not manager_role:
        raise HTTPException(status_code=400, detail="Manager role not found!")


    new_manager=User_model(
        username=ud.username,
        email=ud.email,
        password=ud.password,
        role_id=manager_role.role_id,
        # jo khud ki manager id hai woh 
         )

    db.add(new_manager)
    db.commit()
    db.refresh(new_manager)

    new_manager_details = Manager_model(
        manager_name=ud.username, # Ya jo bhi field tumne rakhi hai
        user_id=new_manager.user_id # Ye bahut zaroori hai!
    )
    db.add(new_manager_details)
    db.commit()
    return {"message": "Manager registered!"}






@router.post("/register/employee",status_code=status.HTTP_201_CREATED)
def register_employee(ed:EmployeeRegisterRequest,db: Session = Depends(get_db)):
    # check karenge  ki manaager hai ya nahi woh 

    manager_user=db.query(User_model).filter(User_model.user_id==ed.manager_id).first()
    if not manager_user:
        raise HTTPException(status_code=400, detail="Manager not found!")

    # check karenge ki employee hai ya nahi 

    employee_user=db.query(Role_model).filter(Role_model.role_name=="Employees").first()
    # iss line se puri row ka data aa jayega 

    if not employee_user:
        raise HTTPException(status_code=400, detail="Employee role not found!")

# 3. Pehle User_Details Table mein entry karo
    new_user=User_model(
        username=ed.username,
        email=ed.email,
        password=ed.password,
        role_id=employee_user.role_id,
    )   

    db.add(new_user)
    db.commit()  
    db.refresh(new_user)


    new_employee=Employee_model(
        employee_name=ed.employee_name,
        user_id=new_user.user_id,
        manager_id=ed.manager_id

    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {"message": "Employee registered successfully in both tables!"}




@router.post("/register/customer",status_code=status.HTTP_201_CREATED)
def register_customer(cd:CustomerRegisterRequest,db: Session = Depends(get_db)):

    # check ki employee sahi hai ya nahi 
    employee_user=db.query(User_model).filter(cd.employee_id==User_model.user_id).first()
    if not employee_user:
        raise HTTPException(status_code=400, detail="Employee not found!")

    customer_user=db.query(Role_model).filter(Role_model.role_name=="Customer").first()

    if not customer_user:
        raise HTTPException(status_code=400, detail="Customer role not found!")

    new_customer_user= User_model(
        username=cd.username,
        email=cd.email,
        password=cd.password,
        role_id=customer_user.role_id
    )    


    db.add(new_customer_user)
    db.commit()
    db.refresh(new_customer_user)


    new_customer=Customer_model(
        user_id=new_customer_user.user_id,
        employee_id=cd.employee_id,
        name=cd.customer_name,
        phone=cd.phone,
        loan_amount=cd.loan_amount

    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)    

    return {"message": "Customer registered successfully in both tables!"}

@router.post("/login")
def login(ld: UserLoginRequest, db: Session = Depends(get_db)):
    # Database se user dunda
    user = db.query(User_model).filter(User_model.username == ld.username).first()
    
    # Username ya Password galat hone par 401 error
    if not user or user.password != ld.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Ticket (Payload) mein user_id aur uska role_id bhi daal diya taaki aage kaam aaye
    token = create_token({
        "sub": user.username,
        "user_id": user.user_id,
        "role_id": user.role_id
    })
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "message": f"Welcome back {user.username}!"
    }




    