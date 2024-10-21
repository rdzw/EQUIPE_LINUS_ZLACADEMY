'''
Utilizando vetores, crie um programa que organize uma quantidade qualquer de números
inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem
crescente e depois os números ímpares em ordem decrescente.
'''

def ler_numeros():
    numeros = []
    while True:
        num = input("Digite um número inteiro (ou 'sair' para finalizar): ")
        if num.lower() == 'sair':
            break
        numeros.append(int(num))
    return numeros

def organizar_numeros(numeros):
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort(reverse=True)

    return pares + impares

def exibir_vetor(vetor, nome):
    print(f"{nome}: ", vetor)

def main():
    numeros = ler_numeros()
    vetor_organizado = organizar_numeros(numeros)
    exibir_vetor(vetor_organizado, "Vetor")

main()