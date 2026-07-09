from fastapi import FastAPI
# 1. Saare routers ko unki sahi files se import kiya (admin ko bhi jodh liya)
from app.auth import router as auth_router
from app.customer import router as customer_router
from app.admin import router as admin_router # 👈 Yeh tumhara dhasu point!

app = FastAPI(
    title="Bank Management System API",
    description="Manager, Employee, aur Customer ke liye RBAC aur Loan Management System",
    version="1.0.0"
)

# 2. Teeno counters (routers) ko main engine se jodh diya
app.include_router(auth_router)
app.include_router(customer_router)
app.include_router(admin_router) # 👈 Admin router ko yahan include kar liya!

# 🏠 Basic home route
@app.get("/")
def home():
    return {"message": "Welcome to Bank Management System API! Server ekdam mast chal raha hai."}