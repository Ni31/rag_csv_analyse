from fastapi import FastAPI
from routes import delete, list_files, query, upload

app = FastAPI()

app.include_router(upload.router)
app.include_router(list_files.router)
app.include_router(query.router)
app.include_router(delete.router)
