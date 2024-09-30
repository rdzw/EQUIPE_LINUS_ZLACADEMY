from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def enviar_email(destinatario, assunto, conteudo):
    email = BotEmailPlugin()
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp(host_address="smtp.gmail.com",port=587)
