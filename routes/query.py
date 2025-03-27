from fastapi import APIRouter, Query, HTTPException
from services.file_service import query_csv_file

router = APIRouter()

@router.post("/query")
async def query_csv(file_id: str = Query(...), query: str = Query(...)):
    response = query_csv_file(file_id, query)
    if response is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"response": response}