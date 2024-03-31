from fastapi import APIRouter, UploadFile, status
from database import FilesLogDB, Operation
import os

from uuid import uuid4

router = APIRouter()


@router.get("/all-files", status_code=status.HTTP_200_OK, response_model=list[str])
async def get_all_files():
    files = os.listdir("uploads")
    return files


@router.post("/upload-csv", status_code=status.HTTP_201_CREATED)
async def upload_csv(file: UploadFile):
    try:
        # Save the file to the uploads directory
        # we can replace this routine with a call to S3 or any other storage service
        file_name = f"{uuid4()}.csv"
        with open(
            f"uploads/{file_name}",
            "wb",
        ) as buffer:
            buffer.write(await file.read())

        FilesLogDB.log_operation(
            Operation.UPLOAD,
            status="SUCCESS",
            message=f"File {file_name} uploaded successfully",
        )

        return {"message": "File uploaded successfully"}

    except Exception as e:
        FilesLogDB.log_operation(Operation.UPLOAD, status="FAILED", message=str(e))
        return {"message": "File upload failed"}
