from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "Uploaded successfully"}
