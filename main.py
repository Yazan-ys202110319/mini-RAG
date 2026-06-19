from fastapi import FastAPI

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


# This is called Decorator, its a way to modify a function or a class without changing the actual code.
# So here it will tells FastAPI to register this function as an API route.
@app.get("/welcome") 
def welcome(): 
    return {
        "message": "Hello World!"
    }