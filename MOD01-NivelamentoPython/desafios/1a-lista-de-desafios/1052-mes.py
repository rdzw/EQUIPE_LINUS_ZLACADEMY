'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.
'''

num_mes = int(input())

if num_mes == 1:
    nome_mes = "January"
elif num_mes == 2:
    nome_mes = "February"
elif num_mes == 3:
    nome_mes = "March"
elif num_mes == 4:
    nome_mes = "April"
elif num_mes == 5:
    nome_mes = "May"
elif num_mes == 6:
    nome_mes = "June"
elif num_mes == 7:
    nome_mes = "July"
elif num_mes == 8:
    nome_mes = "August"
elif num_mes == 9:
    nome_mes = "September"
elif num_mes == 10:
    nome_mes = "October"
elif num_mes == 11:
    nome_mes = "November"
elif num_mes == 12:
    nome_mes = "December"
else:
    nome_mes = ""

print(nome_mes)
