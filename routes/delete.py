from fastapi import APIRouter, HTTPException
from services.file_service import delete_csv_file

router = APIRouter()

@router.delete("/file/{file_id}")
async def delete_file(file_id: str):
    result = delete_csv_file(file_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}