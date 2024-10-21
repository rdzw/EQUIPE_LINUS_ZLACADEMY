#import database
from repository import database


# Inserir usuario
# Inseri um novo usuario e retorna o ID
def criar_usuario(usuario):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO usuario(nome, login, senha, email) VALUES('{usuario['nome']}','{usuario['login']}', '{usuario['senha']}', '{usuario['email']}')"
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusao: {ex}')
    finally:
        cursor.close()
        conect.close()


    return last_id
# Fim: criar_usuario(usuario)


# Atualizar usuario
def atualizar_usuario(usuario):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"UPDATE usuario SET nome = '{usuario['nome']}', login = '{usuario['login']}', senha = '{usuario['senha']}', email = '{usuario['email']}' WHERE id = '{usuario['id']}' "
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na atualizacao: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: atualizar_usuario(usuario)


# Deleta usuário pelo ID
def deletar_usuario(id):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM usuario WHERE id = {id}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do usuario: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: deletar_usuario(id)


# Verificar se o Usuário existe pelo ID
def existe_usuario(id):
    existe: False
    # criar uma tupla vazia
    usuario = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT id FROM usuario WHERE id = '{id}'"
        cursor.execute(sql)
        usuario = cursor.fetchone()
        if usuario is not None:
            if len(usuario) == 1:
                existe = True
            else:
                existe = False
        else:
           existe = False
    except Exception as ex:
        print(f'Erro na verificacao da existencia do usuario: {ex}')
    finally:
        cursor.close()
        conect.close()
    return existe
# fim: existe_usuario


# Obter o usuario pelo id
def obter_usuario_id(id):
    # Declar uma tupla vazia
    usuario = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM usuario WHERE id = '{id}'"
        cursor.execute(sql)
        usuario = cursor.fetchone()
    except Exception as ex:
        print(f'Erro na verificacao da existencia do usuario: {ex}')
    finally:
        cursor.close()
        conect.close()
    return usuario
# fim: obter_usuario_id(id)


# Listar todos os usuarios ordenados pelo nome
def lista_usuarios():
    usuarios = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM usuario ORDER BY nome'
        cursor.execute(sql)
        lista_usuario = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for usuario in lista_usuario:
            usuarios.append(
                {
                  'id': usuario[0],
                  'nome': usuario[1],
                  'login': usuario[2],
                  'senha': usuario[3],
                  'email': usuario[4]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar usuario: {ex}')
    finally:
        cursor.close()
        conect.close()
   
    return usuarios
# Fim: lista_usuarios()
