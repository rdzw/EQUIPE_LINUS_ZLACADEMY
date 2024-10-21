from livro import Livro

class Livraria():

    def __init__(self, livros: list):
        self.livros = livros
    
    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
    
    def emprestar_livro(self, titulo: str):
        for item in self.livros:
            if item.titulo == titulo:
                item.emprestar()
            else:
                print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def devolver_livro(self, titulo: str):
        for item in self.livros:
            if item.titulo == titulo:
                item.devolver()
            else:
                print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
    def mostrar_inventario(self):
        for item in self.livros:
            item.mostrar_info()
