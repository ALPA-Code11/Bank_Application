from fastapi import FastAPI
from database import engine, Base

# 1. Sabse pehle saare models import karein taaki SQLAlchemy ko unka pata chal sake
# (Isse NoReferencedTableError jaisi dikkatein kabhi nahi aayengi)
from models.customer_model import Customer_model
from models.employee_model import Employee_model
from models.manager_model import Manager_model
from models.loan_model import loan_data  # Aapki loan class ka naam

# 2. Apne saare API Routers ko import karein
from api.customer_route import router as customer_router
from api.loan_route import router as loan_router
from api.employee_route import router as employee_router
from api.manager_route import router as manager_router

# Agar employee ya manager ke bhi alag routes hain, toh unhe bhi yahan import kar sakti hain

# 3. Database mein saari tables ko automatic create karne wala code
# (Ab aapko har file mein alag se create_all likhne ki zaroorat nahi hai)
Base.metadata.create_all(bind=engine)

# 4. Main FastAPI App ka instance banayein
app = FastAPI(
    title="Bank Application API",
    description="Backend for Customer, Employee, Manager, and Loan Management",
    version="1.0.0"
)

# 5. Saare Routers (Mini-Apps) ko Main App ke andar include/jod dein
app.include_router(customer_router)
app.include_router(loan_router)
app.include_router(employee_router)
app.include_router(manager_router)

# 6. Ek simple Home / Root Welcome route
@app.get("/")
def home():
    return {
        "message": "Welcome to the Bank Application Backend!",
        "status": "Running Successfully",
        "docs": "Go to /docs to see all API endpoints"
    }