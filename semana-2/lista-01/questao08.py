# 8. Faça um programa que leia 100 números inteiros. Calcule e imprima a soma dos
# números pares e a soma dos números ímpares.
resultado_par  = 0
resultado_impar = 0

for  i in range(100):
    n = int(input("Digite os numeros: "))

    if n % 2 == 0:
       resultado_par =  resultado_par + n
    elif n % 2 == 1:
        resultado_impar = resultado_impar + n
    else:
        print("Valor invalido !!!")

print(f"Resultado par é: {resultado_par}")
print(f"Resultado impar é: {resultado_impar}")
