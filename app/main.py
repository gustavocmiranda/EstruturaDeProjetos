from pipeline.extract import extract_data_from_excel
from pipeline.transform import concat_dataframes
from pipeline.load import load_excel

if __name__ == "__main__":
    df_list = extract_data_from_excel('data/input')
    df = concat_dataframes(df_list)
    load_excel(df, 'data/output', 'arquivo_concatenado')