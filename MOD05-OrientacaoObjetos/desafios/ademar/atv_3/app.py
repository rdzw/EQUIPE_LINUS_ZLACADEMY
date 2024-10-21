from pessoa import Pessoa

# Intânciando um objeto Pessoa
pessoa1 = Pessoa("Ademar", 26, 65, 165)

# Exibir pessoa1
print(f"Nome: {pessoa1.nome} / Idade: {pessoa1.idade} / Peso: {pessoa1.peso} / Altura: {pessoa1.altura}")

# Evelhecer pessoa1
pessoa1.envelhecer(2)

# Crescer pessoa1
pessoa1.crescer(10)

# Engordar pessoa1
pessoa1.engordar(10)

# Emagrecer pessoa1
pessoa1.emagrecer(5)

# Exibir pessoa1
print(f"Nome: {pessoa1.nome} / Idade: {pessoa1.idade} / Peso: {pessoa1.peso} / Altura: {pessoa1.altura}")