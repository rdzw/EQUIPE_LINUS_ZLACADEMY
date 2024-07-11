'''Faça um programa que leia e monte dois vetores de números inteiros com 20 números
cada. Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores
lidos, um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor
formado pela multiplicação dos dois vetores lidos.'''

vetor_1 = []
vetor_2 = []
vetor_diferenca = [0]*10
vetor_soma = [0]*10
vetor_multiplicacao = [0]*10

for i in range(10):
    n1 = int(input('Digite um numero: '))
    vetor_1.append(n1)

print('\n')
for i in range(10):
    n2 = int(input('Digite um numero: '))
    vetor_2.append(n2)

for i in range(10):
    vetor_diferenca[i] = vetor_1[i] - vetor_2[i]
    vetor_soma[i] = vetor_1[i] + vetor_2[i]
    vetor_multiplicacao[i] = vetor_1[i] * vetor_2[i]

print(f'\nResultado da diferença entre o vetor 1 e vetor 2: {vetor_diferenca}')
print(f'Resultado da soma entre o vetor 1 e vetor 2: {vetor_soma}')
print(f'Resultado da multiplicação entre o vetor 1 e vetor 2: {vetor_multiplicacao}')