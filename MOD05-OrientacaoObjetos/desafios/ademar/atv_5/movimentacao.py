import datetime
from cliente import Cliente
from conta import Conta

class Movimentacao:
    def __init__(self, id: int, cliente: Cliente, conta: Conta):
        self.id = id
        self.data = datetime.datetime.now().date()
        self.hora = datetime.datetime.now().time()
        self.cliente = cliente
        self.conta = conta

    def operacao(self, valor: float, tipo: str, conta_destino=None):
        if tipo == "sacar":
            self.conta.sacar(valor)
        elif tipo == "depositar":
            self.conta.depositar(valor)
        elif tipo == "transferir" and conta_destino is not None:
            self.conta.transferir(valor, conta_destino)
        elif tipo == "mostrar saldo":
            self.conta.mostrar_saldo()
        else:
            print("Operação inválida.")
