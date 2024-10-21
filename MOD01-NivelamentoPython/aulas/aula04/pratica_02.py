# Escreva um programa em Python que receba dois
# números inteiros do usuário, inicio e fim, e calcule a soma
# de todos os números pares no intervalo fechado entre
# esses dois números. O programa deve usar um laço for
# para iterar pelo intervalo e somar os números pares. Ao
# final, o programa deve exibir a soma.

a, b = map(int, input("Insira dois números separados por espaço: ").split())
soma = 0

for i in range(a, b+1, 1):
    if i % 2 == 0:
        soma += i
        # print(f"{i}")

print(f"A soma dos números pares no intervalo fechado é: {soma}")
