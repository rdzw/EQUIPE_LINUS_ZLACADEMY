'''Faça um programa que calcule N! (fatorial de N), sendo que o valor inteiro de N é
fornecido pelo usuário. Sabe-se que:'''

n = int(input('Digite um numero: '))

resultado = [1] * (n+1)

for i in range (2, n+1):
    resultado[i] = resultado[i - 1] * i

print(f'O fatorial de N é {resultado[n]}')