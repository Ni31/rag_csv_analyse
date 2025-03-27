from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database import files_collection

router = APIRouter()

@router.get("/files")
async def list_files():
    files = list(files_collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1}))
    return JSONResponse(content={"files": files})

@router.delete("/file/{file_id}")
async def delete_file(file_id: str):
    result = files_collection.delete_one({"file_id": file_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="File not found")
    return JSONResponse(content={"message": "File deleted successfully"})
