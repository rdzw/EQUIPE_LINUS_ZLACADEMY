from botcity.maestro import * 
from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv
import pandas as pd
import PyPDF2
import re
import os

# Carrega as variáveis de ambiente (email e senha)
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False

#Extrai o texto de um arquivo PDF.
def extract_pdf_data(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return "".join(page.extract_text() or "" for page in reader.pages)

#Extrai uma tabela de dados formatada a partir do texto usando regex.
def extract_table(text):
    pattern = re.compile(r'(\d+)\s+([\w\s]+)\s+([\w\s,]+)\s+(\d+h)\s+R\$ (\d+\.\d{3},\d{2})')
    return [list(match) for match in pattern.findall(text)]

#Salva os dados extraídos em um arquivo Excel.
def save_to_excel(data, excel_path):
    columns = ['Item', 'Segmento Artístico', 'Tipo', 'Duração', 'Valor']
    pd.DataFrame(data, columns=columns).to_excel(excel_path, index=False)

#Configura e envia um email com o arquivo Excel em anexo.
def send_email(excel_path, email):
    email.configure_smtp("imap.gmail.com", 587)
    email.login(EMAIL, PASSWORD)

    para = ["<menezesandreina18@gmail.com>", "<rodrigoword2@gmail.com>"]
    assunto = "Relatório de Extração"
    corpo_email = "<h1>Olá!</h1> Segue em anexo excel contendo dados extraídos do PDF!"
    
    # Envia o email com o arquivo em anexo
    email.send_message(assunto, corpo_email, para, attachments=[excel_path], use_html=True)
    print('Email enviado com sucesso!!')

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID: {execution.task_id}")
    print(f"Task Parameters: {execution.parameters}")

    email = BotEmailPlugin()

    pdf_path = 'PDF/Credenciamento_003_Edital_009_2023_-_Circulacao.pdf'
    excel_path = "tabela_extraida.xlsx"

    pdf_text = extract_pdf_data(pdf_path)
    table_data = extract_table(pdf_text)
    
    save_to_excel(table_data, excel_path)
    send_email(excel_path, email)

def not_found(label):
    print(f"Elemento não encontrado: {label}")

if __name__ == '__main__':
    main()