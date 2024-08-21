from botcity.web import WebBot, Browser, By
from seleniumbase import Driver
from time import sleep
import pandas as pd
import os

def process_data():
    # Diretório onde os arquivos foram baixados
    download_dir = 'C:/Users/adema/OneDrive/Área de Trabalho/DEVELOP/bot-busca-dado-site/downloaded_files/'

    # Lista de arquivos que serão processados
    files = ['July 2024 No Steel Molybdenum.xlsx', 
             'June 2024 No Steel Molybdenum.xlsx', 
             'May 2024 No Steel Molybdenum.xlsx']

    # Lista para armazenar os DataFrames
    dataframes = []

    # Processa cada arquivo
    for file in files:
        file_path = os.path.join(download_dir, file)
        if os.path.exists(file_path):
            # Carrega o arquivo Excel em um DataFrame
            df = pd.read_excel(file_path)
            dataframes.append(df)
        else:
            print(f"Arquivo {file} não encontrado em {download_dir}.")

    # Concatena todos os DataFrames em um único DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Salva o DataFrame resultante em um novo arquivo Excel
    output_file = os.path.join(download_dir, 'combined_data.xlsx')
    combined_df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Dados processados e salvos em {output_file}.")

def main():

    # Inicializa o WebBot (se você quiser usar isso para algo específico mais tarde)
    bot = WebBot()
    bot.headless = False  # Defina como True se preferir rodar em modo headless
    bot.driver_path = 'resources/chromedriver.exe'
    sleep(3)

    # Cria uma instância do Driver (seleniumbase) com undetected_chromedriver (uc)
    driver = Driver(uc=True, headless=False)

    # Navega para a URL usando o seleniumbase
    driver.get("https://www.lme.com/Account/Login")
    sleep(10)

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Aceita os cookies da página
    try:
        login = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/button[2]')
        login.click()
        sleep(2)
        print("Cookie clicado.")
    except Exception as e:
        print(f"Erro: {e}")
        sleep(2)

    # Aguardar até que o campo de usuário esteja disponível
    while True:
        try:
            email_field = driver.find_element(By.CSS_SELECTOR, '#Email')
            email_field.click()
            sleep(2)
            email_field.send_keys('ademar.castro.fh@gmail.com')
            break
        except Exception as e:
            print(f'Campo de usuário não encontrado, tentando novamente: {e}')
            sleep(1)

    # Aguardar até que o campo de senha esteja disponível
    while True:
        try:
            password_field = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/form/div[2]/input')
            password_field.click()
            sleep(2)
            password_field.send_keys('qyiaXnRN9EfC3J!')
            break
        except Exception as e:
            print(f"Campo de senha não encontrado, tentando novamente: {e}")
            sleep(1)

    try:
        driver.find_element(By.CSS_SELECTOR, 'body > main > div > div.form > div > form > div.form__block > button').click()
        sleep(5)
    except Exception as e:
        print(f'Campo de login não encontrado, tentando novamente: {e}')
        sleep(1)

    # Navega até a página dos datasets
    try:
        data = driver.find_element("/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/button", By.XPATH)
        data.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento Data: {e}")
    sleep(3)

    try:
        report = driver.find_element("/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/div/ul/li[3]/button/span", By.XPATH)
        report.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento Report: {e}")
    sleep(3)

    try:
        monthly = driver.find_element("/html/body/header/div[1]/div/div/div[2]/nav/ul/li[4]/div/ul/li[3]/div/div[2]/ul/li[2]/a", By.XPATH)
        monthly.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento Monthly: {e}")
    sleep(3)

    try:
        primeiro = driver.find_element("/html/body/main/div/div[1]/div[1]/div[2]/div/p[1]/a", By.XPATH)
        primeiro.click()
        sleep(2)
    except Exception as e:
        print(f"Erro ao tentar baixar o primeiro arquivo: {e}")
        sleep(2)

    try:
        segundo = driver.find_element("/html/body/main/div/div[1]/div[1]/div[2]/div/p[2]/a", By.XPATH)
        segundo.click()
        sleep(2)
    except Exception as e:
        print(f"Erro ao tentar baixar o segundo arquivo: {e}")
        sleep(2)

    try:
        terceiro = driver.find_element("/html/body/main/div/div[1]/div[1]/div[2]/div/p[3]/a", By.XPATH)
        terceiro.click()
        sleep(2)
    except Exception as e:
        print(f"Erro ao tentar baixar o terceiro arquivo: {e}")
        sleep(2)

    # Realiza o tratamento dos dados

    process_data()

    # Finaliza e limpa os recursos
    driver.quit()
    bot.stop_browser()

if __name__ == '__main__':
    main()
