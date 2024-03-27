import sqlite3
from settings import Settings

settings = Settings()


def get_db_connection():
    conn = sqlite3.connect(settings.database_url)
    return conn


def create_tables(table_name: str, *args):
    conn = get_db_connection()
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


def log_operation(operation: str, table_name: str, *args):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO {table_name} ({', '.join(args)})
        VALUES {operation}
        """
    )
    conn.commit()
    conn.close()
