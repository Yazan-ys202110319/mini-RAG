from pydantic import BaseModel
from typing import Optional

# Any request that will go to the new endpoin will should look like this, otherwise pydantic 
# will do the data validation and fix it
class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: Optional[int] = 0


