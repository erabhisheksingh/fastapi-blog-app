from databases import database
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String

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
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("UserModel", back_populates="blogs")
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
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("UserModel", back_populates="blogs")


'''
class UserModel(database.Base):
    
    #This UserModel is for the MYSQL DB where we need to
    #specify the VARCHAR column length
    
    __tablename__ = "users"
    
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String(255))
    password=Column(String(255))
    
    blogs = relationship("BlogModel", back_populates="creator")
'''  

class UserModel(database.Base):
    
    """
    This UserModel is for the model for the DB where we don't need to specify the VARCHAR column length
    
    ...

    Attributes
    ----------
    id : Optional[str]
        the id of each blog from the DB
    username : str
        the username of the user
    password : str
        the password of the user

    """
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    
    blogs = relationship("BlogModel", back_populates="creator")

