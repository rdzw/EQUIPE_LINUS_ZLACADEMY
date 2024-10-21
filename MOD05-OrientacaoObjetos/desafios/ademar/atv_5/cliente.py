class Cliente:
    def __init__(self, cpf: str, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str) and len(cpf) == 11:
            self.__cpf = cpf
        else:
            print("CPF inválido.")

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
        else:
            print("Nome inválido.")
