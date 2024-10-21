import pandas as pd
from openpyxl import load_workbook
from IPython.display import display


# Retorna um Data Frame com os dados da leitura do arquivo Excel
def ler_excel(caminho_arquivo, nome_planilha):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo, sheet_name=nome_planilha)
    return df


def exibir_dados_excel(df):
    display(df)
