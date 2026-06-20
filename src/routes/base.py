from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import getSettings, Settings

base_router = APIRouter(
    prefix='/api/v1',
    tags=["api_v1"] # In the FastAPI Swagger, it will help to organize the routes, so the ("/") will be 
    # under the api_v1 tag
)


# This is called Decorator, its a way to modify a function or a class without changing the actual code.
# So here it will tells FastAPI to register this function as an API route.
@base_router.get("/") 
async def welcome(app_settings: Settings = Depends(getSettings)): 

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app name": app_name,
        "app version": app_version
    }