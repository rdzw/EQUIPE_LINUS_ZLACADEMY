# Crie um programa que simula uma urna eletrônica e
# contabilize os votos para os candidatos A, B, além de
# votos brancos e nulos. O programa deverá ser encerrado
# ao digitar uma opção inválida e deverá exibir o total de
# votos de cada candidato.

a = 0
b = 0
branco = 0
nulo = 0

while True:
    print("\n\nUrna Eletrônica:\n1 - Candidato A\n2 - Candidato B\n3 - Branco\n4 - Nulo\n5 - Sair")

    menu = int(input("\nInsira um número que corresponda as opções acima: "))

    match menu:
        case 1:
            a += 1
            print("Você votou no candidato A")
        case 2:
            b += 1
            print("Você votou no candidato B")
        case 3:
            branco += 1
            print("Você votou Branco")
        case 4:
            nulo += 1
            print("Você votou Nulo")
        case 5:
            break

vencedor = a > b

print("\nPrograma finalizado!")

print("\n********* RESULTADO *********")
if vencedor:
    print(f"O vencedor é o candidato A com: {a}")
    print(f"O candidato B com: {b}")
elif a == b:
    print(f"Empate técnico entre os candidatos A e B com: {a}")
else:
    print(f"O vencedor é o candidato B com: {b}")
    print(f"O candidato A com: {a}")
print(f"Votos Brancos: {branco}")
print(f"Votos Nulos: {nulo}")

a, b = map(int, input("Digite dois números: "))

# maior = (a + b + abs(a - b)) / 2
