"""
1 Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor. Ao
final imprima o vetor armazenado nos dois sentidos.
"""

numeros = []

for i in range(10):
    n = int(input("Digite um numero: "))
    numeros.append(n)
    
print("\nValores da lista sentido normal: ", numeros)

print("\nValores da lista em ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i], end=' ')
