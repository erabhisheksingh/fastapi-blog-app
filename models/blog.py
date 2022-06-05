from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):

    """
    This class is the Base class for the User request body
    
    ...

    Attributes
    ----------
    id : Optional[str]
        the id of each blog from the DB
    username : str
        the title of the blog
    password : str
        the body of the blog

    """
    
    id: Optional[int]
    username: str
    password: str
    
    
class UserResponse(BaseModel):
    
    """
    This class is the Base class for the User response body
    
    ...

    Attributes
    ----------
    id : Optional[str]
        the id of each blog from the DB
    username : str
        the title of the blog
    password : str
        the body of the blog
    """
    
    username: str

    class Config():
        orm_mode = True



class Blog(BaseModel):

    """
    This class is the Base class for the Blog request body
    
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
    
    id: Optional[int]
    title: str
    body: str
    author: str
    published: Optional[bool]
    user_id: Optional[int] = None
    creator: UserResponse
    
    

class BlogResponse(Blog):
    
    """
    This class is the Base class for the Blog response body
    
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
    
    class Config():
        orm_mode = True


class Login(BaseModel):

    """
    This class is the Base class for the Login request body
    
    ...

    Attributes
    ----------
    username : str
        the username of the user
    password : str
        the password of the user

    """
    
    username: str
    password: str
    
    class Config():
        orm_mode = True

class Token(BaseModel):
    
    """
    This class is the Base class for the JWT Token response body
    
    ...

    Attributes
    ----------
    access_token : str
        the jwt token of the user
    token_type : str
        the token type of the user

    """
    
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    
    """
    This class is the Base class for the JWT Token request body
    
    ...

    Attributes
    ----------
    username : Optional[str]
        the username of the user

    """
    
    username: Optional[str] = None