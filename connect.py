import os
from schema import TokenData
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

current_dir = os.getcwd()
load_dotenv(os.path.join(current_dir, ".env"))

engine = create_engine(os.environ.get("SQLALCHEMY_DATABASE_URL"))

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

