from datetime import datetime
from formbase import FormBase

class FormEndereco(FormBase):
    """
    Classe que representa um formulário de endereço, herdando de FormBase.

    Atributos:
        cpf (int): CPF do usuário, herdado de FormBase.
        nome (str): Nome do usuário, herdado de FormBase.
        data_nascimento (datetime): Data de nascimento do usuário, herdado de FormBase.
        cep (str): Código postal do endereço.
        rua (str): Nome da rua.
        numero (int): Número do endereço.
        bairro (str): Bairro do endereço.
        cidade (str): Cidade do endereço.
        estado (str): Estado do endereço.
    """
    
    def __init__(self, cpf: int, nome: str, data_nascimento: datetime, cep: str, rua: str, numero: int, bairro: str, cidade: str, estado: str):
        """
        Inicializa uma nova instância da classe FormEndereco.

        Args:
            cpf (int): CPF do usuário.
            nome (str): Nome do usuário.
            data_nascimento (datetime): Data de nascimento do usuário.
            cep (str): Código postal do endereço.
            rua (str): Nome da rua.
            numero (int): Número do endereço.
            bairro (str): Bairro do endereço.
            cidade (str): Cidade do endereço.
            estado (str): Estado do endereço.
        """
        super().__init__(cpf, nome, data_nascimento)
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cep(self) -> str:
        """
        Retorna o CEP do endereço.

        Returns:
            str: CEP do endereço.
        """
        return self.__cep

    @cep.setter
    def cep(self, cep: str):
        """
        Define o CEP do endereço.

        Args:
            cep (str): Código postal do endereço.

        Raises:
            ValueError: Se o CEP não for uma string válida.
        """
        if isinstance(cep, str) and len(cep) == 8:
            self.__cep = cep
        else:
            raise ValueError("CEP inválido. Deve ser uma string de 8 caracteres.")

    @property
    def rua(self) -> str:
        """
        Retorna o nome da rua.

        Returns:
            str: Nome da rua.
        """
        return self.__rua

    @rua.setter
    def rua(self, rua: str):
        """
        Define o nome da rua.

        Args:
            rua (str): Nome da rua.

        Raises:
            ValueError: Se o nome da rua não for uma string válida.
        """
        if isinstance(rua, str) and rua:
            self.__rua = rua
        else:
            raise ValueError("Nome da rua inválido. Deve ser uma string não vazia.")

    @property
    def numero(self) -> int:
        """
        Retorna o número do endereço.

        Returns:
            int: Número do endereço.
        """
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        """
        Define o número do endereço.

        Args:
            numero (int): Número do endereço.

        Raises:
            ValueError: Se o número não for um valor inteiro positivo.
        """
        if isinstance(numero, int) and numero > 0:
            self.__numero = numero
        else:
            raise ValueError("Número inválido. Deve ser um valor inteiro positivo.")

    @property
    def bairro(self) -> str:
        """
        Retorna o bairro do endereço.

        Returns:
            str: Bairro do endereço.
        """
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str):
        """
        Define o bairro do endereço.

        Args:
            bairro (str): Bairro do endereço.

        Raises:
            ValueError: Se o bairro não for uma string válida.
        """
        if isinstance(bairro, str) and bairro:
            self.__bairro = bairro
        else:
            raise ValueError("Bairro inválido. Deve ser uma string não vazia.")

    @property
    def cidade(self) -> str:
        """
        Retorna a cidade do endereço.

        Returns:
            str: Cidade do endereço.
        """
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        """
        Define a cidade do endereço.

        Args:
            cidade (str): Cidade do endereço.

        Raises:
            ValueError: Se a cidade não for uma string válida.
        """
        if isinstance(cidade, str) and cidade:
            self.__cidade = cidade
        else:
            raise ValueError("Cidade inválida. Deve ser uma string não vazia.")

    @property
    def estado(self) -> str:
        """
        Retorna o estado do endereço.

        Returns:
            str: Estado do endereço.
        """
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        """
        Define o estado do endereço.

        Args:
            estado (str): Estado do endereço.

        Raises:
            ValueError: Se o estado não for uma string válida.
        """
        if isinstance(estado, str) and estado:
            self.__estado = estado
        else:
            raise ValueError("Estado inválido. Deve ser uma string não vazia.")

# Exemplo de uso
# try:
#     endereco = FormEndereco(12345678901, "Carlos", datetime(2000, 5, 25), "12345678", "Rua Exemplo", 123, "Bairro Exemplo", "Cidade Exemplo", "Estado Exemplo")
#     print(endereco.cpf)
#     print(endereco.nome)
#     print(endereco.data_nascimento)
#     print(endereco.cep)
#     print(endereco.rua)
#     print(endereco.numero)
#     print(endereco.bairro)
#     print(endereco.cidade)
#     print(endereco.estado)
# except ValueError as e:
#     print(e)
