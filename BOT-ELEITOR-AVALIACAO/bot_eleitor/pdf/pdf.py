import mysql.connector
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


def criar_pdf_dados_eleitor(eleitor_id):
    arq_destino = r'C:\Users\noturno\Desktop\BOT-PYTHON\botproduto\pdf\DadosEleitor.pdf'
    
    # Conectar ao banco de dados MySQL
    conn = mysql.connector.connect(
        host='seu_host',  # e.g. 'localhost'
        user='seu_usuario',
        password='sua_senha',
        database='seu_banco_de_dados'
    )
    cursor = conn.cursor()
    
    # Buscar os dados do eleitor pelo ID
    cursor.execute("SELECT * FROM eleitores WHERE id = %s", (eleitor_id,))
    dados_eleitor = cursor.fetchone()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    if not dados_eleitor:
        print("Eleitor não encontrado.")
        return
    
    # Mapeia os dados para um dicionário
    dados = {
        "nome": dados_eleitor[1],  # Nome
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),  # Data e hora atual
        "cpf": dados_eleitor[2],  # CPF
        "data_nascimento": dados_eleitor[3],  # Data de nascimento
        "nome_mae": dados_eleitor[4],  # Nome da mãe
        "cep": dados_eleitor[5],  # CEP
        "logradouro": dados_eleitor[6],  # Logradouro
        "bairro": dados_eleitor[7],  # Bairro
        "cidade": dados_eleitor[8],  # Cidade
        "titulo": dados_eleitor[9],  # Número do título
        "situacao": dados_eleitor[10],  # Situação
        "local_votacao": dados_eleitor[11],  # Local de votação
        "endereco_votacao": dados_eleitor[12],  # Endereço de votação
        "bairro_votacao": dados_eleitor[13],  # Bairro da votação
        "municipio_votacao": dados_eleitor[14]  # Município/UF
    }
    
    # Cria o documento PDF
    pdf = SimpleDocTemplate(arq_destino, pagesize=A4)
    
    # Estilos
    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(name='Titulo', fontSize=16, alignment=1, spaceAfter=20)  # Centralizado
    estilo_normal = estilos['Normal']
    
    # Criação dos elementos do PDF
    elementos = []
    
    # Nome do eleitor - Centralizado e grande
    titulo = Paragraph(dados["nome"], estilo_titulo)
    elementos.append(titulo)
    
    # Adiciona um espaço após o título
    elementos.append(Spacer(1, 12))
    
    # Data e Hora
    paragrafo_data_hora = Paragraph(f"Data e Hora: {dados['data_hora']}", estilo_normal)
    elementos.append(paragrafo_data_hora)
    
    # CPF, Data de Nascimento, Nome da Mãe
    elementos.append(Paragraph(f"CPF: {dados['cpf']}", estilo_normal))
    elementos.append(Paragraph(f"Data de Nascimento: {dados['data_nascimento']}", estilo_normal))
    elementos.append(Paragraph(f"Nome da Mãe: {dados['nome_mae']}", estilo_normal))
    
    # Endereço
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph("ENDEREÇO DO ELEITOR", estilo_normal))
    elementos.append(Paragraph(f"CEP: {dados['cep']}", estilo_normal))
    elementos.append(Paragraph(f"Logradouro: {dados['logradouro']}", estilo_normal))
    elementos.append(Paragraph(f"Bairro: {dados['bairro']}", estilo_normal))
    elementos.append(Paragraph(f"Cidade: {dados['cidade']}", estilo_normal))
    
    # Dados Eleitorais
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph("DADOS ELEITORAIS", estilo_normal))
    elementos.append(Paragraph(f"Número do título: {dados['titulo']}", estilo_normal))
    elementos.append(Paragraph(f"Situação: {dados['situacao']}", estilo_normal))
    
    # Local de Votação
    elementos.append(Paragraph(f"Local de votação: {dados['local_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Endereço de votação: {dados['endereco_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Bairro da votação: {dados['bairro_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Município/UF: {dados['municipio_votacao']}", estilo_normal))
    
    # Geração do PDF
    pdf.build(elementos)
    print(f"PDF gerado com sucesso em {arq_destino}")

# Exemplo de chamada para criar o PDF do eleitor
criar_pdf_dados_eleitor(eleitor_id=1)  # Altere o ID conforme necessário
