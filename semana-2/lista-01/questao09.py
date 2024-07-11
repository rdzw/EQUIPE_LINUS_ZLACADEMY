# # 9. Faça um programa que leia um número inteiro positivo n 
# # e imprima n linhas na tela com o
# # seguinte formato (exemplo se n = 4):
# 1
# 1 2
# 1 2 3
# 1 2 3 4


n = int(input("Digite um numero: "))


for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
           
    print()