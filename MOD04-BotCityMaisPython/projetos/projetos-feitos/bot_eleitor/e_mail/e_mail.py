from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
SENHA = os.getenv('PASSWORD')

def enviar_email(destinatario, assunto, conteudo, arquivo_anexo):
    email = BotEmailPlugin()
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp("smtp.gmail.com", 587)
    email.login(email=EMAIL, password=SENHA)

    to = [destinatario]
    subject = assunto
    body = conteudo
    files = [arquivo_anexo]

    email.send_message(subject, body, to, attachments=files, use_html=True)
    email.disconnect()
