from passlib.context import CryptContext


class Hash():
    
    pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated="auto")
    
    @staticmethod
    def hash(password: str):
        
        """
        This function is used to GET the Hash for the password 
    
        Parameters
        ----------
        password: str
            The password to be hashed
        """
        
        return Hash.pwd_ctx.hash(password)
    
    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        
        """
        This function is used to verify the Hashed password of the user 
    
        Parameters
        ----------
        hashed_password: str
            The hashed password of the user
        plain_password: str
            The plain password of the user
        """
        
        return Hash.pwd_ctx.verify(plain_password, hashed_password)

    