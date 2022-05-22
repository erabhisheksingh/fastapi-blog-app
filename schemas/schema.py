from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from databases import database

'''
class BlogModel(database.Base):
    
    #This BlogModel is for the MYSQL DB where we need to
    #specify the VARCHAR column length
    
    __tablename__ = "blogs"
    
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(255))
    body=Column(String(255))
    author=Column(String(255))
    published=Column(Boolean)
'''
 
 
class BlogModel(database.Base):
    
    """
    This BlogModel is for the model for the DB where we don't need to specify the VARCHAR column length
    
    ...

    Attributes
    ----------
    id : Optional[str]
        the id of each blog from the DB
    title : str
        the title of the blog
    body : str
        the body of the blog
    author : str
        the author of the blog
    published : Optional[bool]
        the published or not flag

    """
    
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    author = Column(String)
    published = Column(Boolean)
    
