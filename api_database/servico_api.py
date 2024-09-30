# Importações
from flask import Flask, make_response, jsonify, request, Response
from repository import eleitor

# Instanciar
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# --------------------------------------------------------
#           Inicio: Serviços da api usuário
# --------------------------------------------------------

from flask import Flask, jsonify, request, make_response
from repository import eleitor  # Importando o módulo eleitor

app_api = Flask(__name__)

# Criar um novo eleitor
@app_api.route('/eleitor', methods=['POST'])
def criar_eleitor():
    eleitor_json = request.json
    try:
        eleitor.criar_eleitor(eleitor_json)
        sucesso = True
        mensagem = 'Eleitor criado com sucesso'
    except Exception as ex:
        sucesso = False
        mensagem = f'Erro: {ex}'
    
    return make_response(jsonify(status=sucesso, mensagem=mensagem))
# Fim: criar_eleitor()

# Obter eleitor pelo CPF
@app_api.route('/eleitor/<cpf>', methods=['GET'])
def obter_eleitor_cpf(cpf):
    eleitor_data = eleitor.obter_eleitor_cpf(cpf)
    if eleitor_data:
        return make_response(jsonify(status=True, mensagem='Eleitor encontrado', dados=eleitor_data))
    else:
        return make_response(jsonify(status=False, mensagem='Eleitor não encontrado'))
# Fim: obter_eleitor_cpf()

# Listar todos os eleitores
@app_api.route('/eleitor', methods=['GET'])
def listar_eleitores():
    eleitores = eleitor.listar_eleitor()
    return make_response(jsonify(status=True, dados=eleitores))
# Fim: listar_eleitores()

# Atualizar eleitor
@app_api.route('/eleitor', methods=['PUT'])
def atualizar_eleitor():
    eleitor_json = request.json
    try:
        eleitor.atualizar_eleitor(eleitor_json)
        sucesso = True
        mensagem = 'Eleitor atualizado com sucesso'
    except Exception as ex:
        sucesso = False
        mensagem = f'Erro: {ex}'
    
    return make_response(jsonify(status=sucesso, mensagem=mensagem))
# Fim: atualizar_eleitor()

# Deletar eleitor
@app_api.route('/eleitor/<cpf>', methods=['DELETE'])
def deletar_eleitor(cpf):
    try:
        eleitor.deletar_eleitor(cpf)
        sucesso = True
        mensagem = 'Eleitor deletado com sucesso'
    except Exception as ex:
        sucesso = False
        mensagem = f'Erro: {ex}'
    
    return make_response(jsonify(status=sucesso, mensagem=mensagem))
# Fim: deletar_eleitor()

# -- Fim: Serviços da api produto ------------------------
# Levantar/Executar API REST: api_database
app_api.run()