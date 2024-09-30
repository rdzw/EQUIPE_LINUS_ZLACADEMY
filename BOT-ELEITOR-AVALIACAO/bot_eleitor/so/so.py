import glob
import os

def apagar_arquivos(caminho_diretorio, padrao):
    # Cria o caminho completo com o padrão
    caminho_completo = os.path.join(caminho_diretorio, padrao)
    # Encontra todos os arquivos que correspondem ao padrão
    arquivos = glob.glob(caminho_completo)
    # Apaga cada arquivo encontrado
    for arquivo in arquivos:
    os.remove(arquivo)

    