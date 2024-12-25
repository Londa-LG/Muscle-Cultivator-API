import os
from schema import TokenData
from dotenv import load_dotenv
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

current_dir = os.getcwd()
load_dotenv(os.path.join(current_dir, ".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 120

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_user(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def list_to_string(data):
    str_list = ""
    for item in data:
        str_list = str_list + item + ","
    
    return str_list

def string_to_list(data):
    new_list = data.split(",")
    new_list.remove("")

    return new_list

def dict_to_string(data):
    new_list = []
    for key,value in data.items():
       new_list.append(f"{key}:{value}")

    return list_to_string(new_list)
    
def string_to_dict(data):
    str_list = string_to_list(data)
    dict_list = []

    for pair in str_list:
        values = pair.split(":")
        dict_list.append((values[0],values[1]))

    return dict(dict_list)
