import pandas as pd
from typing import List


def concat_dataframes(dataframes_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função que transforma uma lista de DataFrames em um único DataFrame
    """

    return pd.concat(dataframes_list, ignore_index=True)