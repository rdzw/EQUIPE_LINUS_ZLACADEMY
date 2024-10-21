from veiculo import Veiculo

class Carro(Veiculo):
    """
    Classe que representa um carro, herdando de Veículo.

    Atributos:
        marca (str): Marca do carro.
        modelo (str): Modelo do carro.
        numero_portas (int): Número de portas do carro.
    """
    
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.__numero_portas = numero_portas

    @property
    def numero_portas(self):
        return self.__numero_portas

    @numero_portas.setter
    def numero_portas(self, numero_portas):
        if isinstance(numero_portas, int) and numero_portas > 0:
            self.__numero_portas = numero_portas
        else:
            raise ValueError("Número de portas inválido.")

    def informacao_completa(self):
        """Imprime as informações completas do carro."""
        print(f'Carro: Marca: {self.marca}, Modelo: {self.modelo}, Número de portas: {self.__numero_portas}')
