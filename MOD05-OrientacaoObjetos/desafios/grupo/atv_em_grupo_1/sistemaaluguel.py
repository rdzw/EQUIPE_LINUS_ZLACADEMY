class SistemaAluguel:
    def __init__(self):
        self.frota = []

    # Método para adicionar um veículo à frota
    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)

    # Método para mostrar informações de todos os veículos da frota
    def mostrar_frota(self):
        for veiculo in self.frota:
            print(veiculo.mostrar_informacoes())

    # Método para calcular o valor total de aluguel de um veículo
    def calcular_valor_total_aluguel(self, veiculo, dias, desconto=0):
        return veiculo.calcular_valor_total(dias, desconto)

    # Método para aplicar aumento no valor diário de todos os veículos da frota
    def aplicar_aumento(self, percentual, frota):
        for veiculo in frota:
            novo_valor = veiculo.valor_diario * (1 + percentual / 100)
            veiculo.valor_diario = novo_valor
