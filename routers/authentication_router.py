from datetime import timedelta
from os import access
from databases import database
from fastapi import APIRouter, Depends, HTTPException, status
from models import blog
from schemas import schema
from sqlalchemy.orm import Session

from security import hashing
from security.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

login = APIRouter(
    tags = ["Authentication"]
)

@login.post("/login", status_code=status.HTTP_200_OK)
def user_login(request: blog.Login, db: Session = Depends(database.get_db)):
    
    """
    This function is used to validate a User Login 
    
    Parameters
    ----------
    request : blog.Login
        The request body of the type Login
    db : str
        The db instance
    """ 
    
    user = db.query(schema.UserModel).filter(schema.UserModel.username == request.username).first()
    if not user or not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
       
    return {"access_token": access_token, "token_type": "bearer"}
