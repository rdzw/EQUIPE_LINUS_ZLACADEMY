from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin

import requests

import e_mail.e_mail as e_mail
import planilha.planilha as planilha

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def api_lista_usuarios():
    http=BotHttpPlugin('http://127.0.0.1:5000/usuario')
    return http.get_as_json()

def acessar_site(bot):
    bot.browse('https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor?id=1727788956071')
    bot.maximize_window()
    
    #cookie
    while len(bot.find_elements('//*[@id="modal-lgpd"]/div/div/div[2]/button', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')
    bot.find_element('//*[@id="modal-lgpd"]/div/div/div[2]/button', By.XPATH).click()

    #procurar opção 10 
    while len(bot.find_elements('//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')

    excel_path = 'planilha\RelacaoEleitor.xlsx' 
    sheet = 'CPF'  
    df = planilha.ler_excel(excel_path, sheet) 

    for index, row in df.iterrows():
        cpf = str(row['CPF'])
        if len(cpf) < 11:
            cpf = cpf.zfill(11)  # Preenche com zero à esquerda até 11 dígitos

        # Verifica se o CPF ainda não está com 11 dígitos após a correção
        if len(cpf) != 11:
            print(f"O CPF {cpf} ainda não tem 11 dígitos após correção. CPF inválido.")
            continue  # Pula para o próximo CPF, se necessário

        data_nascimento = row['DATA_NASCIMENTO']
        nome = row['NOME']
        nome_mae = row['NOME_MAE']
        cep = row['CEP']
        nro_endereco = row['NRO_ENDERECO']

        data_convertida = data_nascimento.strftime('%d/%m/%Y')

        bot.wait(1000)
        bot.find_element('//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button', By.XPATH).click()

        bot.wait(1000)

        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/input', By.XPATH).click()
        bot.paste(cpf)
        bot.wait(1000)

        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input', By.XPATH).click()
        bot.paste(str(data_convertida))
        bot.wait(1000)

        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[3]/div/input', By.XPATH).click()
        bot.paste(nome_mae)
        bot.wait(1000)

        bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]', By.XPATH).click()
        bot.wait(1000)

        numero_titulo = bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[1]/b', By.XPATH).text
        situacao = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[2]/span', By.XPATH).text
        secao = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[1]/span[2]', By.XPATH).text
        zona = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[3]/span[2]', By.XPATH).text
        local = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[1]/span[2]', By.XPATH).text
        endereco = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[2]/span[2]', By.XPATH).text
        bairro = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[4]/span[2]', By.XPATH).text
        municipio = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[3]/span[2]', By.XPATH).text
        pais = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[2]/span[2]', By.XPATH).text

        print(f"Número do Título: {numero_titulo}")
        print(f"Situação: {situacao}")
        print(f"Seção: {secao}")
        print(f"Zona: {zona}")
        print(f"Local: {local}")
        print(f"Endereço: {endereco}")
        print(f"Bairro: {bairro}")
        print(f"Município: {municipio}")
        print(f"País: {pais}")

        bot.wait(1000)
        bot.print_pdf(f'pdf\{cpf}_titulo.pdf')
        bot.wait(1000)

        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-consultar-numero-titulo-eleitor/app-avatar-e-nome/div/div/button', By.XPATH).click()
        bot.wait(1000)
        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-mensagem/div/div/div/div[2]/button', By.XPATH).click()
        bot.wait(1000)
        bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-home/div/div[4]/app-botao-principal[1]/button', By.XPATH).click()


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    acessar_site(bot)

    bot.wait(3000)

    bot.stop_browser()
    
    

    '''print('Enviando E-mail para a lista de usuario com arquivo Produtos.pdf em anexo.')
    arq_anexo = 'pdf\\banner.png'
    retornoJSON_usuarios = api_lista_usuarios()
    lista_produto = retornoJSON_usuarios['dados']
    for usuario in lista_produto:
        destinatario = usuario['email']
        print(f'Enviando e-mail para: {destinatario}')
        assunto = "Lista de Produtos"
        conteudo = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de produtos."
        e_mail.enviar_email(destinatario, assunto, conteudo,arq_anexo) 
    
    print('Fim do processamento...')'''

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
