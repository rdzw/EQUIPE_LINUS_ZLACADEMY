'''
Dado um conjunto de números inteiros informados pelo usuário, construa um programa
que calcule a média aritmética dos números pares. O valor de finalização será a entrada do
número 0 e não entrará nos cálculos. Observe que nada impede que o usuário forneça
quantos números ímpares quiser, com a ressalva de que eles não entrarão nos cálculos.
'''

def ler_numeros():
    numeros = []
    while True:
        num = int(input("Digite um número inteiro (ou 0 para finalizar): "))
        if num == 0:
            break
        numeros.append(num)
    return numeros

def calcular_media(numeros):
    soma_pares = 0
    count_pares = 0

    for num in numeros:
        if num % 2 == 0:
            soma_pares += num
            count_pares += 1
    if count_pares == 0:
        return 0 # evitar divisão por zero
    return soma_pares / count_pares
    
def main():
    numeros = ler_numeros()

    while True:
        print("\n1 - Calcular a média dos números pares")
        print("2 - Sair")
    
        opcao = int(input("\nSelecione uma opção: "))

        match opcao: 
            case 1:
                media_pares = calcular_media(numeros)
                if media_pares == 0 and all(num % 2 != 0 for num in numeros):
                    print("Não há números pares no conjunto")
                else:
                    print(f"A média aritmética dos números pares é: {media_pares:.2f}")
            case 2:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")

main()

