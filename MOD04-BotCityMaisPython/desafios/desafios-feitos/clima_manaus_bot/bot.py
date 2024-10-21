"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Importar o ChromeDriverManager para utilizar o Chrome na automação
# É preciso instalar anteriormente
from webdriver_manager.chrome import ChromeDriverManager

# Import biblis
import re

# Procedimento
def pesquisar_cidade(bot, cidade):

    # A diferença de Função e Procedimento é que a primeira retorna alguma coisa e a segunda apenas executa

    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregando.')

    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(cidade)

    bot.wait(1000)
    bot.enter()

def extrair_dados_clima(bot):

    count = 0

    while True:
        count+=1
        dia_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[1]', By.XPATH).get_attribute('innerText')
        temp_max = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[1]/span[1]', By.XPATH).get_attribute('innerText')
        temp_min = bot.find_element(f'//*[@id="wob_dp"]/div[{count}]/div[3]/div[2]/span[1]', By.XPATH).get_attribute('innerText')
        print(f'Dia: {dia_semana.capitalize().replace('.', '')} - Temperatura: Max = {temp_max} / Min = {temp_min}')
        if count == 8:
            break


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
    # bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    # bot.driver_path = "<path to your WebDriver binary>"

    # Opens the BotCity website.
    bot.driver_path = ChromeDriverManager().install()
    bot.browse("https://www.google.com/")

    # Implement here your logic...
    try:
        cidade = "Clima Manaus"
        pesquisar_cidade(bot, cidade)

        bot.wait(1000)

        extrair_dados_clima(bot)
    
    except Exception as e:
        print(e)
        bot.save_screenshot('erro.png')
    
    finally:
        # Esperar
        bot.wait(5000)

        # Fecha o navegador
        bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
