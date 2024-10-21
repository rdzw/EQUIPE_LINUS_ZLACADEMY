# Crie um programa que imprima a tabuada de
# multiplicação de um número N digitado pelo usuário.
# Exemplo de entrada: 8
# Saída:
# 1 x 8 = 8
# 2 x 8 = 16
# ...
# 10 x 8 = 80

print("******* TABUADA *******")
n = int(input("Insira um número: "))

for i in range(1, 11, 1):
    print(f"{i} x {n} = {i*n}")