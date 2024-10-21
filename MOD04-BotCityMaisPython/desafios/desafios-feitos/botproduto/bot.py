"""
Projeto robo produto
Funções do robo:
1 - Acessar o site: https://flordejambu.com/shop/ 
2 - No site, localizar o campo pesquisa e fazer uma pesquisa do produto: Acai
3 - Após a pesquisa, imprimir a tema de resultado do site:
    3.1 - Local e nome do arquivo pdf: C:\\LG\\Desafio\\botproduto\\pdf\\SiteProduto.pdf' 
4 - Obter o valor do dolar atualizado (acesso a API na Web)
5 - Realiza a leitura do arquivo Excel com a lista de Produto
    5.1 - C:\\LG\\Desafio\\botproduto\\planilha\\RelacaoProduto.xlsx 
6 - Inserir na tabela produto do banco de dados, os produtos carregados a partir da Planilha, 
    com o campo valor dolar atualizado. (utilizar a api_database)
7 - Gerar o arquivo PDF, conforme layout, com a lista dos Produtos inseridos no banco de dados: ListaProduto.pdf
    7.1 - C:\\LG\\Desafio\\botproduto\\pdf\\ListaProduto.pdf'
8 - Fazer o merge entre os arquivos: ListaProduto.pdf + SiteProduto.pdf. O nome do arquivo de saída: Produtos.pdf 
9 - Acessar, no banco de dados, a lista de usuários.(utilizar a api_database)
10 - Enviar para cada usuário, da lista de usuário, um E-mail com o arquvo Produtos.pdf em anexo  
"""

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
import requests
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
#configuracao chromer
from webdriver_manager.chrome import ChromeDriverManager
#configurar http, antes tem executar terminal: pip install botcity-http-plugin
from botcity.plugins.http import BotHttpPlugin
from datetime import datetime

import planilha.planilha as planilha
import e_mail.e_mail as e_mail
import pdf.pdf as pdf

# Definir as funções

def acessar_site(bot):
    # Acessar site
    bot.browse("https://flordejambu.com/shop/")
    while len(bot.find_elements('/html/body/div[1]/header/div/div[1]/div/div/div[1]/div/a/img', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')
    bot.wait(1000)
    # Perquisar pelo produto
    produto = 'Açai'
    bot.find_element('/html/body/div[1]/header/div/div[1]/div/div/div[2]/div/form/input[1]', By.XPATH).send_keys(produto)
    bot.wait(1000)
    bot.enter()
    # Imprimir página do site para arquivo PDF
    bot.print_pdf('C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\SiteProduto.pdf')

def api_obter_valor_dolar():
    http=BotHttpPlugin('https://economia.awesomeapi.com.br/last/USD-BRL')
    return http.get_as_json()

def api_lista_produtos():
    http=BotHttpPlugin('http://127.0.0.1:5000/produto')
    return http.get_as_json()

def api_lista_usuarios():
    http=BotHttpPlugin('http://127.0.0.1:5000/usuario')
    return http.get_as_json()

def inserir_produto(produto, valor_dolar):
    valor_atualizado = float(valor_dolar) * float(produto['PRECO_REAL'])
    url = 'http://127.0.0.1:5000/produto'
    headers = {'Content-Type': 'application/json'}
    dados = {
        "descricao" : produto['DESCRICAO'],
        "unidade"   : produto['UNIDADE'],
        "quantidade" : produto['QUANTIDADE'],
        "preco_real" : produto['PRECO_REAL'],
        "preco_dolar": valor_atualizado
    }

    try:
        resposta = requests.post(url=url,headers=headers, json=dados)
        resposta.raise_for_status()  # Verifica se houve algum erro na requisição
        # Retorna a resposta em formato JSON
        retorno = resposta.json()
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
    except Exception as e:
        print(f"Erro: {e}")

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    # Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    #bot.maximize_window()
    acessar_site(bot)
    
    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()
   
    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )
    
    # Implement here your logic...
       
    print('Inicio do processamento...')
    print('Acesso API Cotacao Dolar...')
    retornoJSON = api_obter_valor_dolar()
    valor_dolar=retornoJSON['USDBRL']['high']
    print('Leitura do arquivo Excel...')
    arq_excel = 'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\planilha\\RelacaoProduto.xlsx'
    sheet = 'produto'  
    df = planilha.ler_excel(arq_excel,sheet)
    planilha.exibir_dados_excel(df)
    print('Inserindo produtos no banco de dados...')
    for index, produto in df.iterrows():
        inserir_produto(produto,valor_dolar)
        
    print('Gerando arquivo PDF com a lista de produtos...')
    retornoJSON_produtos = api_lista_produtos()
    lista_produto = retornoJSON_produtos['dados']
    pdf.criar_pdf_lista_produto(lista_produto)
    
    print('Gerando arquivo Produtos.pdf com o merge entre os arquivos: ListaProduto.pdf + SiteProduto.pdf...')
    lista_pdf = []
    lista_pdf.append('C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\ListaProduto.pdf')
    lista_pdf.append('C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\SiteProduto.pdf')
    pdf.merge_pdfs(lista_pdf,'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\Produtos.pdf')
    
    print('Enviando E-mail para a lista de usuario com arquivo Produtos.pdf em anexo.')
    arq_anexo = 'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\Produtos.pdf'
    retornoJSON_usuarios = api_lista_usuarios()
    lista_produto = retornoJSON_usuarios['dados']
    for usuario in lista_produto:
        destinatario = usuario['email']
        print(f'Enviando e-mail para: {destinatario}')
        assunto = "Lista de Produtos"
        conteudo = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de produtos."
        e_mail.enviar_email_anexo(destinatario, assunto, conteudo,arq_anexo)    
    
    print('Fim do processamento...')
     

    


def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()