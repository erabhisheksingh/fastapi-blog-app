
from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from models import blog
from databases import database
from schemas import schema
from security import hashing

userroute = APIRouter()

@userroute.post("/users", status_code=status.HTTP_201_CREATED, response_model=blog.UserResponse, tags=['Users'])
def create_user(request: blog.User, db: Session = Depends(database.get_db)):

    """
    This function is used to create a User 
    
    Parameters
    ----------
    request : blog.User
        The request body of the type User
    db : str
        The db instance
    """
    
    hashed_password = hashing.Hash.hash(request.password)
    new_user = schema.UserModel(username = request.username, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@userroute.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=blog.UserResponse, tags=['Users'])
def get_user(id: int, response: Response, db: Session = Depends(database.get_db)):
    
    """
    This function is used to GET a user 
    
    Parameters
    ----------
    id: int
        The id of the blog
    request : blog.Blog
        The request body of the type Blog
    db : str
        The db instance
    """
    
    user = db.query(schema.UserModel).filter(schema.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with the Id {id} is not found")
    return user
