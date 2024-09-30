from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin
import requests

import e_mail.e_mail as e_mail

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def api_lista_usuarios():
    http=BotHttpPlugin('http://127.0.0.1:5000/usuario')
    return http.get_as_json()

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    '''bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.maximize_window()
    bot.browse("https://www.botcity.dev")
    bot.wait(3000)
    bot.stop_browser()'''

    print('Enviando E-mail para a lista de usuario com arquivo Produtos.pdf em anexo.')
    arq_anexo = 'pdf\\banner.png'
    retornoJSON_usuarios = api_lista_usuarios()
    lista_produto = retornoJSON_usuarios['dados']
    for usuario in lista_produto:
        destinatario = usuario['email']
        print(f'Enviando e-mail para: {destinatario}')
        assunto = "Lista de Produtos"
        conteudo = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de produtos."
        e_mail.enviar_email(destinatario, assunto, conteudo,arq_anexo)    
    
    print('Fim do processamento...')

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
