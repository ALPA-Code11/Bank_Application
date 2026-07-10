from fastapi import FastAPI
from database import engine, Base  
# 👈 Database se engine aur Base lekar aaye

# 🚨 Saare models ko yahan import kiya taaki pgAdmin mein tables ban sakein!
from models.role_model import Role_model
from models.permission_model import Permission_model
from models.RolePermissionModel import Role_Permission_Model
from models.user_model import User_model
from models.manager_model import Manager_model
from models.employee_model import Employee_model

from models.customer_model import Customer_model


# 💥 'app.' hata diya aur 'api.' jodh diya kyunki files api folder mein hain
from api.auth import router as auth_router
from api.customer import router as customer_router
from api.admin import router as admin_router

# 🚀 Yeh line database mein saari tables ek baar mein bana degi!
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bank Management System API",
    description="Manager, Employee, aur Customer ke liye RBAC aur Loan Management System",
    version="1.0.0"
)

# Routers link kiye
app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(admin_router)

@app.get("/")
def home():
    return {"message": "Welcome to Bank Management System API! Server ekdam mast chal raha hai."}

# 👇 Uvicorn ko Python se chalane ke liye code ka tukda
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)