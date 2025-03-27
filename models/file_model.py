from pydantic import BaseModel

class FileSchema(BaseModel):
    file_id: str
    file_name: str
    document: dict