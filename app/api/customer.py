from fastapi import APIRouter, Depends, Session
from database import get_db
from model.customer_model import Customer_model
from deps import check_role  # 👈 Apne bodyguard file se check_role import kiya

# Humne prefix="/customers" de diya, toh ab URL automatic "/customers/all" ban jayega
router = APIRouter(prefix="/customers", tags=["Customer Management"])

@router.get("/all", dependencies=[Depends(check_role(["manager", "employee"]))])
def get_all_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer_model).all()
    return customers