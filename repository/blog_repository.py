from fastapi import HTTPException, status
from models import blog
from schemas import schema
from sqlalchemy.orm import Session


def get_all(db: Session):
    
    """
    This function is used to GET all the existing blogs 
    
    Parameters
    ----------
    db : str
        The db instance
    """ 
    
    return db.query(schema.BlogModel).all()

def post_blog(request: blog.Blog, db: Session):
    
    """
    This function is used to POST an existing blog
    
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

def get_blog(id: int, db: Session):
    
    """
    This function is used to GET an existing blogs
    
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
    return blog

def update_blog(id: int, request: blog.Blog, db: Session):
    
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
    
def delete_blog(id: int, db: Session):
    
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
