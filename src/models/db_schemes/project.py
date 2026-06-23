from pydantic import BaseModel, Filed, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId]
    project_id: str = Filed(..., min_length = 1) # if user put the id to be less than 1 will get error

    # custom validation on the schema
    @validator('project_id') # will do validation on project id
    def validate_project_id(cls, value): 
        if not value.isalnum():
            raise ValueError('Project id must be alphanumeric')
        return value

    # This class to avoid errors from objectId
    class Config:
        arbitary_types_allowed = True
