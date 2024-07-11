'''Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor. Ao
final imprima o vetor armazenado nos dois sentidos.'''

vetor = []

for i in range(3):
    n = int(input(f'Informe um numero, vetor {i+1}: '))
    vetor.append(n)

print(f'Vetor normal: {vetor}')
print(f'Vetor inverso: {vetor[::-1]}')