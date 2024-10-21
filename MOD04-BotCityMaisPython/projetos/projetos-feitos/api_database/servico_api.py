# Importações
from flask import Flask, make_response, jsonify, request, Response
from repository import eleitor, usuario

# Instanciar
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# --------------------------------------------------------
#           Inicio: Serviços da api eleitor
# --------------------------------------------------------

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

# -- Fim: Serviços da api eleitor ------------------------


# --------------------------------------------------------
#           Inicio: Serviços da api usuário
# --------------------------------------------------------


# Inserir usuário
@app_api.route('/usuario', methods=['POST'])
def criar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id_usuario=0
    try:
        id_usuario = usuario.criar_usuario(usuario_json)
        sucesso = True
        _mensagem = 'Usuario inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do usuario: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_usuario
        )
    )
# Fim: criar_usuario()


# Atualizar usuário
@app_api.route('/usuario', methods=['PUT'])
def atualizar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id = int(usuario_json['id'])
    try:
        if usuario.existe_usuario(id) == True:
            usuario.atualizar_usuario(usuario_json)
            sucesso = True
            _mensagem = 'Usuario alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteracao do usuario: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )


# Deletar usuário
@app_api.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        if usuario.existe_usuario(id) == True:
            usuario.deletar_usuario(id)
            sucesso = True
            _mensagem = 'Usuario deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de usuario: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )


# Serviço: Obter usuário pelo id
@app_api.route('/usuario/<int:id>', methods=['GET'])
def obter_usuario_id(id):
    # Declarando uma tupla vazia
    usuario_id = ()
    sucesso = False
    if usuario.existe_usuario(id) == True:
        usuario_id = usuario.obter_usuario_id(id)
        sucesso = True
        _mensagem = 'Usuario encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Usuario existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem,
                dados = usuario_id
        )
    )
# Fim: obter_usuario_id(id)


# Serviço: Obter a lista de usuário
@app_api.route('/usuario', methods=['GET'])
def lista_usuarios():
    lista_usuario = list()
    lista_usuario = usuario.lista_usuarios()
    if len(lista_usuario) == 0:
        sucesso = False
        _mensagem = 'Lista de usuario vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de usuario'


    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem,
                dados = lista_usuario
        )
    )
# Fim: lista_usuarios()


# -- Fim: Serviços da api usuário ------------------------

# Levantar/Executar API REST: api_database
app_api.run()