#import database
from repository import database


# Inserir produto
# Inseri um novo produto e retorna o ID
def criar_produto(produto):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO produto(descricao, unidade, quantidade, preco_real, preco_dolar) VALUES('{produto['descricao']}','{produto['unidade']}', '{produto['quantidade']}', '{produto['preco_real']}','{produto['preco_dolar']}')"
        print(sql)
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()


    return last_id
# Fim: criar_produto(produto)


# Atualizar produto
def atualizar_produto(produto):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"UPDATE produto SET descricao = '{produto['descricao']}', unidade = '{produto['unidade']}', quantidade = '{produto['quantidade']}', preco_real = '{produto['preco_real']}', preco_dolar = '{produto['preco_dolar']}' WHERE id = '{produto['id']}' "
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na alteração: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: atualizar_produto(produto)


# Atualizar o preco do campo preco_dolar
def atualizar_preco_dolar(novo_preco):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"UPDATE produto SET preco_dolar = '{novo_preco['preco_dolar']}' WHERE id = '{novo_preco['id']}' "
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na alteracao do preco dolar: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: atualizar_produto(produto)


# Deletar produto pelo id
def deletar_usuario(id):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM produto WHERE id = {id}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: deletar_usuario(id)


# Verificar se o Produto existe
def existe_produto(id):
    existe: False
    # criar uma tupla vazia
    produto = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT id FROM produto WHERE id = '{id}'"
        cursor.execute(sql)
        produto = cursor.fetchone()
        if produto is not None:
            if len(produto) == 1:
                existe = True
            else:
                existe = False
        else:
           existe = False


    except Exception as ex:
        print(f'Erro na verificacao da existencia do produto: {ex}')
    finally:
        cursor.close()
        conect.close()


    return existe
# fim: existe_produto


# Obter o produto pelo id
def obter_produto_id(id):
    # Declar uma tupla vazia
    produto = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM produto WHERE id = '{id}'"
        cursor.execute(sql)
        produto = cursor.fetchone()
    except Exception as ex:
        print(f'Erro na verificacao da existencia do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
    return produto
# fim: obter_produto_id(id)


# Listar todos os produtos ordenados pela descrição
def listar_produto():
    produtos = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM produto ORDER BY descricao'
        cursor.execute(sql)
        lista_produto = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for produto in lista_produto:
            produtos.append(
                {
                  'id': produto[0],
                  'descricao': produto[1],
                  'unidade': produto[2],
                  'quantidade': produto[3],
                  'preco_real': produto[4],
                  'preco_dolar': produto[5]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar produto: {ex}')
    finally:
        cursor.close()
        conect.close()
   
    return produtos
# Fim: lista_produto()
