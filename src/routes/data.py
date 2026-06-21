# To upload files to the app

from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import getSettings, Settings
from controllers import DataController
from controllers import ProjectController
import aiofiles
from models import ResponseSignal 
import logging
from .schemes.data import ProcessRequest
from controllers import ProcessController

# For the logs
logger = logging.getLogger('uvicorn.error')


data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1", "data"]
)

# This endpoint or route will recive a file and then upload the file in the system of the app
@data_router.post("/upload/{project_id}") # This project id you will get it from the user
# Then we will use the project id in the function upload data
async def upload_data(project_id: str, file: UploadFile,
                app_settings: Settings = Depends(getSettings)): 
    # to recive a file in FastAPI you must use
    # the UploadFile class, so the function will also recive a file of type UploadFile

    
    # Will create an object from class DataController of type DataController and then use 
    # validate_uploaded_file function and pass to it the file
    is_valid, results_signal = DataController().validate_uploaded_file(file = file)

    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST, # you can use only 400
            content = {
                "signal": results_signal
            }
        )
    

    project_dir_path = ProjectController().get_project_path(project_id = project_id)
    file_path, file_id = DataController().generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        # This will take chunk by chunk 
        async with aiofiles.open(file_path, "wb") as f: # wb because uploaded files are binary data
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                # := 
                # It means:
                # Read a chunk.
                # Store it in chunk.
                # Check whether it is empty.

                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse (
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                'signal': ResponseSignal.FILE_UPLOAD_FAIL.value
            }
        )


    return JSONResponse(
        content = {
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            'file_id': file_id
        }
    )


@data_router.post("/process/{project_id}")
async def process_endpoint(project_id: str, process_request: ProcessRequest):

    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size

    process_controller = ProcessController(project_id=project_id)

    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )

    if chunk_size is None or len(file_chunks) == 0:

        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.PROCESSING_FAILED.value
            }
        )

    return file_chunks

