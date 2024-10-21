from veiculo import Veiculo
from carro import Carro
from moto import Moto
from sistemaaluguel import SistemaAluguel

def menu():
    sistema = SistemaAluguel()

    while True:
        print("\nMenu do Sistema de Aluguel de Veículos")
        print("1. Adicionar Carro")
        print("2. Adicionar Moto")
        print("3. Mostrar Frota")
        print("4. Calcular Valor do Aluguel")
        print("5. Aplicar Aumento no Valor Diário de Todos os Veículos")
        print("6. Mostrar Total de Veículos Cadastrados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            modelo = input("Digite o modelo do carro: ")
            marca = input("Digite a marca do carro: ")
            ano = int(input("Digite o ano do carro: "))
            valor_diario = float(input("Digite o valor diário de aluguel: "))
            combustivel = input("Digite o tipo de combustível (gasolina/flex): ").lower()
            ar_condicionado = input("Possui ar condicionado? (s/n): ").lower() == 's'
            cambio = input("Digite o tipo de câmbio (manual/automático): ").lower()

            carro = Carro(modelo, marca, ano, valor_diario, combustivel, ar_condicionado, cambio)
            sistema.adicionar_veiculo(carro)
            print("Carro adicionado com sucesso!")

        elif opcao == '2':
            modelo = input("Digite o modelo da moto: ")
            marca = input("Digite a marca da moto: ")
            ano = int(input("Digite o ano da moto: "))
            valor_diario = float(input("Digite o valor diário de aluguel: "))
            combustivel = input("Digite o tipo de combustível (gasolina/flex): ").lower()
            cilindrada = int(input("Digite a cilindrada da moto: "))

            moto = Moto(modelo, marca, ano, valor_diario, combustivel, cilindrada)
            sistema.adicionar_veiculo(moto)
            print("Moto adicionada com sucesso!")

        elif opcao == '3':
            sistema.mostrar_frota()

        elif opcao == '4':
            sistema.mostrar_frota()
            index = int(input("Digite o índice do veículo para calcular o aluguel (começando do 0): "))
            dias = int(input("Digite o número de dias do aluguel: "))
            desconto = float(input("Digite o valor do desconto (se houver): "))

            if 0 <= index < len(sistema.frota):
                veiculo = sistema.frota[index]
                valor_aluguel = sistema.calcular_valor_total_aluguel(veiculo, dias, desconto)
                print(f"Valor total do aluguel: R${valor_aluguel:.2f}")
            else:
                print("Índice de veículo inválido.")

        elif opcao == '5':
            percentual = float(input("Digite o percentual de aumento no valor diário (%): "))
            sistema.aplicar_aumento(percentual, sistema.frota)
            print(f"Aumento de {percentual}% aplicado com sucesso a todos os veículos!")

        elif opcao == '6':
            print(f"Total de veículos cadastrados: {Veiculo.total_veiculos_cadastrados()}")

        elif opcao == '0':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")


# Executar o menu
menu()