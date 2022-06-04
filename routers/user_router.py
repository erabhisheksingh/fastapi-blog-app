from databases import database
from fastapi import APIRouter, Depends, status
from models import blog
from repository import user_repository as userrepo
from security import hashing
from sqlalchemy.orm import Session

userroute = APIRouter(
    prefix = "/users",
    tags = ['Users']
)

@userroute.post("/", status_code=status.HTTP_201_CREATED, response_model=blog.UserResponse)
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
    return userrepo.create_user(request, hashed_password, db)


@userroute.get("/{id}", status_code=status.HTTP_200_OK, response_model=blog.UserResponse)
def get_user(id: int, db: Session = Depends(database.get_db)):
    
    """
    This function is used to GET a user 
    
    Parameters
    ----------
    id: int
        The id of the blog
    db : str
        The db instance
    """
    
    return userrepo.get_user(id, db)
