# 10. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
# linhas do chamado triângulo de Floyd. O exemplo abaixo mostra o triângulo de Floyd com 4
# linhas.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 

print("\n*************************** TRIÂNGULO DE FLOYD ***************************")

n = int(input("\nInsira a quantidade de linhas a serem exibidas: "))
m = 1

print("\n")

for i in range(1, n + 1):

    for x in range(1, i + 1):
        print(m, end=" ")
        m += 1
    print()