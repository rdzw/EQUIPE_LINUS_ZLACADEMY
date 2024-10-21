from formbase import FormBase
from datetime import datetime

class FormLogin(FormBase):
    """
    Classe que representa um formulário de login, herdando de FormBase.

    Atributos:
        usuario (str): Nome de usuário.
        senha (str): Senha do usuário.
    """
    
    def __init__(self, cpf: int, nome: str, data_nascimento: datetime, usuario: str, senha: str):
        """
        Inicializa uma nova instância da classe FormLogin.

        Args:
            cpf (int): CPF do usuário.
            nome (str): Nome do usuário.
            data_nascimento (datetime): Data de nascimento do usuário.
            usuario (str): Nome de usuário.
            senha (str): Senha do usuário.
        """
        super().__init__(cpf, nome, data_nascimento)
        self.__usuario = usuario
        self.__senha = senha

    @property
    def usuario(self) -> str:
        """
        Retorna o nome de usuário.

        Returns:
            str: Nome de usuário.
        """
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: str):
        """
        Define o nome de usuário.

        Args:
            usuario (str): Nome de usuário.

        Raises:
            ValueError: Se o nome de usuário não for uma string não vazia.
        """
        if isinstance(usuario, str) and usuario:
            self.__usuario = usuario
        else:
            raise ValueError("Nome de usuário inválido. Deve ser uma string não vazia.")

    @property
    def senha(self) -> str:
        """
        Retorna a senha do usuário.

        Returns:
            str: Senha do usuário.
        """
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        """
        Define a senha do usuário.

        Args:
            senha (str): Senha do usuário.

        Raises:
            ValueError: Se a senha não for uma string não vazia.
        """
        if isinstance(senha, str) and senha:
            self.__senha = senha
        else:
            raise ValueError("Senha inválida. Deve ser uma string não vazia.")

# Exemplo de uso
# try:
#     login = FormLogin(12345678901, "Carlos", datetime(2000, 5, 25), "usuario_exemplo", "senha123")
#     print(login.cpf)
#     print(login.nome)
#     print(login.data_nascimento)
#     print(login.usuario)
#     print(login.senha)
# except ValueError as e:
#     print(e)
