from datetime import datetime

class FormBase:
    """
    Classe que representa um formulário básico.

    Atributos:
        cpf (int): CPF do usuário, deve ser um número inteiro de 11 dígitos.
        nome (str): Nome do usuário.
        data_nascimento (datetime): Data de nascimento do usuário.
    """

    def __init__(self, cpf: int, nome: str, data_nascimento: datetime):
        """
        Inicializa uma nova instância da classe FormBase.

        Args:
            cpf (int): CPF do usuário.
            nome (str): Nome do usuário.
            data_nascimento (datetime): Data de nascimento do usuário.
        """
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self) -> int:
        """
        Retorna o CPF do usuário.

        Returns:
            int: CPF do usuário.
        """
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        """
        Define o CPF do usuário.

        Args:
            cpf (int): CPF do usuário.

        Raises:
            ValueError: Se o CPF não for um número inteiro de 11 dígitos.
        """
        if isinstance(cpf, int) and len(str(cpf)) == 11:
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido. Deve ser um número inteiro de 11 dígitos.")

    @property
    def nome(self) -> str:
        """
        Retorna o nome do usuário.

        Returns:
            str: Nome do usuário.
        """
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        """
        Define o nome do usuário.

        Args:
            nome (str): Nome do usuário.

        Raises:
            ValueError: Se o nome não for uma string não vazia.
        """
        if isinstance(nome, str) and nome:
            self.__nome = nome
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")

    @property
    def data_nascimento(self) -> datetime:
        """
        Retorna a data de nascimento do usuário.

        Returns:
            datetime: Data de nascimento do usuário.
        """
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: datetime):
        """
        Define a data de nascimento do usuário.

        Args:
            data_nascimento (datetime): Data de nascimento do usuário.

        Raises:
            ValueError: Se a data de nascimento não for uma instância de datetime.
        """
        if isinstance(data_nascimento, datetime):
            self.__data_nascimento = data_nascimento
        else:
            raise ValueError("Data de nascimento inválida. Deve ser uma instância de datetime.")
