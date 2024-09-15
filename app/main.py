"""Chamada das funções e execução do pipeline."""
from pipeline.extract import extract_data_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframes

if __name__ == "__main__":
    df_list = extract_data_from_excel("data/input")
    df = concat_dataframes(df_list)
    load_excel(df, "data/output", "arquivo_concatenado")
