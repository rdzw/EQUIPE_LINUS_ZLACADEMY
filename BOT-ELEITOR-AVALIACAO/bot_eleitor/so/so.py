import os

diretorio = r'C:\Users\noturno\Downloads\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf'

def listar_arquivos(diretorio):
    """Lista todos os arquivos em um diretório."""
    try:
        return os.listdir(diretorio)
    except FileNotFoundError:
        print("Diretório não encontrado.")
        return []

def criar_diretorio(diretorio):
    """Cria um novo diretório se ele não existir."""
    try:
        os.mkdir(diretorio)
        print(f'Diretório "{diretorio}" criado com sucesso.')
    except FileExistsError:
        print(f'Diretório "{diretorio}" já existe.')

def renomear_arquivo(diretorio, arquivo_antigo, novo_nome):
    """Renomeia um arquivo ou diretório."""
    try:
        os.rename(os.path.join(diretorio, arquivo_antigo), os.path.join(diretorio, novo_nome))
        print(f'Arquivo "{arquivo_antigo}" renomeado para "{novo_nome}".')
    except FileNotFoundError:
        print(f'Arquivo "{arquivo_antigo}" não encontrado.')

def apagar_arquivos(diretorio, lista_arquivos):
    """Apaga arquivos especificados em uma lista de um determinado diretório."""
    for arquivo in lista_arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.exists(caminho_completo) and input(f'Tem certeza que deseja apagar {arquivo}? (s/n): ').lower() == 's':
            os.remove(caminho_completo)
            print(f'Arquivo {arquivo} apagado com sucesso.')
        else:
            print(f'Arquivo {arquivo} não encontrado ou não foi apagado.')

# Execução
print("Arquivos disponíveis:", listar_arquivos(diretorio))
criar_diretorio(os.path.join(diretorio, 'novo_diretorio'))

# Renomear o primeiro arquivo se existir
arquivos_existentes = listar_arquivos(diretorio)
if arquivos_existentes:
    renomear_arquivo(diretorio, arquivos_existentes[0], 'arquivo_renomeado.txt')

# Exemplo de arquivos a serem apagados
apagar_arquivos(diretorio, ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt'])
