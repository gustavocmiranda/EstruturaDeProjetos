"""Móodulo que faz a transformação dos dados na pipeline."""
from typing import List

import pandas as pd


def concat_dataframes(dataframes_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função que transforma uma lista de DataFrames em um único DataFrame.

    args:
    dataframes_list(List[pd.DataFrame])

    return: DataFrame
    """
    return pd.concat(dataframes_list, ignore_index=True)
