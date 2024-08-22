from botcity.web import WebBot, By
from botcity.maestro import BotMaestroSDK
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def fetch_iframe_content(url):
    # Faz uma requisição GET
    page = requests.get(url)
    
    # Verifica se a solicitação foi bem-sucedida
    if page.status_code == 200:
        print(f"Requisição bem sucedida para {url}: {page.status_code}")
    else:
        print(f"Erro na requisição para {url}: {page.status_code}")
        return None
    
    # Cria o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, "html.parser")
    
    return soup

def convert_to_numeric(price_str):
    # Remove o cifrão e pontos
    price_str = price_str.replace('R$', '').replace('.', '')

    # Troca a vírgula por ponto
    price_str = price_str.replace(',', '.')
    
    # Debug: exibe o preço após limpeza
    print(f"Preço para conversão após limpeza: {price_str}")

    try:
        return float(price_str)
    except ValueError:
        print("Erro ao converter o preço para float.")
        return None

def update_excel(price, name):
    file_path = "precos.xlsx"
    
    # Criar um DataFrame vazio se o arquivo não existir
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Nome", "Data", "Preço"])
    else:
        df = pd.read_excel(file_path)
    
    # Adicionar nova linha ao DataFrame
    today = datetime.now().strftime("%Y-%m-%d")
    new_data = pd.DataFrame({"Nome": [name], "Data": [today], "Preço": [price]})
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Salvar o DataFrame atualizado no arquivo Excel
    df.to_excel(file_path, index=False)
    
    # Atualização e visualização do gráfico
    df['Data'] = pd.to_datetime(df['Data'])
    df.set_index('Data', inplace=True)
    
    # Converter coluna "Preço" para numérico
    df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')

    # Verificar se há dados numéricos para plotar
    if df['Preço'].notna().any():
        plt.figure(figsize=(10, 5))
        df.plot(y='Preço', kind='line', marker='o')
        plt.title('Variação de Preço ao Longo do Tempo')
        plt.xlabel('Data')
        plt.ylabel('Preço')
        plt.grid(True)
        plt.savefig("grafico_precos.png")
        plt.show()
    else:
        print("Nenhum dado numérico para plotar.")

def main():
    url = "https://www.amazon.com.br/dp/B00CLOZBHK/ref=fs_a_atv_5"  # Substitua pela URL da sua página
    soup = fetch_iframe_content(url)
    
    if not soup:
        return

    # Encontrar o preço e o nome do produto
    name = soup.find(id="productTitle")
    price = soup.find(class_="a-offscreen")

    if price and name:
        price_str = price.text.strip()
        name_str = name.text.strip()
        print(f"Preço extraído: {price_str}")  # Debug: exibe o preço extraído
        price = convert_to_numeric(price_str)
        if price is not None:
            print(f"Preço convertido: {price}")
            update_excel(price, name_str)
        else:
            print("Preço em formato inválido.")
    else:
        print("Preço ou nome do produto não encontrado.")

if __name__ == '__main__':
    main()
