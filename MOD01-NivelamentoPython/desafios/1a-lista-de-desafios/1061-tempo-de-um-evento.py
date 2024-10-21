'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
'''

id = int(input().split()[1])
h, m, s = map(int, input().split(" : "))
dm = int(input().split()[1])
hh, mm, ss = map(int, input().split(" : "))

total_segundos_inicial = d * 24 * 3600 + h * 3600 + m * 60 + s
total_segundos_final = dm * 24 * 3600 + hh * 3600 + mm * 60 + ss
duracao_segundos = total_segundos_final - total_segundos_inicial

dias = duracao_segundos // (24 * 3600)
duracao_segundos %= (24 * 3600)
horas = duracao_segundos // 3600
duracao_segundos %= 3600
minutos = duracao_segundos // 60
segundos = duracao_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
