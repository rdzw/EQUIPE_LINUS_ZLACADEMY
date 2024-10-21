from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime


def merge_pdfs(pdf_lista, arq_saida):
    merger = PdfMerger()
    
    for pdf in pdf_lista:
        merger.append(pdf)
    
    merger.write(arq_saida)
    merger.close()
  
def criar_pdf_lista_produto(produtos):
    arq_logo = 'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\banner.png'
    arq_destino = 'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\ListaProduto.pdf'

    
    # Cria o documento PDF
    pdf = SimpleDocTemplate(arq_destino, pagesize=A4)
    
    # Estilos
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']
    estilo_normal = estilos['Normal']
    estilo_centralizado = ParagraphStyle(name='Centralizado', parent=estilos['Normal'], alignment=1)  # 1 é para centralizar
    
    # Parágrafo de texto
    # paragrafo = Paragraph(texto, estilo_normal)
    
    # Cabeçalho com imagem e título
    imagem = Image(arq_logo, width=320, height=50)
    titulo = Paragraph("Lista de Produto", estilo_titulo)
    
    # Data e hora atual no formato brasileiro
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #paragrafo_data_hora = Paragraph(f"Data e Hora: {data_hora_atual}", estilo_normal)
    paragrafo_data_hora = Paragraph(f"Data e Hora: {data_hora_atual}", estilo_centralizado)
    
    # Cria a tabela de dados
    dados = [["Descrição", "Unidade", "Quantidade", "Preço Real","Preço Dolar"]]
    for produto in produtos:
        dados.append([produto["descricao"], produto["unidade"], produto["quantidade"], produto["preco_real"],produto["preco_dolar"]])
    
    # Cria a tabela
    tabela = Table(dados)
    
    # Define o estilo da tabela
    estilo_tabela = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    tabela.setStyle(estilo_tabela)
    
    # Adiciona os elementos ao documento
    elementos = [imagem, titulo, paragrafo_data_hora, tabela]
    pdf.build(elementos)
