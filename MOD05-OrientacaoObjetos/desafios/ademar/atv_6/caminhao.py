from veiculo import Veiculo

class Caminhao(Veiculo):
    """
    Classe que representa um caminhão, herdando de Veículo.

    Atributos:
        marca (str): Marca do caminhão.
        modelo (str): Modelo do caminhão.
        capacidade_carga (float): Capacidade de carga do caminhão em toneladas.
    """
    
    def __init__(self, marca, modelo, capacidade_carga):
        super().__init__(marca, modelo)
        self.__capacidade_carga = capacidade_carga

    @property
    def capacidade_carga(self):
        return self.__capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, capacidade_carga):
        if isinstance(capacidade_carga, float) and capacidade_carga > 0:
            self.__capacidade_carga = capacidade_carga
        else:
            raise ValueError("Capacidade de carga inválida.")

    def informacao_completa(self):
        """Imprime as informações completas do caminhão."""
        print(f'Caminhão: Marca: {self.marca}, Modelo: {self.modelo}, Capacidade de carga: {self.__capacidade_carga} toneladas')
