class Conta:
    def __init__(self, numero: str, saldo: float):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def numero(self) -> str:
        return self.__numero

    @numero.setter
    def numero(self, numero: str):
        if isinstance(numero, str) and len(numero) == 8:
            self.__numero = numero
        else:
            print("Número inválido.")

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float):
        if isinstance(saldo, float) and saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo inválido.")

    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saque inválido.")

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
        else:
            print("Depósito inválido.")

    def transferir(self, valor: float, conta_destino):
        if valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
        else:
            print("Transferência inválida.")

    def mostrar_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")
