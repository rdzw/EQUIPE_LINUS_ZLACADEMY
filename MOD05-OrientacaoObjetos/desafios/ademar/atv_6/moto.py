from veiculo import Veiculo

class Moto(Veiculo):
    """
    Classe que representa uma moto, herdando de Veículo.

    Atributos:
        marca (str): Marca da moto.
        modelo (str): Modelo da moto.
        cilindradas (int): Cilindradas da moto.
    """
    
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        if isinstance(cilindradas, int) and cilindradas > 0:
            self.__cilindradas = cilindradas
        else:
            raise ValueError("Cilindradas inválidas.")

    def informacao_completa(self):
        """Imprime as informações completas da moto."""
        print(f'Moto: Marca: {self.marca}, Modelo: {self.modelo}, Cilindradas: {self.__cilindradas} cc')
