import os
import glob # biblioteca para listar arquivos
import pandas as pd

from typing import List



PATH = 'data/input'

def extract_data_from_excel(path: str) -> List[pd.DataFrame]: # type: ignore
    """
    Função para ler os arquivos de uma pasta data/input 
    e retornar uma lista de DataFrames

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """

    
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    df_list = []
    for file in all_files:
        df_list.append(pd.read_excel(file))

    return df_list


if __name__ == "__main__":
    df_list = extract_data_from_excel(path=PATH)
    print(df_list)