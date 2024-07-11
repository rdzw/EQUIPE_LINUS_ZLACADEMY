# 3, 7, 10, 14

# 7. Dados dois vetores de tamanho N, faça uma função que diga se os mesmos possuem
# conteúdo igual.

vetor_a = []
vetor_b = []

while True:
    print("\n*************************** COMPARAÇÃO DE VETORES ***************************")
    print("1 - Adicionar elemento ao vetor A.\n2 - Adicionar elemento ao vetor B.\n3 - Comparar vetor A e B.\n4 - Sair.")
    print("*****************************************************************************")

    menu = int(input("\nSelecione uma opção acima: "))

    print("---------------------------------------------------------------")

    match menu:
        case 1:
            print("\nOpção 1 selecionada")
            n = int(input("Insira o elemento que será adicionado ao vetor A: "))
            vetor_a.append(n)
            print(f"\nVetor A: {vetor_a}\nVetor B: {vetor_b}")
        case 2:
            print("\nOpção 2 selecionada")
            n = int(input("Insira o elemento que será adicionado ao vetor B: "))
            vetor_b.append(n)
            print(f"\nVetor A: {vetor_a}\nVetor B: {vetor_b}")
        case 3 if len(vetor_a) > 0 and len(vetor_b) > 0:
            print("\nOpção 3 selecionada")
            resultante = set(vetor_a) & set(vetor_b)
            if len(resultante) > 0:
                print(f"Os elementos que se repetem nos dois vetores são: {resultante}")
            else:
                print("Não há nenhum elemento que se repete nos dois vetores.")
        case 4:
            print("\nOpção 4 selecionada")
            print("Saindo do programa....")
            break
        case _:
            if len(vetor_a) > 0 and len(vetor_b) > 0:
                print("Opção inválida, tente novamente.")
            else:
                print("Não é possível acessar essa opção em um vetor vazio.")
            continue