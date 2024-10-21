# Novo comentário
"""
    Comentário em bloco
"""
print("Olá mundo!")

# Variáveis: Definição e tipos

# Declarado 4 variáveis e atribuindo valores e elas
var_string = "Hello!"
var_number = 9
var_float = 9.0
var_bool_t = True

# Imprimindo os valores das variáveis
print(var_string)
print(var_number)
print(var_float)
print(var_bool_t)

# Imprimindo os tipos das variáveis
print(type(var_string))
print(type(var_number))
print(type(var_float))
print(type(var_bool_t))

# Convesões de variáveis

print(bool(var_string))
print(int(var_number))
print(int(var_float))
print(str(var_bool_t))

# Operações aritméticas

adicao = var_float + 1
subtracao = var_float - 4
multiplicacao = var_float * 5
divisao = var_float / 5
potencia = var_float ** 2
modulo = var_float % 4
quociente = var_float // 2

# Imprimi as operações aritméticas

print("Adição: " + str(adicao))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
print("Divisão: " + str(divisao))
print("Potenciação: " + str(potencia))
print("Resto da divisão: " + str(modulo))
print("Quociente da divisão: " + str(quociente))

# Incremento e Decremento

var_float -= 2
print("Resultado da atribuição -= 2 é " + str(var_float))

var_float += 5
print("Resultado da atribuição += 5 é " + str(var_float))

# Entrada de dados

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")

# print("Olá " + nome + "!")
# print("Sua idade é " + str(idade))

# Formatação

# %s = string
# %d = int
# %f = float

# print("Olá %s!\nSua idade é %s" % (nome, idade))


# Utilizando a função .format para formatar

# print("Olá {:s}!\nSua idade é {:s}" .format(nome, idade))

# Formatação com f-string

# print(f"Olá {nome}!\nSua idade é {idade}")

# Site para resolver desafios de código
# www.beecrowd.com.br

from time import sleep

for second in range(3, 0, -1):
    print(second)
    sleep(2)
print("Go!")

from time import sleep

for second in range(3, 0, -1):
    print(second, end=" ", flush=True)
    sleep(2)
print("Go!")

# amadeu.neto@ifam.edu.br

