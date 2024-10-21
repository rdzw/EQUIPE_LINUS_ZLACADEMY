emprestimo = float(input("Insira o valor do empréstimo: "))
parcelas = int(input("Insira o número de parcelas: "))
salario = float(input("Insira o seu salário: "))

valor_parcelas = emprestimo / parcelas

if valor_parcelas <= salario * 0.30:
    print(f"Parabéns! Seu empréstimo foi aprovado.")
else:
    print(f"Sentimos lhe informar que o seu empréstimo foi recusado.")
