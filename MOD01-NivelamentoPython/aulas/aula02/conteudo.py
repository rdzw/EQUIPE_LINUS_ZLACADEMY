# Exemplo 1

x = 1
y = 2

igual = x == y
diferente = x != y

print(f"O valor igual é: {igual}")
print(f"O valor diferente é: {diferente}")

# Exemplo 2

z = 3

print(f"Resultado de x < y < z: {x < y < z}")

maior = x > y
print(f"Resultado de x > y: {maior}")

menor_igual = y <= x
print(f"Resultado de y <= x: {menor_igual}")

# numeroA = input("Insira o primeiro número: ")
# numeroB = input("Insira o segundo número: ")
# numeroA, numeroB = input("Insira o primeiro e o segundo número: ").split()
# split() = Funciona tanto para capturar espaços quanto \n
# int = Transforma apenas 1 item em inteiro, não aceita uma lista
# map(int, ) = Sempre retorna uma lista. Cada elemento da lista vai receber o parametro de transformação para int

# Foco em coleções: Vamos trabalhar mais com isso quando começarmos a manipular dados

numeroA, numeroB = map(int, (input("Insira o primeiro e o segundo número: ").split()))

if numeroA > numeroB:
    print(f"O maior número é o A: {numeroA}")
elif numeroB > numeroA:
    print(f"O maior número é o B: {numeroB}")
else:
    print(f"O numéro A e B são iguais")


# somaAB = int(numeroA) + int(numeroB)
somaAB = numeroA + numeroB
print(f"O resultado da soma de A e B é: {somaAB}")

