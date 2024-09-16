from botcity.maestro import * 
from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv
import pandas as pd
import PyPDF2
import re
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def extract_pdf_data(pdf_path):
    with open(pdf_path,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""         
    return text

def extract_table(text):

    pattern = re.compile(r'(\d+)\s+([\w\s]+)\s+([\w\s,]+)\s+(\d+h)\s+R\$ (\d+\.\d{3},\d{2})')
    matches = pattern.findall(text)
    data = [list(match) for match in matches]

    return data

def save_to_excel(data, excel_path):
    columns = ['Item', 'Segmento Artístico', 'Tipo', 'Duração', 'Valor']
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(excel_path, index=False)

def send_email(excel_path, email):
    email.configure_smtp("imap.gmail.com", 587)
    email.login(EMAIL, PASSWORD)

    # Definindo os atributos que comporão a mensagem
    para = ["<menezesandreina18@gmail.com>", "<rodrigoword2@gmail.com>"]
    assunto = "Relatório de Extração"
    corpo_email = "<h1>Olá!</h1> Segue em anexo excel contendo dados extraídos do pdf!"
    arquivos = [excel_path]

    email.send_message(assunto, corpo_email, para, attachments=arquivos, use_html=True)

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    email = BotEmailPlugin()

    pdf_path = 'PDF\Credenciamento_003_Edital_009_2023_-_Circulacao.pdf'
    excel_path = "tabela_extraida.xlsx"

    pdf_text = extract_pdf_data(pdf_path)

    table_data = extract_table(pdf_text)

    excel_path = "tabela_extraida.xlsx"
    save_to_excel(table_data, excel_path)

    send_email(excel_path, email)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()