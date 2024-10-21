class Livro():
    ########## INÍCIO MÉTODO CONSTRUTOR ##########
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True
    ########## FIM MÉTODO CONSTRUTOR ##########

    ########## INÍCIO GETTERS AND SETTERS ##########
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and len(novo_titulo) > 0:
            self.__titulo = novo_titulo
        else:
            print("Título inválido.")

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, novo_autor):
        if isinstance(novo_autor, str) and len(novo_autor) > 0:
            self.__autor = novo_autor
        else:
            print("Autor inválido.")

    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, novo_disponivel):
        if isinstance(novo_disponivel, bool):
            self.__disponivel = novo_disponivel
        else:
            print("Disponível inválido.")
    ########## FIM GETTERS AND SETTERS ##########

    ########## INÍCIO MÉTODOS ##########
    def emprestar(self):
        if self.__disponivel:
            self.disponivel(False)
            print(f"O livro {self.titulo()} foi emprestado com sucesso!")

    def devolver(self):
        if not self.__disponivel:
            self.set_disponivel(True)
            print(f"O livro {self.titulo()} foi devolvido com sucesso!")
    
    def mostrar_info(self):
        print(f"Título: {self.titulo()}\nAutor: {self.autor()}\nDisponível: {self.disponivel()}")
    ########## FIM MÉTODOS ##########