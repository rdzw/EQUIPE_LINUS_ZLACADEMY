from botcity.web import WebBot, By
from botcity.maestro import *
from dotenv import load_dotenv
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import re
import os
import pandas as pd

# Carrega as variáveis de ambiente
load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False

#Atualiza a planilha Excel com as informações do perfil extraído
def atualizar_planilha(nome, cargo, empresa, tempo, file_path='Dados-leads.xlsx'):

    # Expressões regulares para limpar dados
    regex_1 = r'^[^·]+'
    regex_2 = r'·\s*(.*)'

    empresa_result = re.search(regex_1, empresa)
    tempo_result = re.search(regex_2, tempo)

    if empresa_result:
        empresa = empresa_result.group().strip()
    if tempo_result:
        tempo = tempo_result.group(1).strip()

    # Ler o arquivo Excel
    df = pd.read_excel(file_path, engine='openpyxl')

    # Adicionar o nome extraído à próxima linha disponível no DataFrame
    nova_linha = len(df)
    df.at[nova_linha, 'NOME'] = nome
    df.at[nova_linha, 'CARGO'] = cargo
    df.at[nova_linha, 'EMPRESA'] = empresa
    df.at[nova_linha, 'TEMPO'] = tempo
    
    # Salvar as alterações na planilha Excel
    df.to_excel(file_path, index=False, engine='openpyxl', na_rep='')

#Inicializa o navegador e abre a página de login do LinkedIn
def iniciar_navegador():
    bot = WebBot()
    bot.headless = False
    bot.driver_path = ChromeDriverManager().install()
    bot.browse("https://www.linkedin.com/login/pt")
    bot.driver.maximize_window()
    return bot

def realizar_login(bot=WebBot):
    while True:
        try:
            bot.find_element("username", By.ID).click()
            bot.paste(EMAIL)
            bot.find_element("password", By.ID).click()
            bot.paste(SENHA)
            bot.find_element("#organic-div > form > div.login__form_action_container > button", By.CSS_SELECTOR).click()
            break
        except Exception as e:
            print("Erro no login, tentando novamente...")
            sleep(1)

#Busca perfis de LinkedIn usando o termo de busca fornecido
def buscar_perfis(bot=WebBot):
    while True:
        try:
            bot.find_element("#global-nav-typeahead > input", By.CSS_SELECTOR).click()
            bot.paste("desenvolvedor full stack")
            bot.enter()
            break
        except Exception as e:
            print(F"Erro ao buscar perfis, tentando novamente: {e}")
            sleep(1)

    sleep(5)

    while True:
        try:
            bot.find_element("//button[contains(., 'Pessoas')]", By.XPATH).click()
            break
        except Exception as e:
            print("Erro ao aplicar filtro, tentando novamente...")
            sleep(1)

# Extrai dados dos perfis de LinkedIn e atualiza a planilha com essas informações
def extrair_dados_e_atualizar_planilha(bot=WebBot, max_result=2):
    link_perfil = '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]'
    sleep(5)
    
    for i in range(1, max_result + 1):
        try:
            bot.find_element(link_perfil.format(i), By.XPATH).click()
            sleep(5)
            
            nome = bot.find_element('/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span[1]/a/h1', By.XPATH).get_attribute('innerHTML')
            cargo = bot.find_element('//*[@id="profile-content"]/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div[1]/div/div/div/div/div/span[1]', By.XPATH).get_attribute('innerText')
            empresa = bot.find_element('//*[@id="profile-content"]/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div[1]/div/span[1]/span[1]', By.XPATH).get_attribute('innerText')
            tempo = bot.find_element('//*[@id="profile-content"]/div/div[2]/div/div/main/section[5]/div[3]/ul/li[1]/div/div[2]/div[1]/div/span[2]/span[1]', By.XPATH).get_attribute('innerText')
               
            atualizar_planilha(nome, cargo, empresa, tempo)
            bot.back()
        except Exception as e:
            print(f"Erro ao clicar no resultado {i}: {e}")

def main():
    bot = iniciar_navegador()

    realizar_login(bot)
    buscar_perfis(bot)
    extrair_dados_e_atualizar_planilha(bot, max_result=2)
    
    bot.wait(300)
    bot.stop_browser()

if __name__ == '__main__':
    main()
