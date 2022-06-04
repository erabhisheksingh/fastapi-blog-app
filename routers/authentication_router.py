from databases import database
from fastapi import APIRouter, Depends
from models import blog
from sqlalchemy.orm import Session

login = APIRouter(
    tags = ["Login"]
)

@login.post("/login")
def user_login(request: blog.Login, db: Session = Depends(database.get_db)):
    
    pass
