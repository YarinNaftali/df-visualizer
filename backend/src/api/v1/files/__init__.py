from fastapi import APIRouter, UploadFile, status
from database import FilesLogDB, Operation

from uuid import uuid4

router = APIRouter()


@router.post("/upload-csv", status_code=status.HTTP_201_CREATED)
async def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
        FilesLogDB.log_operation(
            Operation.UPLOAD,
            status="FAILED",
            message=f"File content type is not CSV. Got {file.content_type}",
        )
        return {"error": "Only CSV files are allowed"}
    if not file.filename.endswith(".csv"):
        FilesLogDB.log_operation(
            Operation.UPLOAD,
            status="FAILED",
            message=f"File extension is not CSV. Got {file.filename}",
        )
        return {"error": "Only CSV files are allowed"}

    # Save the file to the uploads directory
    with open(
        f"uploads/{uuid4()}.csv",
        "wb",
    ) as buffer:
        buffer.write(await file.read())

    FilesLogDB.log_operation(Operation.UPLOAD, status="SUCCESS")

    return {"message": "File uploaded successfully"}
