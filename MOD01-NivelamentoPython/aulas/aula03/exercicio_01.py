salario = float(input("Insira o seu salário: "))
tempo_servico = int(input("Insira o seu tempo de serviço em anos (Não contabiliza meses): "))

salario_final = 0

if tempo_servico > 5:
    salario_final = salario * 1.20
    print(f"Seu salário é de R$ {salario_final:.2f} após um aumento de 20% graças aos seus mais de 5 anos de serviço. Parabéns!")
else:
    salario_final = salario * 1.10
    print(f"Seu salário é de R$ {salario_final:.2f} após um aumento de 10%. Parabéns!")


