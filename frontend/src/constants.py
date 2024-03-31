API_URL = "http://backend:8000"
API_VERSION = "api/v1"

FILES_ROUTE = "files"
UPLOAD_CSV_ENDPOINT = f"{API_URL}/{API_VERSION}/{FILES_ROUTE}/upload-csv"
GET_ALL_UPLOADED_FILES_ENDPOINT = f"{API_URL}/{API_VERSION}/{FILES_ROUTE}/all-files"

DATABASE_ROUTE = "database"
GET_ALL_RECORDS_ENDPOINT = f"{API_URL}/{API_VERSION}/{DATABASE_ROUTE}/records"
