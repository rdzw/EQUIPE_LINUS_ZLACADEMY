print("Leitor de Artigo!\n")

nome_artigo1 = input("Insira o nome do primeiro Artigo: ")
preco_artigo1 = input("Insira o preco do primeiro Artigo: ")
percentual_artigo1 = input("Insira o percentual de desconto do primeiro Artigo (Ex: 15% = 1.15): ")

nome_artigo2 = input("Insira o nome do segundo Artigo: ")
preco_artigo2 = input("Insira o preco do segundo Artigo: ")
percentual_artigo2 = input("Insira o percentual de desconto do segundo Artigo (Ex: 15% = 1.15): ")

nome_artigo3 = input("Insira o nome do terceiro Artigo: ")
preco_artigo3 = input("Insira o preco do terceiro Artigo: ")
percentual_artigo3 = input("Insira o percentual de desconto do terceiro Artigo (Ex: 15% = 1.15): ")

calculo1 = float(preco_artigo1) * float(percentual_artigo1)
calculo2 = float(preco_artigo2) * float(percentual_artigo2)
calculo3 = float(preco_artigo3) * float(percentual_artigo3)

print(f"O resultado do Artigo {nome_artigo1} com o preço {preco_artigo1} e o percentual de desconto {percentual_artigo1} é: {calculo1}")
print(f"O resultado do Artigo {nome_artigo2} com o preço {preco_artigo2} e o percentual de desconto {percentual_artigo2} é: {calculo2}")
print(f"O resultado do Artigo {nome_artigo3} com o preço {preco_artigo3} e o percentual de desconto {percentual_artigo3} é: {calculo3}")
