# Crie um vetor que armazene 10 números digitados pelo
# usuário e ao final exiba os números pares digitados.

numeros = []

for i in range(1, 11):
    n = int(input("Insira um número inteiro qualquer: "))
    numeros.append(n)

print("Números pares digitados: ", end="")

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero}", end=", ")