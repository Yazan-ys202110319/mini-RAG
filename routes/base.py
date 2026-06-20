from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix='/api/v1',
    tags=["api_v1"]
)


# This is called Decorator, its a way to modify a function or a class without changing the actual code.
# So here it will tells FastAPI to register this function as an API route.
@base_router.get("/") 
async def welcome(): 
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "app name": app_name,
        "app version": app_version
    }