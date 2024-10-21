# Prática 3

n1, n2, n3 = map(int, input("Insira 3 números inteiros separados por espaço: ").split())

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        print(f"Os números {n1}, {n2} e {n3} formam um triangulo Equilátero!")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print(f"Os números {n1}, {n2} e {n3} formam um triangulo Isósceles!")
    else:
        print(f"Os números {n1}, {n2} e {n3} formam um triangulo Escaleno!")
else:
    print(f"Os números {n1}, {n2} e {n3} não formam um triangulo!")


numeros = [int(input()) for c in range(5)]
par = 0
impar = 0
positivo = 0
negativo = 0

for numero in numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)")

