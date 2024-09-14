import pandas as pd
from typing import List

"""
Função que transforma uma lista de DataFrames em um único DataFrame
"""

def concat_dataframes(dataframes_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dataframes_list, ignore_index=True)