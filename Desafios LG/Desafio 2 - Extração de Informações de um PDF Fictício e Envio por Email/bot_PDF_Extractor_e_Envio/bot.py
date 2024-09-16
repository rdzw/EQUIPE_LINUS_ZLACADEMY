from botcity.maestro import * 
import pandas as pd
import PyPDF2

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

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    pdf_path = 'PDF\Credenciamento_003_Edital_009_2023_-_Circulacao.pdf'

    pdf_text = extract_pdf_data(pdf_path)

    print(pdf_text)

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()