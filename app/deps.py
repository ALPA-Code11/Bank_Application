from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from database import get_db
from models.user_model import User_model



# 1. Yeh FastAPI ka standard tareeqa hai token headers se nikalne ka
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


SECRET_KEY = "mysecret"
ALGORITHM = "HS256"



# 🌟 ASSLI BODYGUARD FUNCTION: Yeh check karega ki token kiske paas hai
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # Token ko khola (Decode kiya)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid Token")
    except:
        raise HTTPException(status_code=401, detail="Could not validate credentials")



# Database se check kiya ki yeh user sach mein hai na
    user = db.query(User_model).filter(User_model.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
        
    return user # Yeh poora user ka object (with role_id) aage bhej dega



# 🌟 ROLE CHECKER: Yeh batayega ki kya is bande ke paas access hai?
def check_role(allowed_roles: list[str]):
    def role_checker(current_user: User_model = Depends(get_current_user), db: Session = Depends(get_db)):
        # current_user ke paas uski role_id hai, hum uske role ka naam check karenge
        if current_user.role.role_name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="No Access! Tumhare paas iski permission nahi hai."
            )
        return current_user
    return role_checker





    