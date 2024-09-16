from botcity.maestro import * 
import pandas as pd
import PyPDF2
import re

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def extract_pdf_data(pdf_path):
    with open(pdf_path,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ''

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                print(f"Página {page_num + 1} está vazia ou não contém texto.")
            
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

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    pdf_path = 'PDF\Credenciamento_003_Edital_009_2023_-_Circulacao.pdf'
    excel_path = "tabela_extraida.xlsx"

    pdf_text = extract_pdf_data(pdf_path)

    table_data = extract_table(pdf_text)

    excel_path = "tabela_extraida.xlsx"
    save_to_excel(table_data, excel_path)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()