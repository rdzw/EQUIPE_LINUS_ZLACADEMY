class Pessoa:
    def __init__(self, nome, idade=0, peso=3.5, altura=50):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")


if __name__ == "__main__":

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em cm: "))

    pessoa = Pessoa(nome, idade, peso, altura)

    pessoa.envelhecer(3)
    pessoa.engordar(5)
    pessoa.emagrecer(2)

    pessoa.mostrar_informacoes()

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em cm: "))

    pessoa = Pessoa(nome, idade, peso, altura)

    pessoa.envelhecer(6)
    pessoa.engordar(10)
    pessoa.emagrecer(4)

    pessoa.mostrar_informacoes()

    pessoa = Pessoa("Maria")

    pessoa.envelhecer(15)
    pessoa.engordar(65)
    pessoa.emagrecer(6)

    pessoa.mostrar_informacoes()