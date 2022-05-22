from typing import Optional
from pydantic import BaseModel


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
