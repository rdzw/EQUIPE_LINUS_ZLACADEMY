'''Ler um vetor com 10 nomes de pessoas, após pedir que o usuário digite um nome
qualquer de pessoa. Escrever a mensagem “ACHEI”, se o nome estiver armazenado no
vetor C ou “NÃO ACHEI” caso contrário.'''

vetor_nome = []

for i in range(10):
    n = input('Informe um nome: ')
    vetor_nome.append(n)

nome_procurado = input('\nDigite um nome: ')

if nome_procurado in vetor_nome:
    print('ACHEI')
else:
    print('NÃO ACHEI')
