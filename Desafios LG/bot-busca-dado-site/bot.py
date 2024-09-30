from botcity.web import WebBot, Browser, By
from seleniumbase import Driver
from time import sleep
import pandas as pd
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
import os

# Carrega as variáveis de ambiente
load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('PASSWORD')

def process_data(directory: str, files: list, output_path: str):
    # Processa e mescla arquivos Excel em um único arquivo
    df_total = pd.DataFrame()
    
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        df = pd.read_excel(file_path, sheet_name="ABR")
        df["Mês/Ano"] = file_name.split()[0] + " 2024"
        df_total = pd.concat([df_total, df], ignore_index=True)
    
    # Reorganizar colunas
    columns_order = [col for col in df_total.columns if col != "Mês/Ano"] + ["Mês/Ano"]
    df_total = df_total[columns_order]
    df_total = df_total.replace({pd.NA: ''}).fillna('')
    
    # Salvar dados mesclados
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_total.to_excel(output_path, index=False)
    print(f"Dados mesclados salvos com sucesso em {output_path}")

def initialize_browser():
    # Inicializa o navegador e retorna a instância do Driver e do WebBot
    driver = Driver(uc=True, headless=False)
    bot = WebBot()
    bot.headless = False
    bot.driver_path = ChromeDriverManager().install()
    sleep(3)
    return driver, bot

def login_to_website(driver: Driver):
    # Realiza o login no site
    driver.get("https://www.lme.com/Account/Login")
    sleep(10)
    driver.maximize_window()

    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[2]').click()
        sleep(2)
    except Exception as e:
        print(f"Erro ao aceitar cookies: {e}")
        sleep(2)
    
    # Login
    while True:
        try:
            email_field = driver.find_element(By.ID, 'Email')
            email_field.send_keys(EMAIL)
            break
        except Exception as e:
            print(f'Campo de usuário não encontrado: {e}')
            sleep(1)
    
    while True:
        try:
            password_field = driver.find_element(By.ID, 'Password')
            password_field.send_keys(SENHA)
            break
        except Exception as e:
            print(f"Campo de senha não encontrado: {e}")
            sleep(1)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'body > main > div > div.form > div > form > div.form__block > button').click()
        sleep(5)
    except Exception as e:
        print(f'Campo de login não encontrado: {e}')
        sleep(1)

def navigate_and_download(driver: Driver):
    # Navega até os datasets e realiza o download dos arquivos.
    try:
        driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/button").click()
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/div/ul/li[3]/button/span").click()
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/div/ul/li[3]/div/div[2]/ul/li[2]/a").click()
        sleep(3)
        
        for i in range(1, 4):
            try:
                driver.find_element(By.XPATH, f"/html/body/main/div/div[1]/div[1]/div[2]/div/p[{i}]/a").click()
                sleep(2)
            except Exception as e:
                print(f"Erro ao tentar baixar o {i}º arquivo: {e}")
                sleep(2)
    except Exception as e:
        print(f"Erro ao navegar e baixar arquivos: {e}")

def main():
    driver, bot = initialize_browser()
    
    try:
        login_to_website(driver)
        navigate_and_download(driver)
        process_data(
            directory="downloaded_files",
            files=[
                "May 2024 No Steel  Molybdenum.xlsx",
                "June 2024 No Steel  Molybdenum.xlsx",
                "July 2024 No Steel  Molybdenum.xlsx"
            ],
            output_path="output_files/Mesclado_Maio_Junho_Julho_2024_Organizado.xlsx"
        )
    finally:
        driver.quit()
        bot.stop_browser()

if __name__ == '__main__':
    main()
