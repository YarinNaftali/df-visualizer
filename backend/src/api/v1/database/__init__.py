from fastapi import APIRouter, status
from database import FilesLogDB
from schemas.db_row import FilesLogRow
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get(
    "/records", status_code=status.HTTP_200_OK, response_model=list[FilesLogRow]
)
async def get_all_records(table_name: str = "files"):
    records = FilesLogDB.get_all_records(table_name)
    logger.fatal(f"Records: {records}")
    return {"records": records}
