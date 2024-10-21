from mysql.connector import connect
from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime

def merge_pdfs(pdf_lista, arq_saida):
    merger = PdfMerger()
    
    for pdf in pdf_lista:
        merger.append(pdf)
    
    merger.write(arq_saida)
    merger.close()

def criar_pdf_dados_eleitor(cpf, endereco):
    arq_logo = r'C:\Users\matutino\Desktop\LG\botproduto\pdf\banner.png'
    arq_destino = fr'C:\Users\matutino\Documents\EQUIPE_LINUS_ZLACADEMY\BOT-ELEITOR-AVALIACAO\bot_eleitor\pdf\{cpf}_eleitor.pdf'

    # Conectar ao banco de dados MySQL
    conn = connect(
        host='localhost',
        user='root',
        password='',
        database='banco'
    )
    cursor = conn.cursor()

    # Buscar os dados do eleitor pelo CPF
    cursor.execute("SELECT * FROM eleitor WHERE cpf = %s", (cpf,))
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
        "titulo": dados_eleitor[9],  # Número do título
        "situacao": dados_eleitor[10],  # Situação
        "local_votacao": dados_eleitor[11],  # Local de votação
        "endereco_votacao": dados_eleitor[12],  # Endereço de votação
        "bairro_votacao": dados_eleitor[13],  # Bairro da votação
        "municipio_votacao": dados_eleitor[14],  # Município/UF
    }

    endereco_eleitor = {
        "logradouro": endereco["logradouro"],
        "bairro": endereco["bairro"],
        "cidade": endereco["localidade"],
        "uf": endereco["uf"],
        "cep": endereco["cep"]
    }

    # Cria o documento PDF
    pdf = SimpleDocTemplate(arq_destino, pagesize=A4)

    # Estilos
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']
    estilo_normal = estilos['Normal']
    estilo_centralizado = ParagraphStyle(name='Centralizado', parent=estilos['Normal'], alignment=1)

    # Cabeçalho com imagem e título
    imagem = Image(arq_logo, width=320, height=50)
    titulo = Paragraph(f"{dados['nome']}", estilo_titulo)

    # Data e hora atual no formato brasileiro
    paragrafo_data_hora = Paragraph(f"Data e Hora: {dados['data_hora']}", estilo_normal)

    # Criação dos elementos do PDF
    elementos = [imagem, titulo, paragrafo_data_hora]

    # CPF, Data de Nascimento, Nome da Mãe
    elementos.append(Paragraph(f"CPF: {dados['cpf']}", estilo_normal))
    elementos.append(Paragraph(f"Data de Nascimento: {dados['data_nascimento']}", estilo_normal))
    elementos.append(Paragraph(f"Nome da Mãe: {dados['nome_mae']}", estilo_normal))

    # Endereço do Eleitor (obtido via API)
    elementos.append(Paragraph("ENDEREÇO DO ELEITOR", estilo_centralizado))
    elementos.append(Paragraph(f"CEP: {endereco_eleitor['cep']}", estilo_normal))
    elementos.append(Paragraph(f"Logradouro: {endereco_eleitor['logradouro']}", estilo_normal))
    elementos.append(Paragraph(f"Bairro: {endereco_eleitor['bairro']}", estilo_normal))
    elementos.append(Paragraph(f"Cidade: {endereco_eleitor['cidade']}/{endereco_eleitor['uf']}", estilo_normal))

    # Dados Eleitorais
    elementos.append(Paragraph("DADOS ELEITORAIS", estilo_centralizado))
    elementos.append(Paragraph(f"Número do título: {dados['titulo']}", estilo_normal))
    elementos.append(Paragraph(f"Situação: {dados['situacao']}", estilo_normal))
    elementos.append(Paragraph(f"Local de votação: {dados['local_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Endereço de votação: {dados['endereco_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Bairro da votação: {dados['bairro_votacao']}", estilo_normal))
    elementos.append(Paragraph(f"Município/UF: {dados['municipio_votacao']}", estilo_normal))

    # Geração do PDF
    pdf.build(elementos)
    print(f"PDF gerado com sucesso em {arq_destino}")
