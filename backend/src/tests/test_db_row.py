from schemas.db_row import FilesLogRow
from pytest import fixture


@fixture
def files_log_row_dict():
    return {
        "id": 1,
        "status": "success",
        "operation": "upload",
        "timestamp": "2021-09-01T00:00:00",
        "message": "File uploaded successfully.",
    }


@fixture
def files_log_row(files_log_row_dict):
    return FilesLogRow(**files_log_row_dict)


def test_files_log_row(files_log_row: FilesLogRow):
    assert files_log_row.id == 1
    assert files_log_row.status == "success"
    assert files_log_row.operation == "upload"
    assert files_log_row.timestamp == "2021-09-01T00:00:00"
    assert files_log_row.message == "File uploaded successfully."
