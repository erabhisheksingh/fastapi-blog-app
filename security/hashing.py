from passlib.context import CryptContext

class Hash():
    
    pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated="auto")
    
    def hash(password: str):
        return Hash.pwd_ctx.hash(password)