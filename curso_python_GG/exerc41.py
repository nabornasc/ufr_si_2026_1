from datetime import date
from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

anoAtual = date.today().year

anoNasc = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNasc

print(f"Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.")

if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÚNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")

