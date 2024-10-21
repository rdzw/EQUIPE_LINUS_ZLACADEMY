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


def pesquisar_produto(bot, produto):
    bot.browse("https://www.amazon.com")
    bot.wait(2000)
    while len(bot.find_elements('//*[@id="twotabsearchtextbox"]', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado...')
    bot.find_element('//*[@id="twotabsearchtextbox"]', By.XPATH).send_keys(produto)
    bot.wait(1000)
    bot.enter()


def extrair_dados_produto(bot):
    while len(bot.find_elements('//*[@id="search"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregando...')

    valores = bot.find_elements('a-price-whole', By.CLASS_NAME)

    if valores:
        valor = valores[0].get_attribute('innerText')
        print(f'Valor: {valor}')
        bot.wait(1000)
        return valor
    else:
        print('Nenhum valor encontrado.')
        return None

def calc_usd_brl(bot,valor_us,cotacao):
    bot.wait(1000)

    valor_us_limpo = valor_us.replace('\n', '').replace('.', '')

    print(f'Cotação: {cotacao}')
    print(f'Valor US: {valor_us_limpo}')

    if type(valor_us_limpo) != float:
        valor_us_limpo = float(valor_us_limpo)
    if type(cotacao) != float:
        cotacao = float(cotacao)

    valor_br = valor_us_limpo * cotacao
    return round(valor_br, 2)


def executar_api():
    http=BotHttpPlugin('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    return http.get_as_json()


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()


    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")


    bot = WebBot()


    # Configure whether or not to run on headless mode
    bot.headless = False


    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME


    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    try:
        retornoJSON = executar_api()
        # print(retornoJSON)
        cotacao = retornoJSON['USDBRL']['high']

        produto = "kindle"
        pesquisar_produto(bot,produto)
        valor_us = extrair_dados_produto(bot)
        valor_br = calc_usd_brl(bot, valor_us, cotacao)
        bot.wait(1000)
        print(f'R$ {valor_br}')


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