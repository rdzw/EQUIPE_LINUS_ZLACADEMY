class Veiculo:
    total_veiculos = 0

    def __init__(self, modelo, marca, ano, valor_diario, combustivel):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__valor_diario = valor_diario
        self.__combustivel = combustivel
        Veiculo.total_veiculos += 1

    # Propriedades para encapsulamento
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def valor_diario(self):
        return self.__valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel

    # Método para exibir informações
    def mostrar_informacoes(self):
        return (f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, "
                f"Combustível: {self.combustivel}, Valor Diário: R${self.valor_diario:.2f}")

    # Método para calcular o valor total de locação
    def calcular_valor_total(self, dias, desconto=0):
        valor = self.__valor_diario * dias
        if self.__combustivel == 'gasolina':
            valor *= 0.95  # 5% de desconto para gasolina
        if dias > 7:
            valor *= 0.90  # 10% de desconto para mais de 7 dias
        valor -= desconto
        return max(valor, 0)

    @classmethod
    def total_veiculos_cadastrados(cls):
        return cls.total_veiculos

    @classmethod
    def aplicar_aumento(cls, percentual, frota):
        for veiculo in frota:
            novo_valor = veiculo.valor_diario * (1 + percentual / 100)
            veiculo.valor_diario = novo_valor
