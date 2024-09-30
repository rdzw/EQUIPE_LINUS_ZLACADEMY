from flask import Flask, make_response, jsonify, request, Response
import mysql.connector
import sys
import os


# Atualizar o path do projeto para localizar os módulos da pasta
# repository
#modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
# sys.path.append(modulo)




#from repository.usuario import *
#from repository.produto import *


import repository.produto as produto
import repository.usuario as usuario


#import usuario as usuario


#import usuario
#import produto


# Instanciar
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False


# Implementar a lógica de programação


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




# --------------------------------------------------------
#           Inicio: Serviços da api produto
# --------------------------------------------------------


# Incluir um novo Produto
@app_api.route('/produto', methods=['POST'])
def criar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    produto_json = request.json # corpo da requisição
    id_produto=0
    try:
        id_produto = produto.criar_produto(produto_json)
        sucesso = True
        _mensagem = 'Produto inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do produto: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_produto
        )
    )


# Alterar um Produto
@app_api.route('/produto', methods=['PUT'])
def atualizar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    produto_json = request.json # corpo da requisição
    id = int(produto_json['id'])
    try:
        if produto.existe_produto(id) == True:
            atualizar_produto(produto_json)
            sucesso = True
            _mensagem = 'Produto alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Falha na alteracao do produto: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )
# Fim: atualizar_produto()


# Alterar o preco do dolar do Produto
@app_api.route('/produto/preco_dolar', methods=['PUT'])
def atualizar_preco_dolar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    novo_preco_dolar_json = request.json # corpo da requisição
    id = int(novo_preco_dolar_json['id'])
    try:
        if produto.existe_produto(id) == True:
            produto.atualizar_preco_dolar(novo_preco_dolar_json)
            sucesso = True
            _mensagem = 'Preco do dolar do Produto alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Falha na alteracao do preco do dolar do produto: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )
# Fim: atualizar_produto()


# Deletar produto pelo id
@app_api.route('/produto/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        if produto.existe_produto(id) == True:
            deletar_produto(id)
            sucesso = True
            _mensagem = 'Produto deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusão de usuario: {ex}'
   
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )
# Fim: deletar_produto(id)  


# Serviço: Obter produto pelo id
@app_api.route('/produto/<int:id>', methods=['GET'])
def obter_produto_id(id):
    # Declarando uma tupla vazia
    produto_id = ()
    sucesso = False
    if produto.existe_produto(id) == True:
        produto_id = obter_produto_id(id)
        sucesso = True
        _mensagem = 'Produto encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Produto nao existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem,
                dados = produto_id
        )
    )
# Fim: obter_produto_id(id)


# Serviço: Obter uma lista de produtos ordenada pela descricao
@app_api.route('/produto', methods=['GET'])
def lista_produtos():
    lista_produto = list()
    lista_produto = produto.listar_produto()
    if len(lista_produto) == 0:
        sucesso = False
        _mensagem = 'Lista de produto vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de produto'


    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem,
                dados = lista_produto
        )
    )
# Fim: lista_produtos()


# -- Fim: Serviços da api produto ------------------------
# Levantar/Executar API REST: api_database
app_api.run()
