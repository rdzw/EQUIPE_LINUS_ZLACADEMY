'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

h1, m1, h2, m2 = map(int, input().split())

if h2 < h1 or (h2 == h1 and m2 <= m1):
    h2 += 24

inicio_em_minutos = h1 * 60 + m1
fim_em_minutos = h2 * 60 + m2
diferenca_em_minutos = fim_em_minutos - inicio_em_minutos

duracao_horas = diferenca_em_minutos // 60
duracao_minutos = diferenca_em_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
