from time import sleep
from botcity.web import WebBot, Browser, By
from botcity.maestro import *

from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.driver_path = 'resources\chromedriver.exe'
    bot.browse("https://www.linkedin.com/login/pt")
    bot.driver.maximize_window()

    # Aguardar até que o campo de usuário esteja disponível
    while True:
        try:
            bot.find_element("username", By.ID).click()
            bot.paste(EMAIL)
            break
        except Exception as e:
            print("Campo de usuário não encontrado, tentando novamente...")
            sleep(1)

    # Aguardar até que o campo de senha esteja disponível
    while True:
        try:
            bot.find_element( "password", By.ID).click()
            bot.paste(SENHA)
            break
        except Exception as e:
            print("Campo de senha não encontrado, tentando novamente...")
            sleep(1)

    # Aguardar até que o botão de login esteja disponível
    while True:
        try:
            bot.find_element("#organic-div > form > div.login__form_action_container > button", By.CSS_SELECTOR).click()
            break
        except Exception as e:
            print("Botão de login não encontrado, tentando novamente...")
            sleep(1)

    # Aguardar até que a caixa de pesquisa esteja disponível
    while True:
        try:
            bot.find_element("#global-nav-typeahead > input", By.CSS_SELECTOR).click()
            bot.paste("desenvolvedor full stack")
            bot.enter()
            break
        except Exception as e:
            print("Caixa de pesquisa não encontrada, tentando novamente...")
            sleep(1)

    bot.wait(5000)  # Aguarda brevemente antes de fechar o navegador
    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
