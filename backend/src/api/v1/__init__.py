from fastapi import APIRouter

from .files import router as files_router
from .database import router as database_router

router = APIRouter()

router.include_router(files_router, prefix="/files", tags=["files"])
router.include_router(database_router, prefix="/database", tags=["database"])
