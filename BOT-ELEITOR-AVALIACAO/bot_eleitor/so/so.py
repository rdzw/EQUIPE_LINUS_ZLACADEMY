import os
import glob

def apagar_arquivos_pdf(diretorio):
    # Define o padrão de arquivos a serem excluídos
    padroes = ['*_eleitor.pdf', '*_titulo.pdf']

    # Itera sobre os padrões de busca e exclui os arquivos correspondentes
    for padrao in padroes:
        arquivos = glob.glob(os.path.join(diretorio, padrao))
        for arquivo in arquivos:
            try:
                os.remove(arquivo)
                print(f"Arquivo {arquivo} excluído com sucesso.")
            except Exception as e:
                print(f"Erro ao excluir o arquivo {arquivo}: {e}")