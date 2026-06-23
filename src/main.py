from fastapi import FastAPI
from routes import base
from routes import data

# Motor is an asynchronous MongoDB driver for Python.
# MongoDB itself is just the database.
# Your Python code needs a way to talk to MongoDB.
# While waiting for MongoDB, FastAPI can handle other requests.

from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import getSettings

app = FastAPI() # We call it app because FastAPI creates a complete web/backend application

# It includes:

# API routes (like /users, /login)
# logic (database, calculations)
# configuration
# server behavior


# API (part of the app)
# Inside that app, you define: 
# API endpoints — the ways other programs can talk to your app.



# In web development:

# “App” = full backend application
# “API” = how others interact with that application

app.on_event("startup")
async def startup_db_client():
    settings = getSettings()

    # To contant with mongo and the database 
    
                        # This creates a connection (client) to the MongoDB server.
                        # 1- Initlize the client using (AsyncIOMotorClient)
                        # 2- Give the client the mongodb URL to connect to it 
    app.mongo_connection = AsyncIOMotorClient(settings.MONGODB_URL)

    # A MongoDB server can contain multiple databases. Like: admin db, config db, mini-rag db
                    
    # 3- Now you have the connection to the mongo and now we want to acess the specific db
    # 4- This step means: From the MongoDB server connection, give me the database named my_rag_db
    app.db_client = app.mongo_connection[settings.MONGODB_DATABSE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close() # close the connectio when app shutdown


app.include_router(base.base_router)
app.include_router(data.data_router)

