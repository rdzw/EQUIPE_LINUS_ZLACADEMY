# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
#configuracao chromer
from webdriver_manager.chrome import ChromeDriverManager
#configurar http, antes tem executar terminal: pip install botcity-http-plugin
from botcity.plugins.http import BotHttpPlugin


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False




def pesquisar_cidade(bot, cidade):
    bot.browse("https://www.google.com")
    bot.wait(2000)
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')
    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(cidade)
    bot.wait(1000)
    bot.enter()


def extrair_dados_clima(bot):
    count = 0
    while True:
        count+=1
        dia_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[1]', By.XPATH).text
        max = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[1]/span[1]', By.XPATH).text
        min = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[2]/span[1]', By.XPATH).text
        print("Dia: "+dia_semana+" - Max: "+max+" - Min: "+min)
        if count == 8:
            break


def executar_api():
    http=BotHttpPlugin('https://servicodados.ibge.gov.br/api/v1/localidades/estados/13/regioes-metropolitanas')
    return http.get_as_json()


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()


    # print(f"Task ID is: {execution.task_id}")
    # print(f"Task Parameters are: {execution.parameters}")


    bot = WebBot()


    # Configure whether or not to run on headless mode
    bot.headless = False


    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME


    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()


    # Implement here your logic...
    try:
        retornoJSON = executar_api()
        for item in retornoJSON:
            for m in item['municipios']:
                cidade = "clima "+m['nome']+", AM"
                print("Cidade: "+m['nome'])
                pesquisar_cidade(bot,cidade)
                bot.wait(1000)
                extrair_dados_clima(bot)
   
    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')
   
    finally:
        bot.wait(2000)
        bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()