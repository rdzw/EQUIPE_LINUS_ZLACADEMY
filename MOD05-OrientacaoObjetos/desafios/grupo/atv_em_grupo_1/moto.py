from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diario, combustivel, cilindrada):
        super().__init__(modelo, marca, ano, valor_diario, combustivel)
        self.__cilindrada = cilindrada

    # Propriedade para encapsulamento
    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    # Método para calcular o valor total de locação
    def calcular_valor_total(self, dias, desconto=0):
        valor = super().calcular_valor_total(dias, desconto)
        if self.cilindrada > 200:
            valor += 20  # Custo adicional para cilindrada maior que 200cc
        return max(valor, 0)

    # Método para exibir informações
    def mostrar_informacoes(self):
        info_basica = super().mostrar_informacoes()
        return f"{info_basica}, Cilindrada: {self.cilindrada}cc"
