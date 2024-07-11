# 13. Uma loja utiliza o código “V” para transação à vista e “P” para transação à prazo. Faça
# um programa que receba o código e o valor das transações. Quando o código for diferente
# de “V” ou “P”, calcule e mostre:

# a. O valor das compras à vista;
# b. O valor das compras a prazo;
# c. O valor total das compras efetuadas.

valor_trans = 0
valor_prazo = 0

while(True):

    codigo = input("Digite o codigo: ")
    

    if codigo == 'V':
        valor = float(input("Digite o valor da transação: "))
        valor_trans = valor_trans + valor
        print(f"O valor das compras à vista é {valor_trans}")
    elif codigo == 'P':
        valor = float(input("Digite o valor da transação: "))
        valor_prazo = valor_prazo + valor
        print(f"O valor das compras a prazo é {valor_prazo}")
    else:
        print("Codigo Invalido !!!")
    
    valor_total = valor_trans + valor_prazo
    print(f"O valor total das compras efetuadas é R$ {valor_total}")







