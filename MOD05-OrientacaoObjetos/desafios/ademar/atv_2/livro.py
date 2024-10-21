class Livro():

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso!")
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nDisponível: {self.disponivel}")
    

