from botcity.plugins.email import BotCityEmailPlugin

def enviar_email(cpf, arquivo_pdf):
    email_plugin = BotCityEmailPlugin(username="seu_email@gmail.com", password="sua_senha", smtp_server="smtp.gmail.com", smtp_port=587)
    
    assunto = "Eleitor"
    conteudo = "<h2>Sistema automatizado de coleta de dados do Eleitor</h2> Em anexo, os dados do Eleitor."
    
    email_plugin.send(
        to="benevaldo.goncalves@ifam.edu.br",
        subject=assunto,
        html=conteudo,
        attachments=[arquivo_pdf]
    )
