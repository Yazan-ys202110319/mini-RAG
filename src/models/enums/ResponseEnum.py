from enum import Enum

class ResponseSignal(Enum):

    FILE_VAILDATED_SUCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_type_exceeded"
    FILE_UPLOAD_SUCCESS = "file_uploaded_success"    
    FILE_UPLOAD_FAIL = "file_upload_failed"
