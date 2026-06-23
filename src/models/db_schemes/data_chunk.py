from pydantic import BaseModel, Filed, validator
from typing import Optional
from bson.objectid import ObjectId


class DataChunk(BaseModel):

    _id: Optional[ObjectId]
    chunk_text: str = Filed(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Filed(..., gt = 0) # grater than 0
    chunk_project_id: ObjectId # To link with the project schema


    # This class to avoid errors from objectId
    class Config:
        arbitary_types_allowed = True