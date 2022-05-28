from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://test:toor@localhost:3306/fastapi"

'''The below engine configuration is needed for SQLite DB'''
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


'''The below engine configuration is needed for MYSQL DB'''
#engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    
    """This method configures the DB layer to be used by the methods"""
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
