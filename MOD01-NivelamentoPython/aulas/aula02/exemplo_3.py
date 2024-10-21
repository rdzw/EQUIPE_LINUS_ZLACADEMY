# Exemplo 3 - Sem operador lógico

numero = int(input("Insira um número inteiro qualquer: "))

if 0 < numero <= 13:
    print("Criança!")
elif 13 < numero <= 59:
    print("Jovem!")
elif numero >= 60:
    print("Idoso!")