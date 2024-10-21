# Exemplo 1 - Operador Lógico

nota, frequencia = input("Insira a nota e a frequência do aluno: ").split()

if float(nota) >= 7.5 and int(frequencia) >= 75:
    print("APROVADO!")
else:
    print("REPROVADO!")


a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print(f"{c}\n{b}\n{a}\n\n{a}\n{b}\n{c}")
elif a > c > b:
    print(f"{b}\n{c}\n{a}\n\n{a}\n{b}\n{c}")
elif b > a > c:
    print(f"{c}\n{a}\n{b}\n\n{a}\n{b}\n{c}")
elif b > c > a:
    print(f"{a}\n{c}\n{b}\n\n{a}\n{b}\n{c}")
elif c > a > b:
    print(f"{b}\n{a}\n{c}\n\n{a}\n{b}\n{c}")
else:
    print(f"{a}\n{b}\n{c}\n\n{a}\n{b}\n{c}")