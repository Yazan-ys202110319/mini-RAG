from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os


class ProjectController(BaseController):
    

    def __init__(self):
        super().__init__()


    # will take the project id and give you the path where it should be saved 
    def get_project_path(self, project_id: str):
        
        project_dir = os.path.join(
            self.file_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir) # create it if not exist

        
        return project_dir