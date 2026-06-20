from fastapi import FastAPI
from routes import base
from routes import data



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


app.include_router(base.base_router)
app.include_router(data.data_router)