# 14. Construa um programa que permita fazer um levantamento do estoque de vinhos de
# uma adega, tendo como dados de entrada tipos de vinho, sendo: “T” para tinto, “B” para
# branco e “R” para rosê. Quando o tipo de vinho for diferente dos apresentados acima,
# mostre a porcentagem de cada tipo de vinho sobre o total geral de vinhos. A quantidade de
# vinhos é desconhecida.

adega = ["T", "T", "T", "T", "T", "T", "B", "B", "B", "B", "B", "B", "B", "T", "T", "T", "T", "T", "T", "T", "T", "R", "R", "R"]

while True:
    print("\n*************************** CONTROLE DE ESTOQUE DE VINHOS ***************************")
    print("T - Vinho tinto.\nB - Vinho branco.\nR - Vinho rosê.\n? - Levantamento geral.\nX - Sair.")
    print("*************************************************************************************")

    menu = input("\nSelecione uma opção acima: ")

    print("---------------------------------------------------------------")

    match menu:
        case "T":
            print("\nOpção T selecionada")
            print(f"\nVinho tinto: {((adega.count("T") / len(adega)) * 100):.2f} %")
        case "B":
            print("\nOpção B selecionada")
            print(f"\nVinho branco: {((adega.count("B") / len(adega)) * 100):.2f} %")
        case "R":
            print("\nOpção R selecionada")
            print(f"\nVinho rosê: {((adega.count("R") / len(adega)) * 100):.2f} %")
        case _:
            print("\nLevantamento geral selecionado")
            print(f"\nVinho tinto: {((adega.count("T") / len(adega)) * 100):.2f} %")
            print(f"\nVinho branco: {((adega.count("B") / len(adega)) * 100):.2f} %")
            print(f"\nVinho rosê: {((adega.count("R") / len(adega)) * 100):.2f} %")
            print(f"\nTotal: {(((adega.count("R") / len(adega)) * 100) + ((adega.count("B") / len(adega)) * 100) + ((adega.count("T") / len(adega)) * 100)):.2f} %")