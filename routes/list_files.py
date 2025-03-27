from fastapi import APIRouter
from services.file_service import get_all_files

router = APIRouter()

@router.get("/files")
async def list_files():
    return {"files": get_all_files()}