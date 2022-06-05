from datetime import datetime, timedelta
from typing import Optional

from jose import JWSError, jwt

SECRET_KEY = "JWTSecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    
    """
    This function is used to verify the Hashed password of the user 
    
    Parameters
    ----------
    data: dict
        The data payload of the JWT Token
    expires_delta: Optional[timedelta]
        The expire time of the token
    """
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt
