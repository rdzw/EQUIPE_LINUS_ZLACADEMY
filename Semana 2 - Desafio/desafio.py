# Objetivo: Desenvolver competências técnicas na manipulação de
# vetores e listas.
# Você deve escrever um programa que permita ao usuário gerenciar um
# vetor de números inteiros. O programa deve oferecer um menu com as
# seguintes opções:

# Adicionar um número ao vetor.
# Remover um número do vetor.
# Exibir o vetor completo.
# Encontrar e exibir o maior e o menor número no vetor.
# Calcular e exibir a soma de todos os números no vetor.
# Sair.

# Obs: O programa deve continuar exibindo o menu até que o usuário
# escolha a opção de sair.

# Requisitos:
# Utilizar vetores (listas) para armazenar os números inteiros.
# Utilizar laços for para iterar sobre os vetores quando necessário.

vetor = []

while True:
    print("\n*************************** VETORES ***************************")
    print("1 - Adicionar um número ao vetor.\n2 - Remover um número do vetor.\n3 - Exibir o vetor completo.\n4 - Encontrar e exibir o maior e o menor número no vetor.\n5 - Calcular e exibir a soma de todos os números no vetor.\n6 - Sair.")
    print("***************************************************************")

    menu = int(input("\nSelecione uma opção acima: "))

    print("---------------------------------------------------------------")

    match menu:
        case 1:
            print("\nOpção 1 selecionada")

            n = int(input("Insira o número que será adicionado ao vetor: "))
            vetor.append(n)
            print(f"Vetor: {vetor}")
        case 2 if len(vetor) > 0:
            print("\nOpção 2 selecionada")

            print(f"Vetor: {vetor}")
            print("Considere que o primeiro número, da esquerda para a direita, é a posição 0 e assim por diante.")

            x = int(input("\nSelecione a posição do vetor que deseja remover: "))
            print("---------------------------------------------------------------")

            print(f"Posição {x} selecionada.")

            if 0 <= x < len(vetor):
                vetor.pop(x)
                print(f"Vetor após remoção do elemento: {vetor}")
            else:
                print(f"A posição {x} não existe no vetor: {vetor}")
        case 3:
            print("\nOpção 3 selecionada")
            print(f"Vetor completo: {vetor}")
        case 4:
            print("\nOpção 4 selecionada")
        case 5:
            print("\nOpção 5 selecionada")
            soma_total = sum(vetor)
            print(f'A soma de todos os numeros do vetor é: {soma_total}')
        case 6:
            print("\nOpção 6 selecionada")
            break
        case _:
            if len(vetor) > 0:
                print("Opção inválida, tente novamente.")
            else:
                print("Não é possível remover um elemento de um vetor vazio.")
            continue