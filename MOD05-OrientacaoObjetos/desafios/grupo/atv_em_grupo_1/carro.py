from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diario, combustivel, ar_condicionado, cambio):
        super().__init__(modelo, marca, ano, valor_diario, combustivel)
        self.__ar_condicionado = ar_condicionado
        self.__cambio = cambio

    # Propriedades para encapsulamento
    @property
    def ar_condicionado(self):
        return self.__ar_condicionado

    @ar_condicionado.setter
    def ar_condicionado(self, ar_condicionado):
        self.__ar_condicionado = ar_condicionado

    @property
    def cambio(self):
        return self.__cambio

    @cambio.setter
    def cambio(self, cambio):
        self.__cambio = cambio

    # Método para calcular o valor total de locação
    def calcular_valor_total(self, dias, desconto=0):
        valor = super().calcular_valor_total(dias, desconto)
        if self.cambio == 'automático':
            valor += 50  # Custo adicional para câmbio automático
        if self.ar_condicionado:
            valor += 30  # Custo adicional para ar condicionado
        return max(valor, 0)

    # Método para exibir informações
    def mostrar_informacoes(self):
        info_basica = super().mostrar_informacoes()
        return (f"{info_basica}, Ar Condicionado: {'Sim' if self.ar_condicionado else 'Não'}, "
                f"Câmbio: {self.cambio}")
