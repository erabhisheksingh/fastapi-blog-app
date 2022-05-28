from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from models import blog
from databases import database
from schemas import schema

blogroute = APIRouter()

@blogroute.get("/blogs/all", status_code=status.HTTP_200_OK, response_model=List[blog.BlogResponse], tags=['Blogs'])
def get_all_blogs(db: Session = Depends(database.get_db)):
    
    """
    This function is used to get all the blogs from the DB 
    
    Parameters
    ----------
    db : str
        The db instance
    """
    
    return db.query(schema.BlogModel).all()

@blogroute.post("/blogs", status_code=status.HTTP_201_CREATED, response_model=blog.BlogResponse, tags=['Blogs'])
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
    
    new_blog = schema.BlogModel(title = request.title, body = request.body, author = request.author, published = request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@blogroute.get("/blogs/{id}", status_code=status.HTTP_200_OK, response_model=blog.BlogResponse, tags=['Blogs'])
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
    
    blog = db.query(schema.BlogModel).filter(schema.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with the Id {id} is not found")
    return blog

@blogroute.put("/blogs/{id}", status_code=status.HTTP_201_CREATED, response_model=blog.BlogResponse, tags=['Blogs'])
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
    
    blog_in_db = db.query(schema.BlogModel).filter(schema.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with the Id {id} is not found")
    
    blog_in_db.title = request.title
    blog_in_db.body = request.body
    blog_in_db.author = request.author 
    blog_in_db.published = request.published 
    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db

@blogroute.delete("/blogs/{id}", status_code=status.HTTP_200_OK, response_model=blog.BlogResponse, tags=['Blogs'])
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
    
    blog = db.query(schema.BlogModel).filter(schema.BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with the Id {id} is not found")
    
    db.delete(blog)
    db.commit()
    return blog