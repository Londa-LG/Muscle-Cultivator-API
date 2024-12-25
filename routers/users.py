from connect import get_db
from models import User_Model
from pydantic import EmailStr
from auth import get_current_user
from sqlalchemy.orm import Session
from schema import User, Token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from utils import pwd_context, verify_user, create_access_token
from fastapi import Depends,HTTPException,APIRouter,status


router = APIRouter(
    tags = ["Users end-points"],
    prefix = "/users"
)

@router.post("/login", response_model=Token)
def login_user(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    credentials.username = credentials.username.lower()
    user = db.query(User_Model).filter(User_Model.email == credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not verify_user(credentials.password, user.password):
        raise HTTPExcpetion(status_code=HTTP_404_NOT_FOUND, details="invalid credentials")
    access_token = create_access_token(data= {"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", status_code = status.HTTP_201_CREATED,response_model=User)
def create_user(data: User):
    pass

@router.get("/{id}", response_model=User)
def get_user(id: int):
    pass

@router.put("/{id}", response_model=User)
def update_user(id: int):
    pass

@router.delete("/{id}", response_model=User)
def delete_user(id: int):
    pass
