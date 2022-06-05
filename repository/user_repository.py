from fastapi import HTTPException, status
from models import blog
from schemas import schema
from sqlalchemy.orm import Session

def create_user(request: blog.User, hashed_password: str, db: Session):
    
    """
    This function is used to POST a user 
    
    Parameters
    ----------
    request : blog.User
        The request body of the type User
    hashed_password: str
        The hashed password of the user
    db : str
        The db instance
    """ 
    
    new_user = schema.UserModel(username = request.username, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def get_user(id: int, db: Session):
    
    """
    This function is used to POST a user 
    
    Parameters
    ----------
    id : int
        The id of the user
    db : str
        The db instance
    """ 
    
    user = db.query(schema.UserModel).filter(schema.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with the Id {id} is not found")
    return user