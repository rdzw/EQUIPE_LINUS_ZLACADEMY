# 3. Ler um vetor de 10 elementos inteiros e positivos. Criar um segundo vetor da seguinte
# forma: os elementos de índice par receberão os respectivos elementos divididos por 2; os
# elementos de índice ímpar receberão os respectivos elementos multiplicados por 3. Imprima
# os dois vetores.

vetor = []
par = []
impar = []

print("Selecione 10 elementos inteiros e positivos.")

for i in range(1, 11):
    n = int(input(f"Insira o {i}° número: "))
    vetor.append(n)

for i in vetor:
    if i % 2 == 0:
        i = i / 2
        par.append(int(i))
    elif i % 2 == 1:
        i = i * 3
        impar.append(i)

print(f"Vetor par: {par}")
print(f"Vetor impar: {impar}")