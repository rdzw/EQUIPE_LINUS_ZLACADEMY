'''Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e
assim por diante. Imprima os dois vetores.'''

vetor = []

for i in range(10):
    n = int(input(f'Informe o numero da posição {i+1}: '))
    vetor.append(n)

print(f'\nVetor original: {vetor}')

vetor.reverse()

print(f'Vetor invertido: {vetor}')