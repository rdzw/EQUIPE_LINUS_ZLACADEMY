from atv_em_grupo_1.carro import Carro
from moto import Moto
from caminhao import Caminhao

def main():
    veiculos = []

    while True:
        print("\nSistema de Gerenciamento de Veículos:")
        print("1. Adicionar carro")
        print("2. Adicionar moto")
        print("3. Adicionar caminhão")
        print("4. Mostrar informações dos veículos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        try:
            if escolha == "1":
                marca = input("Digite a marca do carro: ")
                modelo = input("Digite o modelo do carro: ")
                numero_portas = int(input("Digite o número de portas do carro: "))
                carro = Carro(marca, modelo, numero_portas)
                veiculos.append(carro)
                print("Carro adicionado com sucesso!")

            elif escolha == "2":
                marca = input("Digite a marca da moto: ")
                modelo = input("Digite o modelo da moto: ")
                cilindradas = int(input("Digite as cilindradas da moto: "))
                moto = Moto(marca, modelo, cilindradas)
                veiculos.append(moto)
                print("Moto adicionada com sucesso!")
                
            elif escolha == "3":
                marca = input("Digite a marca do caminhão: ")
                modelo = input("Digite o modelo do caminhão: ")
                capacidade_carga = int(input("Digite a capacidade de carga do caminhão: "))
                caminhao = Caminhao(marca, modelo, capacidade_carga)
                veiculos.append(caminhao)
                print("Caminhão adicionado com sucesso!")

            elif escolha == "4":
                for veiculo in veiculos:
                    if isinstance(veiculo, Carro) or isinstance(veiculo, Moto) or isinstance(veiculo, Caminhao):
                        veiculo.informacao_completa()
                    else:
                        veiculo.informacao()

            elif escolha == "5":
                print("Obrigado por usar nosso sistema de gerenciamento de veículos!")
                break

            else:
                print("Opção inválida. Por favor, tente novamente.")
        
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
