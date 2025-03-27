# RAG CSV Analyse

## Description
This project is designed for analyzing CSV files using FastAPI. It allows users to upload CSV files and process the data efficiently.

## Features
- Upload CSV files via FastAPI
- Process and analyze data
- Return results in JSON format

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ni31/rag_csv_analyse.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rag_csv_analyse
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Use `curl` to upload a file:
   ```bash
   curl -X POST "http://127.0.0.1:8000/upload" \
        -H "accept: application/json" \
        -H "Content-Type: multipart/form-data" \
        -F "file=@path/to/yourfile.csv"
   ```

## API Endpoints
- `POST /upload`: Uploads a CSV file for processing.

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn

## Contributing
Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.

