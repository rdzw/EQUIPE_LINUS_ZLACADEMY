# Crie um programa que exiba o menu:

# 1 - SACAR
# 2 - DEPOSITAR
# 3 - SAIR

# obs: o programa deve estar em loop, e deverá ser
# encerrado ao digitar o número 3. Use Match Case.

while True:
    print("\n\nBanco de Operações:\n1 - SACAR\n2 - DEPOSITAR\n3 - SAIR")

    menu = int(input("\nInsira um número que corresponda as opções acima: "))

    match menu:
        case 1:
            print("Operação de SAQUE bem sucedida")
        case 2:
            print("Operação de DEPOSITO bem sucedida")
        case 3:
            break

print("\nPrograma finalizado!")