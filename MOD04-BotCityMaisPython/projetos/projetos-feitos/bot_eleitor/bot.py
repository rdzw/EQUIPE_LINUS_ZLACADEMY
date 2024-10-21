###
# EQUIPE LINUS
#
# Ademar Alves Castro Filho
# Jade
# Natália
# Rodrigo
###

from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin

import requests

import e_mail.e_mail as e_mail
import planilha.planilha as planilha

from pdf import pdf

from so import so

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Acessa a API dos Correios (ViaCEP) e busca o endereço completo do eleitor com base no CEP
def api_cep_eleitor():
    try:
        # Obtenha todos os eleitores gravados no banco de dados
        http = BotHttpPlugin('http://127.0.0.1:5000/eleitor')
        eleitores = http.get_as_json()

        # Lista de pdfs
        lista_pdf = []

        # Verificar se há dados retornados
        if 'dados' in eleitores:
            for eleitor in eleitores['dados']:
                cep = eleitor["cep"]
                print(f'Buscando endereço para o CEP: {cep}')

                try:
                    # Chamada para a API ViaCEP para obter o endereço a partir do CEP
                    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
                    response.raise_for_status()  # Levanta exceção para códigos de status 4xx/5xx

                    endereco = response.json()

                    # Verificar se o CEP é válido
                    if 'erro' not in endereco:
                        print(f"Nome do eleitor: {eleitor['nome']}")
                        print(f"Endereço completo: {endereco}")

                        pdf.criar_pdf_dados_eleitor(eleitor["cpf"], endereco)

                        lista_pdf.append(f'C:\\Users\\matutino\\Documents\\EQUIPE_LINUS_ZLACADEMY\\BOT-ELEITOR-AVALIACAO\\bot_eleitor\\pdf\\{eleitor["cpf"]}_eleitor.pdf')
                        lista_pdf.append(f'C:\\Users\\matutino\\Documents\\EQUIPE_LINUS_ZLACADEMY\\BOT-ELEITOR-AVALIACAO\\bot_eleitor\\pdf\\{eleitor["cpf"]}_titulo.pdf')
                        pdf.merge_pdfs(lista_pdf, f'C:\\Users\\matutino\\Documents\\EQUIPE_LINUS_ZLACADEMY\\BOT-ELEITOR-AVALIACAO\\bot_eleitor\\pdf\\{eleitor["cpf"]}.pdf')

                    else:
                        print(f"CEP {cep} inválido ou não encontrado.")
                except requests.exceptions.RequestException as e:
                    # Captura qualquer erro durante a requisição HTTP
                    print(f"Erro ao acessar a API ViaCEP para o CEP {cep}: {e}")
                except ValueError as e:
                    # Captura erros ao processar a resposta JSON
                    print(f"Erro ao processar a resposta da API ViaCEP para o CEP {cep}: {e}")
            
                print('Gerando arquivo Produtos.pdf com o merge entre os arquivos: ListaProduto.pdf + SiteProduto.pdf...')
                lista_pdf = []
                lista_pdf.append('C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\ListaProduto.pdf')
                lista_pdf.append('C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\SiteProduto.pdf')
                pdf.merge_pdfs(lista_pdf,'C:\\Users\\matutino\\Desktop\\LG\\botproduto\\pdf\\Produtos.pdf')
        else:
            print("Nenhum eleitor encontrado ou dados malformados.")
    
    except Exception as e:
        # Captura exceções gerais durante a obtenção dos eleitores
        print(f"Erro ao obter eleitores: {e}")

def api_lista_usuarios():
    http=BotHttpPlugin('http://127.0.0.1:5000/usuario')
    return http.get_as_json()


def inserir_eleitor(linha_excel, nr_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais):
    # Valida se as chaves esperadas estão no dicionário
    if all(key in linha_excel for key in ['CPF', 'NOME', 'DATA_NASCIMENTO', 'NOME_MAE', 'CEP', 'NRO_ENDERECO']):
        try:
            url = 'http://127.0.0.1:5000/eleitor'
            headers = {'Content-Type': 'application/json'}

            # Cria o dicionário eleitor_JSON com os dados do eleitor
            eleitor_JSON = {
                "cpf": linha_excel["CPF"],
                "nome": linha_excel["NOME"],
                "data_nascimento": linha_excel["DATA_NASCIMENTO"],
                "nome_mae": linha_excel["NOME_MAE"],
                "cep": linha_excel["CEP"],
                "nro_endereco": linha_excel["NRO_ENDERECO"],
                "nro_titulo": nr_titulo,
                "situacao": situacao,
                "secao": secao,
                "zona": zona,
                "local_votacao": local_votacao,
                "endereco_votacao": endereco_votacao,
                "bairro": bairro,
                "municipio_uf": municipio_uf,
                "pais": pais
            }

            # Faz a requisição POST
            resposta = requests.post(url=url, headers=headers, json=eleitor_JSON)
            resposta.raise_for_status()  # Verifica se houve algum erro na requisição
            
            # Retorna a resposta em formato JSON
            retorno = resposta.json()
            return retorno
        
        except requests.exceptions.HTTPError as err:
            print(f"Erro HTTP: {err}")
        except Exception as e:
            print(f"Erro: {e}")
    else:
        print("Linha do Excel não contém todas as informações necessárias.")

def acessar_site(bot):
    bot.browse('https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor')
    bot.maximize_window()
    
     # Aceitar o cookie
    while len(bot.find_elements('//*[@id="modal-lgpd"]/div/div/div[2]/button', By.XPATH)) < 1:
        bot.wait(1000)
        print('Carregando...')
    bot.find_element('//*[@id="modal-lgpd"]/div/div/div[2]/button', By.XPATH).click()

    # Procurar a opção 10
    while len(bot.find_elements('//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button', By.XPATH)) < 1:
        bot.wait(1000)
        print('Carregando...')

    # Ler os dados da planilha
    excel_path = 'planilha\\RelacaoEleitor.xlsx'
    sheet = 'CPF'
    df = planilha.ler_excel(excel_path, sheet) 

    for index, row in df.iterrows():
        cpf = str(row['CPF']).zfill(11)  # Preenche com zero à esquerda até 11 dígitos
        if len(cpf) != 11:
            print(f"CPF inválido: {cpf}")
            continue  # Pula para o próximo CPF, se necessário

        # Extração dos dados
        data_nascimento = row['DATA_NASCIMENTO']
        nome_mae = row['NOME_MAE']
        nome = row['NOME']
        cep = str(row['CEP'])
        nro_endereco = str(row['NRO_ENDERECO'])
        
        data_convertida = data_nascimento.strftime('%d/%m/%Y')

        # Preencher e submeter o formulário
        preencher_formulario(bot, cpf, data_convertida, nome_mae)

        # Extração de informações
        nr_titulo, situacao, secao, zona, local, endereco, bairro, municipio, pais = extrair_informacoes(bot)
        
        linha_excel = {
            "CPF": cpf,
            "NOME": nome,
            "DATA_NASCIMENTO": data_convertida,
            "NOME_MAE": nome_mae,
            "CEP": cep,
            "NRO_ENDERECO": nro_endereco,
        }


        retorno = inserir_eleitor(
        linha_excel,
        nr_titulo,
        situacao,
        secao,
        zona,
        local,  # O que for necessário aqui deve ser definido corretamente
        endereco,  # O que for necessário aqui deve ser definido corretamente
        bairro,
        municipio,
        pais
    )

        # Exibe o retorno da API
        print(retorno)
        # Salvar o PDF
        salvar_pdf(bot, cpf)

        # Fechar modal e retornar ao início
        fechar_modal(bot)

# Função para preencher o formulário no site
def preencher_formulario(bot, cpf, data_convertida, nome_mae):
    bot.find_element('//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button', By.XPATH).click()
    bot.wait(1000)

    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[1]/input', By.XPATH).click()
    bot.paste(cpf)
    bot.wait(1000)

    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input', By.XPATH).click()
    bot.paste(str(data_convertida))
    bot.wait(1000)

    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div[3]/div/input', By.XPATH).click()
    bot.paste(nome_mae)
    bot.wait(1000)

    bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]', By.XPATH).click()
    bot.wait(1000)

# Função para extrair informações do site
def extrair_informacoes(bot):
    numero_titulo = bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[1]/b', By.XPATH).text
    situacao = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[2]/span', By.XPATH).text
    secao = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[1]/span[2]', By.XPATH).text
    zona = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[3]/span[2]', By.XPATH).text
    local = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[1]/span[2]', By.XPATH).text
    endereco = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[2]/span[2]', By.XPATH).text
    bairro = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[4]/span[2]', By.XPATH).text
    municipio = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[3]/span[2]', By.XPATH).text
    pais = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[2]/span[2]', By.XPATH).text
    return numero_titulo, situacao, secao, zona, local, endereco, bairro, municipio, pais

# Função para salvar o PDF
def salvar_pdf(bot, cpf):
    bot.print_pdf(f'pdf\\{cpf}_titulo.pdf')
    bot.wait(1000)

# Função para fechar o modal
def fechar_modal(bot):
    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-consultar-numero-titulo-eleitor/app-avatar-e-nome/div/div/button', By.XPATH).click()
    bot.wait(1000)
    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/app-modal-mensagem/div/div/div/div[2]/button', By.XPATH).click()
    bot.wait(1000)
    bot.find_element('/html/body/main/div/div/div[3]/div/div/app-root/div/app-home/div/div[4]/app-botao-principal[1]/button', By.XPATH).click()

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()


    api_cep_eleitor()
    acessar_site(bot)

    bot.wait(3000)
    bot.stop_browser()
    
    
    print('Enviando E-mail para a lista de usuario com arquivo Produtos.pdf em anexo.')
    arq_anexo = 'pdf\\banner.png'
    retornoJSON_usuarios = api_lista_usuarios()
    lista_produto = retornoJSON_usuarios['dados']
    for usuario in lista_produto:
        destinatario = usuario['email']
        print(f'Enviando e-mail para: {destinatario}')
        assunto = "Lista de Produtos"
        conteudo = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de produtos."
        e_mail.enviar_email(destinatario, assunto, conteudo, arq_anexo)
    
    print('Fim do processamento...')

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()