class Usuario:
    numeros_de_usuarios = 0  # Atributo da classe para contar o número de usuários

    def __init__(self, peso, altura):
        # Validar e inicializar peso e altura
        try:
            self.peso = float(peso)
            self.altura = float(altura) / 100  # Converter altura de cm para metros
            Usuario.numeros_de_usuarios += 1  # Incrementa o contador de usuários
        except ValueError:
            print("Por favor, insira valores válidos para peso e altura.")
            self.peso = 0
            self.altura = 1  # Evitar divisão por zero
    
    @property
    def peso(self):
        return self._idade


    @classmethod
    def total_de_usuarios(cls):
        print(f"Total de usuários cadastrados: {cls.numeros_de_usuarios}")

    def calcular_imc_usuario(self):
        try:
            imc = self.peso / (self.altura ** 2)
            return round(imc, 2)
        except ZeroDivisionError:
            return "Altura não pode ser zero."

    def classificar_imc(self):
        imc = self.calcular_imc_usuario()

        if isinstance(imc, str):  # Em caso de erro no cálculo (altura zero)
            return imc

        # Classificação com base nas faixas do IMC
        if imc < 18.5:
            return f"IMC: {imc} - Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return f"IMC: {imc} - Peso normal"
        elif 25 <= imc < 29.9:
            return f"IMC: {imc} - Sobrepeso"
        elif 30 <= imc < 34.9:
            return f"IMC: {imc} - Obesidade Grau 1"
        elif 35 <= imc < 39.9:
            return f"IMC: {imc} - Obesidade Grau 2"
        else:
            return f"IMC: {imc} - Obesidade Grau 3"
        
    
