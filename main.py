from fastapi import FastAPI
from databases import database
from routers import blog_router, user_router
from schemas import schema

app = FastAPI()

app.include_router(blog_router.blogroute)
app.include_router(user_router.userroute)

"""This configuration is needed to create the Tables in the DB at runtime"""
schema.BlogModel.metadata.create_all(database.engine)
