import os

cls = lambda: os.system("cls" if os.name == "NT" else "clear")

cls()

valorCasa=float(input("Digite o valor da casa: "))
valorSalario=float(input("Digite o valor do seu salário: "))
qtdAnos=int(input("Digite a quantidade de anos que deseja pagar: "))

prestacao=valorCasa/(qtdAnos*12)
minimo=valorSalario*0.3

print(f'Para pagar uma casa de R${valorCasa:,.2f} em {qtdAnos} anos, a prestação será de R${prestacao:,.2f}')
print(f'O valor Maximo da prestação é de R${minimo:,.2f}')

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")