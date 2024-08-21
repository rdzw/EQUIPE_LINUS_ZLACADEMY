from botcity.web import WebBot, By
from botcity.maestro import *
from dotenv import load_dotenv
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

import os
import pandas as pd

# Carrega as variáveis de ambiente
load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def atualizar_planilha(nome, file_path='Dados-leads.xlsx'):
    # Ler o arquivo Excel
    df = pd.read_excel(file_path, engine='openpyxl')
    
    # Adicionar o nome extraído à próxima linha disponível no DataFrame
    nova_linha = len(df)
    df.at[nova_linha, 'NOME'] = nome
    
    # Salvar as alterações na planilha Excel
    df.to_excel(file_path, index=False, engine='openpyxl', na_rep='')

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Configurar e iniciar o navegador
    bot = WebBot()
    bot.headless = False
    bot.driver_path = ChromeDriverManager().install()
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

    #Adicionar filtro Pessoas
    while True:
        try:
            bot.find_element("//button[contains(., 'Pessoas')]", By.XPATH).click()
            break
        except Exception as e:
            print("Filtro não encontrado, tentando novamente...")
            sleep(1)
    
    link_perfil = '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]'
    max_result = 2
    sleep(2)


    for i in range(1, max_result+1):
        try:
            sleep(2)
            #nome
            bot.find_element(link_perfil.format(i), By.XPATH).click()
            nome = bot.find_element('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1', By.XPATH).get_attribute('innerHTML')
           
            atualizar_planilha(nome)

            sleep(5)
            bot.back()
        except Exception as e:
            print(f"Erro ao clicar no resultado {i}: {e}")

    bot.wait(5000)
    bot.stop_browser()

if __name__ == '__main__':
    main()
