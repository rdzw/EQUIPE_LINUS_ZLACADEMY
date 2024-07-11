'''Utilizando vetores, crie um programa que organize uma quantidade qualquer de números
inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem
crescente e depois os números ímpares em ordem decrescente.'''

pares = []
impares = []


while True:
    n = int(input('Digite um numero qualquer ou 0 para sair: '))
    if n == 0:
        break
    elif n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

#ordenar pares em ordem crescente
pares.sort()

#ordenar impares em ordem decrescente
impares.sort(reverse=True)

resultado = pares + impares

print(f'\nNumeros organizados: {resultado}')