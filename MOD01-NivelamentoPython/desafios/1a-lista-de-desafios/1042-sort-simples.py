'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

x, y, z = map(int, input().split())

lista = [x, y, z]

lista_ordenada = sorted(lista)

for valor in lista_ordenada:
    print(valor)

print("")

print(x)
print(y)
print(z)
