numero = input("Insira um número inteiro: ")

# FORMA No 1
# if numero > 0:
#     print(f"O número {numero} é: Positivo")
# elif numero < 0:
#     print(f"O número {numero} é: Negativo")
# else:
#     print(f"O número {numero} é: Neutro")

# FORMA No 2
resultado = ""

if int(numero) > 0:
    resultado = "Positivo"
elif int(numero) < 0:
    resultado = "Negativo"
else:
    resultado = "Neutro"


print(f"O número digitado é {resultado}")