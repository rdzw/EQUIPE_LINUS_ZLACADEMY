numero = int(input("Insira um número inteiro: "))

if numero == 0:
    print(f"O número {numero} é NEUTRO")
elif numero % 2 == 0:
    print(f"O número {numero} é PAR")
elif numero % 2 != 0:
    print(f"O número {numero} é IMPAR")
    