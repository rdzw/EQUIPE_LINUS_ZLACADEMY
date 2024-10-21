from cliente import Cliente
from conta import Conta
from movimentacao import Movimentacao

def main():
    clientes = []
    contas = []
    id_mov = 1

    while True:
        print("\nCaixa do Seu Ze:")
        print("1. Criar conta")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Transferir")
        print("5. Mostrar saldo")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            cpf = input("Digite o CPF do cliente: ")
            nome = input("Digite o nome do cliente: ")
            cliente = Cliente(cpf, nome)
            numero = input("Digite o número da conta: ")
            saldo = float(input("Digite o saldo inicial: "))
            conta = Conta(numero, saldo)
            clientes.append(cliente)
            contas.append(conta)
            print(f"Conta criada com sucesso para {nome}!")

        elif choice == "2":
            numero = input("Digite o número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                valor = float(input("Digite o valor do saque: "))
                mov = Movimentacao(id_mov, cliente, conta)
                mov.operacao(valor, "sacar")
                id_mov += 1
            else:
                print("Conta não encontrada.")
        
        elif choice == "3":
            numero = input("Digite o número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                valor = float(input("Digite o valor do depósito: "))
                mov = Movimentacao(id_mov, cliente, conta)
                mov.operacao(valor, "depositar")
                id_mov += 1
            else:
                print("Conta não encontrada.")
        
        elif choice == "4":
            numero_origem = input("Digite o número da conta de origem: ")
            conta_origem = next((c for c in contas if c.numero == numero_origem), None)
            if conta_origem:
                numero_destino = input("Digite o número da conta de destino: ")
                conta_destino = next((c for c in contas if c.numero == numero_destino), None)
                if conta_destino:
                    valor = float(input("Digite o valor da transferência: "))
                    mov = Movimentacao(id_mov, cliente, conta_origem)
                    mov.operacao(valor, "transferir", conta_destino)
                    id_mov += 1
                else:
                    print("Conta de destino não encontrada.")
            else:
                print("Conta de origem não encontrada.")
        
        elif choice == "5":
            numero = input("Digite o número da conta: ")
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                mov = Movimentacao(id_mov, cliente, conta)
                mov.operacao(0, "mostrar saldo")
                id_mov += 1
            else:
                print("Conta não encontrada.")
        
        elif choice == "6":
            print("Obrigado por usar nosso caixa eletrônico!")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
