'''Ler um vetor de 10 elementos inteiros e positivos. Criar um segundo vetor da seguinte
forma: os elementos de índice par receberão os respectivos elementos divididos por 2; os
elementos de índice ímpar receberão os respectivos elementos multiplicados por 3. Imprima
os dois vetores.'''

vetor_inicial = []
vetor_final = []

for i in range(4):
    n = int(input('Digite um numero: '))
    while n <= 0:
        print('Por favor, informe um numero inteiro e positivo')
        n = int(input('Digite um numero: '))
    vetor_inicial.append(n)
            
for num in vetor_inicial:
    if num % 2 == 0:
        vetor_final.append(num//2)
    else:
        vetor_final.append(num*3)

print(f'Vetor inicial: {vetor_inicial}')
print(f'Vetor final: {vetor_final}')