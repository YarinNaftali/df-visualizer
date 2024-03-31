import pandas as pd
from pandas import DataFrame


def get_dataframe_from_csv(csv_file) -> DataFrame:
    df = pd.read_csv(csv_file)
    return df
