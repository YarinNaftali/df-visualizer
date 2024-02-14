from fastapi import APIRouter, UploadFile, status

router = APIRouter()


@router.post("/upload-csv", status_code=status.HTTP_201_CREATED)
async def upload_csv(file: UploadFile):
    return {
        "filename": file.filename,
        "size": file.size,
        "content_type": file.content_type,
    }
