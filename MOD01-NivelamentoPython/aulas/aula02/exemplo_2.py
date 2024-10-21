# Exemplo 2 - Operador Lógico

# Modulo de 2 : % 2

numero = input("Insira um número inteiro qualquer: ")

if float(numero) % 2 != 0 or float(numero) < 0:
    print("Número aceito!")
else:
    print("Número recusado!")