
numeros = []

for i in range(1, 6):
    x = int(input("Insira um número inteiro qualquer: "))
    numeros.append(x)

for numero in numeros:
    print(f"{numero}", end=", ")