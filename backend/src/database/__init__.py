import sqlite3
from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from schemas.db_row import FilesLogRow
from settings import Settings


settings = Settings()


class Operation(str, Enum):
    UPLOAD = "UPLOAD"


class FilesLogDB(BaseModel):
    @staticmethod
    def __get_db_connection__():
        conn = sqlite3.connect(settings.database_url)
        if conn is None:
            raise Exception("Could not connect to the database")
        return conn

    @classmethod
    def __create_tables_if_missing__(cls, table_name: str, *args):
        conn = cls.__get_db_connection__()
        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                {', '.join(args)}
            )
            """
        )
        conn.commit()
        conn.close()

    @classmethod
    def __get_files_db__(cls):
        conn = cls.__get_db_connection__()
        cls.__create_tables_if_missing__(
            "files",  # table_name
            "timestamp TEXT",
            "operation TEXT",
            "status TEXT",
            "message TEXT",
        )
        return conn

    @classmethod
    def log_operation(
        cls,
        operation: str,
        status: str,
        message: str,
        table_name: str = "files",
    ):
        timestamp = datetime.now().isoformat()
        conn = cls.__get_files_db__()
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO {table_name} (timestamp, operation, status, message)
            VALUES ('{timestamp}', '{operation}', '{status}', '{message}')
            """
        )
        conn.commit()
        conn.close()

    @classmethod
    def get_all_records(cls, table_name: str) -> list[FilesLogRow]:
        conn = cls.__get_files_db__()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        records: list[FilesLogRow] = cursor.fetchall()
        conn.close()
        return records
