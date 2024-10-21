# Crie um programa que imprima sequência de fibonacci
# até um um número N digitado pelo usuário.
# Exemplo de entrada: 7
# Saída:
# 1, 1, 2, 3, 5, 8, 13,

# UTILIZANDO LISTA
# n = int(input("Insira um inteiro qualquer: "))
# fibonacci = [1, 1]

# for i in range(len(fibonacci), n, 1):
#     r = fibonacci[-1] + fibonacci[-2]
#     fibonacci.append(r)
# print(f"{fibonacci}")

# UTILIZANDO VARIÁVEL AUX
a, b = 1, 1
aux = 0

n = int(input("Insira um inteiro qualquer: "))

if n > 0:
    print(f"{a}", end=", ")

if n > 1:
    print(f"{a}", end=", ")

if n > 2:
    for i in range(2, n):
        print(f"{a + b}", end=", ")
        aux = b
        b = a + b
        a = aux
    