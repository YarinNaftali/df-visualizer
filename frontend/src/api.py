import httpx

from pandas import DataFrame
from constants import UPLOAD_CSV_ENDPOINT, GET_ALL_RECORDS_ENDPOINT


def upload_dataframe(df: DataFrame):
    url = UPLOAD_CSV_ENDPOINT
    response = httpx.post(url, files={"file": df.to_csv()})
    if response.status_code == 201:
        return True
    else:
        return False


def get_all_records():
    url = GET_ALL_RECORDS_ENDPOINT
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json()["records"]
    else:
        return []
