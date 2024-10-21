class Veiculo:
    """
    Classe que representa um veículo.

    Atributos:
        marca (str): Marca do veículo.
        modelo (str): Modelo do veículo.
    """
    
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        if isinstance(marca, str) and marca:
            self.__marca = marca
        else:
            raise ValueError("Marca inválida.")

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        if isinstance(modelo, str) and modelo:
            self.__modelo = modelo
        else:
            raise ValueError("Modelo inválido.")

    def informacao(self):
        """Imprime as informações do veículo."""
        print(f'Marca: {self.__marca}, Modelo: {self.__modelo}')
