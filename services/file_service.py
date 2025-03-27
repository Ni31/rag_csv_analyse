import pandas as pd
import uuid
from services.database import files_collection

def save_csv_to_db(file):
    file_id = str(uuid.uuid4())
    df = pd.read_csv(file.file)
    files_collection.insert_one({
        "file_id": file_id,
        "file_name": file.filename,
        "document": df.to_dict()
    })
    return file_id

def get_all_files():
    return list(files_collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1}))

def query_csv_file(file_id, query):
    file_data = files_collection.find_one({"file_id": file_id}, {"_id": 0, "document": 1})
    if not file_data:
        return None
    df = pd.DataFrame(file_data["document"])
    return df[query].to_json() if query in df.columns else "Column not found in CSV"

def delete_csv_file(file_id):
    return files_collection.delete_one({"file_id": file_id})