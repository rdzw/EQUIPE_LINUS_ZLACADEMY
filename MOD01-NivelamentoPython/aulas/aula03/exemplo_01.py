print("Escolha uma das opções:\n1 - Depositar\n2 - Sacar\n3 - Cancelar")

menu = int(input("Insira um número correspondente as opções do menu acima: "))

match menu:
        case 1:
            print("Operação bem sucedida")
        case 2:
            print("Operação bem sucedida")
        case 3:
            print("Operação bem sucedida")
        case _:
            print(f"Valor {menu} não corresponde a uma opção do menu")