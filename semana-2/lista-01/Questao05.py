'''
Faça um programa que leia e monte dois vetores de números inteiros com 20 números
cada. Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores
lidos, um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor
formado pela multiplicação dos dois vetores lidos.
'''

def montar_vetores():
    vetor1 = []
    vetor2 = []

    # Leitura dos vetores
    print("Digite 20 números inteiros para o primeiro vetor:")
    for i in range(20):
        num = int(input(f"Número {i+1}: "))
        vetor1.append(num)

    print("Digite 20 números inteiros para o segundo vetor:")
    for i in range(20):
        num = int(input(f"Número {i+1}: "))
        vetor2.append(num)

    return vetor1, vetor2

def calcular_diferenca(vetor1, vetor2):
    vetor_diferenca = []
    for i in range(20):
        vetor_diferenca.append(vetor1[i] - vetor2[i])
    return vetor_diferenca

def calcular_soma(vetor1, vetor2):
    vetor_soma = []
    for i in range(20):
        vetor_soma.append(vetor1[i] + vetor2[i])
    return vetor_soma

def calcular_multiplicacao(vetor1, vetor2):
    vetor_multiplicacao = []
    for i in range(20):
        vetor_multiplicacao.append(vetor1[i] * vetor2[i])
    return vetor_multiplicacao

def exibir_vetores(vetor, nome):
    print(f"{nome}: ", vetor)

def main():
    vetor1, vetor2 = montar_vetores()
    
    vetor_diferenca = calcular_diferenca(vetor1, vetor2)
    vetor_soma = calcular_soma(vetor1, vetor2)
    vetor_multiplicacao = calcular_multiplicacao(vetor1, vetor2)
    
    exibir_vetores(vetor1, "Vetor 1")
    exibir_vetores(vetor2, "Vetor 2")
    exibir_vetores(vetor_diferenca, "Vetor diferença")
    exibir_vetores(vetor_soma, "Vetor soma")
    exibir_vetores(vetor_multiplicacao, "Vetor multiplicação")

main()