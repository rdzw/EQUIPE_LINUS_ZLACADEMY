from livro import Livro
from livraria import Livraria

def main():
    livros = []
    livraria = Livraria(livros)

    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            livraria.adicionar_livro(livro)
            print(f"Livro '{titulo}' por {autor} adicionado com sucesso!")
        elif choice == "2":
            livraria.mostrar_inventario()
        elif choice == "3":
            titulo = input("Digite o título do livro para emprestar: ")
            livraria.emprestar_livro(titulo)
        elif choice == "4":
            titulo = input("Digite o título do livro para devolver: ")
            livraria.devolver_livro(titulo)
        elif choice == "5":
            print("Obrigado por usar nossa biblioteca!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()