# Crie um programa que leia N notas de um aluno. O valor
# das notas deverá ser de 0 a 10. O programa deverá ser
# parado ao ser digitado um número negativo e deverá
# imprimir a média das notas digitadas.

print("***************** SIGAA *****************")

# UTILIZANDO MATCH

soma = 0
qtd_notas = 0

while True:
    menu = float(input("\nInsira uma nota de 0 a 10 para o aluno: "))

    match menu:
        case menu if 0 <= menu <= 10:
            qtd_notas += 1
            soma += menu
        case menu if menu > 10:
            continue
        case menu if menu < 0:
            break

media =  soma / qtd_notas

print("\nPrograma finalizado!")

print(f"A média do aluno foi de {media:.2f}")

# UTILIZANDO LISTA

# notas = []
# soma = 0

# while True:
#     notas.append (int(input("\nInsira uma nota de 0 a 10 para o aluno: ")))

#     if notas[-1] < 0:
#         notas.pop()
#         break

# for nota in notas:
#     soma += nota

# media =  soma / len(notas)

# print("\nPrograma finalizado!")

# print(f"A média do aluno foi de {media}")