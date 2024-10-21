from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import pandas as pd

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    #arquivo excel
    file_path = r'resources\PedidosEmprestimo.xlsx'

    # Ler o arquivo Excel
    df = pd.read_excel(file_path, engine='openpyxl')

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://uibank.uipath.com/welcome")

    bot.maximize_window()

    bot.wait(3000)

    for _ in range(2):  # Rola a página para baixo
        bot.page_down()
        sleep(1)
   
    totalAprovado = 0
    totalNaoAprovado = 0

    #realiza clique no button "Apply For Loan"
    xpath = "/html/body/app-root/body/div/app-welcome-page/div[2]/div/div[3]/div/button"
    element = bot.find_element(xpath, By.XPATH)
    element.click()
    sleep(2)
    
    #realiza clique no button "Apply For Loan"
    button_applyForLoan = bot.find_element("applyButton", By.ID)
    button_applyForLoan.click()
    
    #extraia dados da plnailha para preencher nos campos do site
    for index, row in df.iterrows():
        bot.page_up()

        # variaveis para acessar os valores da planilha
        email = row['Email do Solicitante']
        emprestimo = row['Montante do Empréstimo']
        termoEmprestimo = row['Termo do Empréstimo']
        rendaAnualAtual = row['Renda Anual Atual( Antes dos Impostos)']
        idade = row['Idade']
        
        # Email
        campoEmail = bot.find_element("email", By.ID)
        campoEmail.click()
        bot.paste(email)
        sleep(1)

        # Valor do empréstimo
        campoValorEmprestimo = bot.find_element("amount", By.ID)
        campoValorEmprestimo.click()
        bot.paste(str(emprestimo)) 

        # Termo do empréstimo
        campoTermoEmprestimo = bot.find_element("term", By.ID)

        # Seleciona o termo do empréstimo no dropdown
        selectTermo = Select(campoTermoEmprestimo)
        selectTermo.select_by_visible_text(str(termoEmprestimo))
        sleep(1)

        # Renda Anual Atual
        campoRendaAnualAtual = bot.find_element("income", By.ID)
        campoRendaAnualAtual.click()
        bot.paste(str(rendaAnualAtual))
        sleep(1)

        # Idade
        campoIdade = bot.find_element("age", By.ID)
        campoIdade.click()
        bot.paste(str(idade))
        sleep(1)
    	
        # pula para o botão de submissão
        bot.tab()
        sleep(1)
        
        #clica no botão de submissão
        btnSubmit = bot.find_element("submitButton", By.ID)
        btnSubmit.click()
        sleep(2)
        
        # Procura a mensagem de aprovação usando XPath 
        mensagem_aprovacao = bot.find_element("//h1[contains(text(), 'approved for a loan with UiBank!')]", By.XPATH)
        if mensagem_aprovacao:
            apr = float(bot.find_element("rateValue", By.ID).get_attribute('innerHTML'))  
            idEmprestimo = bot.find_element("loanID", By.ID).get_attribute('innerHTML')
               
            #extraindo informações do site  como porcentagem de aprovado e o id do emprestimo, preenchendo na planilha
            df.at[index, 'Status do Empréstimo'] = 'Aprovado'
            df.at[index, 'ID do Empréstimo'] = str(idEmprestimo)
            df.at[index, 'APR'] = apr

            totalAprovado += 1
                                     
        else:
            df.at[index, 'Status do Empréstimo'] = 'Não Aprovado'

            totalNaoAprovado += 1
        
        # Salva as alterações de volta na planilha
        df.to_excel(file_path, index=False, engine='openpyxl', na_rep='')

        # Cilcar em Apply For Another Loan
        btnSubmitApply = bot.find_element("applyForNewLoanButton", By.ID)
        btnSubmitApply.click()
        sleep(2)
    
    # Imprimir no console
    print("Relatório de Cadastro de Funcionários")
    print("-------------------------------------")
    print(f"Total de emprestimos aprovados: {totalAprovado}")
    print(f"Total de emprestimos não aprovados: {totalNaoAprovado}")
    
    bot.wait(1000)
    bot.stop_browser()
    
def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()