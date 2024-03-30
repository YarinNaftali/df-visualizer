from pydantic import BaseModel


class FilesLogRow(BaseModel):
    id: int
    timestamp: str
    operation: str
    status: str
    message: str

    class Config:
        orm_mode = True
