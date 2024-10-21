'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

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
