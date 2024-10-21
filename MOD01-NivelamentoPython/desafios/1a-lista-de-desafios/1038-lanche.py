'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
'''

codigo, quantidade = map(int, input().split())
preco_unitario = 0

if codigo == 1:
    preco_unitario = 4.00
elif codigo == 2:
    preco_unitario = 4.50
elif codigo == 3:
    preco_unitario = 5.00
elif codigo == 4:
    preco_unitario = 2.00
elif codigo == 5:
    preco_unitario = 1.50

total = preco_unitario * quantidade
print(f"Total: R$ {total:.2f}")
