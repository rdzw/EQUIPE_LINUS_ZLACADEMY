from livro import Livro

class Livraria():
    ########## INÍCIO MÉTODO CONSTRUTOR ##########
    def __init__(self, livros: list):
        self.__livros = livros
    ########## FIM MÉTODO CONSTRUTOR ##########

    ########## INÍCIO GETTERS AND SETTERS ##########
    @property
    def livros(self):
        return self.__livros
    
    @livros.setter
    def livros(self, novo_livro):
        if isinstance(novo_livro, Livro):
            self.__livros.append(novo_livro)
        else:
            print("Livro inválido.")
    ########## FIM GETTERS AND SETTERS ##########

    ########## INÍCIO MÉTODOS ##########
    def adicionar_livro(self, livro: Livro):
        self.set_livros(livro)
    
    def emprestar_livro(self, titulo: str):
        for item in self.livros():
            if item.titulo() == titulo:
                item.emprestar()
            else:
                print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def devolver_livro(self, titulo: str):
        for item in self.livros():
            if item.titulo() == titulo:
                item.devolver()
            else:
                print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def mostrar_inventario(self):
        for item in self.livros():
            item.mostrar_info()
    ########## FIM MÉTODOS ##########
