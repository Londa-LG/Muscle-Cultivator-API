from connect import get_db
from pydantic import EmailStr
from models import User_Model
from auth import get_current_user
from sqlalchemy.orm import Session
from schema import User, User_Response, Token
from utils import list_to_string, string_to_list
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from utils import pwd_context, verify_user, create_access_token
from fastapi import Depends,HTTPException,APIRouter,status,Response


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
        raise HTTPExcpetion(status_code=HTTP_404_NOT_FOUND, detail="invalid credentials")
    access_token = create_access_token(data= {"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", status_code = status.HTTP_201_CREATED,response_model=User_Response)
def create_user(data: User,db: Session = Depends(get_db)):
    data.workouts = list_to_string(data.workouts)
    data.awards = list_to_string(data.awards)

    new_user = User_Model(**data.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_user.workouts = string_to_list(new_user.workouts)
    new_user.awards = string_to_list(new_user.awards)

    return new_user

@router.get("/{id}", response_model=User_Response)
def get_user(id: int,db: Session = Depends(get_db)):
    user = db.query(User_Model).filter(User_Model.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user with that id found")

    user.workouts = string_to_list(user.workouts)
    user.awards = string_to_list(user.awards)

    return user

@router.put("/{id}", response_model=User_Response)
def update_user(id: int,data: User,db: Session = Depends(get_db)):
    data.workouts = list_to_string(data.workouts)
    data.awards = list_to_string(data.awards)

    user = db.query(User_Model).filter(User_Model.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user with that id found")

    user.update(data.dict())
    db.commit()

    user = user.first()
    user.workouts = string_to_list(user.workouts)
    user.awards = string_to_list(user.awards)

    return user

@router.delete("/{id}", response_model=User_Response)
def delete_user(id: int,db: Session = Depends(get_db)):
    user = db.query(User_Model).filter(User_Model.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user with that id found")

    user.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
