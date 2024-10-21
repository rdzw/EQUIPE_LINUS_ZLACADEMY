banana = {'item': 'banana', 'quantidade': 2, 'valor': 10.0}
laranja = {'item': 'laranja', 'quantidade': 3, 'valor': 20.0}

vendas = [banana, laranja]

def adicionar_vendas():
    item = input('Digite o nome do item: ')
    quantidade = int(input('Informe a quantidade do item vendido: '))
    valor = float(input('Informe o valor unitário do item: '))
    venda = {'item': item, 'quantidade': quantidade, 'valor': valor}
    vendas.append(venda)

def listar_vendas():
    for venda in vendas:
        print(venda)

def exibir_total_vendas():
    total = sum(venda['valor'] * venda['quantidade'] for venda in vendas)
    print(f"Valor total de vendas: R$ {total:.2f}")
    return total

def media_vendas():
    if vendas:
        total = 0
        media = 0
        for venda in vendas:
            total += venda['quantidade'] * venda['valor']
            media = total / len(vendas)

        print(f'Média das vendas: R${media:.2f}')
    else:
        print('Nenhuma venda registrada')

def maior_venda():
    if vendas:
        maior = vendas[0]
        for venda in vendas:
            if venda["quantidade"] * venda["valor"] > maior["quantidade"] * maior["valor"]:
                maior = venda
        valor = maior["quantidade"] * maior["valor"]
        print(f"Maior venda: {maior['item']} - R${valor:.2f}")
    else:
        print("Nenhuma venda registrada.")

def item_mais_vendido():
    if not vendas:
        print("Nenhuma venda registrada")

    itens_vendidos = {}
    for venda in vendas:
        item = venda['item']
        quantidade = venda['quantidade']
        if item in itens_vendidos:
            itens_vendidos[item] += quantidade
        else: 
            itens_vendidos[item] = quantidade
    item_mais_vendido = max(itens_vendidos, key=itens_vendidos.get)
    print(f"Item mais vendido: {item_mais_vendido}, Quantidade vendida: {itens_vendidos[item_mais_vendido]}")

def main():
    while True:
        print("**** MENU ****")
        print("1 - Listar vendas\n2 - Adicionar venda\n3 - Exibir o valor total de vendas\n4 - Exibir a média de vendas\n5 - Exibir a maior venda\n6 - Exibir o item mais vendido\n7 - Sair")
        op = int(input('Escolha uma opção: '))

        if op == 1:
            listar_vendas()
        elif op == 2:
            adicionar_vendas()
        elif op == 3:
            exibir_total_vendas()
        elif op == 4:
            media_vendas()
        elif op == 5:
            maior_venda()
        elif op == 6:
            item_mais_vendido()
        elif op == 7:
            break
        
        print('\n')

if __name__ == '__main__':
    main()