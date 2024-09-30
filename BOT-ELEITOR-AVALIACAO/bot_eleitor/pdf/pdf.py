from fpdf import FPDF
from PyPDF2 import PdfMerger
import os

def gerar_pdf_eleitor(eleitor, endereco, cpf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Banner
    pdf.image('C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\banner.png', x=10, y=8, w=100)

    # Dados do eleitor
    pdf.cell(200, 10, txt=f"Nome: {eleitor['nome']}", ln=True)
    pdf.cell(200, 10, txt=f"CPF: {cpf}", ln=True)
    pdf.cell(200, 10, txt=f"CEP: {eleitor['cep']}", ln=True)
    pdf.cell(200, 10, txt=f"Endereço: {endereco['logradouro']}, {endereco['bairro']}", ln=True)

    eleitor_pdf = f'C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\\{cpf}_eleitor.pdf'
    pdf.output(eleitor_pdf)
    return eleitor_pdf

def gerar_pdf_titulo(eleitor, cpf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Dados eleitorais
    pdf.cell(200, 10, txt=f"Título Eleitoral: {eleitor['titulo_eleitoral']}", ln=True)
    pdf.cell(200, 10, txt="Situação: REGULAR", ln=True)

    titulo_pdf = f'C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\\{cpf}_titulo.pdf'
    pdf.output(titulo_pdf)
    return titulo_pdf
s
def merge_pdfs(cpf):
    merger = PdfMerger()
    titulo_pdf = f'C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\\{cpf}_titulo.pdf'
    eleitor_pdf = f'C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\\{cpf}_eleitor.pdf'
    merger.append(titulo_pdf)
    merger.append(eleitor_pdf)

    merged_pdf = f'C:\Users\noturno\Desktop\BotCity-Python\LG\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\\{cpf}.pdf'
    merger.write(merged_pdf)
    merger.close()

    return merged_pdf
