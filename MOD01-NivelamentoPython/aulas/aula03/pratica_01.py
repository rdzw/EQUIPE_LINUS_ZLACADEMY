# Crie um programa que receba dois números A e B, em
# seguida exiba um menu para que o usuário possa
# escolher uma operação aritmética:
# 1 - Exibir a soma
# 2 - Exibir a subtração
# 3 - Exibir a multiplicação
# 4 - Exibir a divisão

a, b = map(int, input("Insira dois números separados por espaço: ").split())

print("\n\nOperações Aritméticas:\n1 - Exibir a soma\n2 - Exibir a subtração\n3 - Exibir a multiplicação\n4 - Exibir a divisão")

menu = int(input("\nInsira um número correspondente as opções do menu acima: "))

match menu:
        case 1:
            soma = a + b
            print(f"A soma de {a} e {b} é: {soma}")
        case 2:
            subtracao = a - b
            print(f"A subtração de {a} e {b} é: {subtracao}")
        case 3:
            multiplicacao = a * b
            print(f"A multiplicação de {a} e {b} é: {multiplicacao}")
        case 4:
            divisao = a / b
            print(f"A divisão de {a} e {b} é: {divisao}")
        case _:
            print(f"Valor {menu} não corresponde a uma opção do menu")


# match op:
#     case 0 | 1 | 2:
#         print("Faixa 1 (de 0 a 2)")
#     case 3 | ... 99: ?

# match op:
#     case op if 0 <= op <= 9:
#         print("Faixa 1 (de 0 a 9)")
#     case op if 10 <= op <= 99:
#         print("Faixa 2 (de 10 a 99)")
#     case op if 100 <= op <= 999:
#         print("Faixa 3 (de 100 a 999)")