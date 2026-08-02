from datetime import date
from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

anoAtual = date.today().year

anoNasc = int(input("Digite o ano de nascimento: "))

idade = anoAtual - anoNasc

print(f"Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {anoAtual + (18 - idade)}.")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {anoAtual - (idade - 18)}.")
