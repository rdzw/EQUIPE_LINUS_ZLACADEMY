# Importações
from repository import database

# Criar eleitor
def criar_eleitor(eleitor):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"""INSERT INTO eleitor (cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais)
                  VALUES ('{eleitor['cpf']}', '{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}', '{eleitor['cep']}', '{eleitor['nro_endereco']}', '{eleitor['nro_titulo']}', '{eleitor['situacao']}', '{eleitor['secao']}', '{eleitor['zona']}', '{eleitor['local_votacao']}', '{eleitor['endereco_votacao']}', '{eleitor['bairro']}', '{eleitor['municipio_uf']}', '{eleitor['pais']}')"""
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão do eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: criar_eleitor(eleitor)

# Verificar se o eleitor existe
def existe_eleitor(cpf):
    existe = False
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT cpf FROM eleitor WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        if cursor.fetchone():
            existe = True
    except Exception as ex:
        print(f'Erro: Falha na verificação da existência do eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return existe
# Fim: existe_eleitor(cpf)

# Obter eleitor pelo CPF
def obter_eleitor_cpf(cpf):
    eleitor = {}
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            eleitor = {
                'cpf': result[0],
                'nome': result[1],
                'data_nascimento': result[2],
                'nome_mae': result[3],
                'cep': result[4],
                'nro_endereco': result[5],
                'nro_titulo': result[6],
                'situacao': result[7],
                'secao': result[8],
                'zona': result[9],
                'local_votacao': result[10],
                'endereco_votacao': result[11],
                'bairro': result[12],
                'municipio_uf': result[13],
                'pais': result[14]
            }
    except Exception as ex:
        print(f'Erro: Falha ao obter o eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return eleitor
# Fim: obter_eleitor_cpf(cpf)

# Listar eleitores
def listar_eleitor():
    eleitores = []
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = "SELECT * FROM eleitor"
        cursor.execute(sql)
        result = cursor.fetchall()
        for eleitor in result:
            eleitores.append({
                'cpf': eleitor[0],
                'nome': eleitor[1],
                'data_nascimento': eleitor[2],
                'nome_mae': eleitor[3],
                'cep': eleitor[4],
                'nro_endereco': eleitor[5],
                'nro_titulo': eleitor[6],
                'situacao': eleitor[7],
                'secao': eleitor[8],
                'zona': eleitor[9],
                'local_votacao': eleitor[10],
                'endereco_votacao': eleitor[11],
                'bairro': eleitor[12],
                'municipio_uf': eleitor[13],
                'pais': eleitor[14]
            })
    except Exception as ex:
        print(f'Erro: Falha ao listar eleitores: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return eleitores
# Fim: listar_eleitor()

# Atualizar eleitor
def atualizar_eleitor(eleitor):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"""UPDATE eleitor SET nome='{eleitor['nome']}', data_nascimento='{eleitor['data_nascimento']}', nome_mae='{eleitor['nome_mae']}', cep='{eleitor['cep']}', nro_endereco='{eleitor['nro_endereco']}', nro_titulo='{eleitor['nro_titulo']}', situacao='{eleitor['situacao']}', secao='{eleitor['secao']}', zona='{eleitor['zona']}', local_votacao='{eleitor['local_votacao']}', endereco_votacao='{eleitor['endereco_votacao']}', bairro='{eleitor['bairro']}', municipio_uf='{eleitor['municipio_uf']}', pais='{eleitor['pais']}' WHERE cpf='{eleitor['cpf']}'"""
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha ao atualizar eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: atualizar_eleitor(eleitor)

# Deletar eleitor
def deletar_eleitor(cpf):
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"DELETE FROM eleitor WHERE cpf='{cpf}'"
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha ao deletar eleitor: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: deletar_eleitor(cpf)
