from datetime import datetime
from formbase import FormBase

class FormContato(FormBase):
    """
    Classe que representa um formulário de contato, herdando de FormBase.

    Atributos:
        cpf (int): CPF do usuário, herdado de FormBase.
        nome (str): Nome do usuário, herdado de FormBase.
        data_nascimento (datetime): Data de nascimento do usuário, herdado de FormBase.
        telefone (int): Telefone do usuário.
        celular (int): Celular do usuário.
        email (str): Email do usuário.
    """
    
    def __init__(self, cpf: int, nome: str, data_nascimento: datetime, telefone: int, celular: int, email: str):
        """
        Inicializa uma nova instância da classe FormContato.

        Args:
            cpf (int): CPF do usuário.
            nome (str): Nome do usuário.
            data_nascimento (datetime): Data de nascimento do usuário.
            telefone (int): Telefone do usuário.
            celular (int): Celular do usuário.
            email (str): Email do usuário.
        """
        super().__init__(cpf, nome, data_nascimento)
        self.__telefone = telefone
        self.__celular = celular
        self.__email = email

    @property
    def telefone(self) -> int:
        """
        Retorna o telefone do usuário.

        Returns:
            int: Telefone do usuário.
        """
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        """
        Define o telefone do usuário.

        Args:
            telefone (int): Telefone do usuário.

        Raises:
            ValueError: Se o telefone não for um valor inteiro positivo.
        """
        if isinstance(telefone, int) and telefone > 0:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido. Deve ser um valor inteiro positivo.")

    @property
    def celular(self) -> int:
        """
        Retorna o celular do usuário.

        Returns:
            int: Celular do usuário.
        """
        return self.__celular

    @celular.setter
    def celular(self, celular: int):
        """
        Define o celular do usuário.

        Args:
            celular (int): Celular do usuário.

        Raises:
            ValueError: Se o celular não for um valor inteiro positivo.
        """
        if isinstance(celular, int) and celular > 0:
            self.__celular = celular
        else:
            raise ValueError("Celular inválido. Deve ser um valor inteiro positivo.")

    @property
    def email(self) -> str:
        """
        Retorna o email do usuário.

        Returns:
            str: Email do usuário.
        """
        return self.__email

    @email.setter
    def email(self, email: str):
        """
        Define o email do usuário.

        Args:
            email (str): Email do usuário.

        Raises:
            ValueError: Se o email não for uma string válida.
        """
        if isinstance(email, str) and email:
            self.__email = email
        else:
            raise ValueError("Email inválido. Deve ser uma string não vazia.")

# Exemplo de uso
# try:
#     contato = FormContato(12345678901, "Carlos", datetime(2000, 5, 25), 123456789, 987654321, "exemplo@dominio.com")
#     print(contato.cpf)
#     print(contato.nome)
#     print(contato.data_nascimento)
#     print(contato.telefone)
#     print(contato.celular)
#     print(contato.email)
# except ValueError as e:
#     print(e)
