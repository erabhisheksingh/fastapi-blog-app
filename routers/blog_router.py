from typing import List

from databases import database
from fastapi import APIRouter, Depends, Response, status
from models import blog
from repository import blog_repository as blogrepo
from sqlalchemy.orm import Session

blogroute = APIRouter(
    prefix = "/blogs",
    tags = ['Blogs']
)

@blogroute.get("/all", status_code=status.HTTP_200_OK, response_model=List[blog.BlogResponse])
def get_all_blogs(db: Session = Depends(database.get_db)):
    
    """
    This function is used to get all the blogs from the DB 
    
    Parameters
    ----------
    db : str
        The db instance
    """
    
    return blogrepo.get_all(db)

@blogroute.post("/", status_code=status.HTTP_201_CREATED, response_model=blog.BlogResponse)
def post_blog(request: blog.Blog, db: Session = Depends(database.get_db)):
    
    """
    This function is used to POST a blog 
    
    Parameters
    ----------
    request : blog.Blog
        The request body of the type Blog
    db : str
        The db instance
    """
    
    return blogrepo.post_blog(request, db)

@blogroute.get("/{id}", status_code=status.HTTP_200_OK, response_model=blog.BlogResponse)
def get_blog(id: int, response: Response, db: Session = Depends(database.get_db)):
    
    """
    This function is used to POST a blog 
    
    Parameters
    ----------
    id: int
        The id of the blog
    request : blog.Blog
        The request body of the type Blog
    db : str
        The db instance
    """
    
    return blogrepo.get_blog(id, db)

@blogroute.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=blog.BlogResponse)
def update_blog(id: int, request: blog.Blog, db: Session = Depends(database.get_db)):
    
    """
    This function is used to UPDATE an existing blog 
    
    Parameters
    ----------
    id: int
        The id of the blog
    request : blog.Blog
        The request body of the type Blog
    db : str
        The db instance
    """ 
    
    return blogrepo.update_blog(id, request, db)

@blogroute.delete("/{id}", status_code=status.HTTP_200_OK, response_model=blog.BlogResponse)
def delete(id: int, db: Session = Depends(database.get_db)):
    
    """
    This function is used to DELETE an existing blog 
    
    Parameters
    ----------
    id: int
        The id of the blog
    db : str
        The db instance
    """
    
    return blogrepo.delete_blog(id, db)
