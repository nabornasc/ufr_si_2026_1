import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

fat = int(input("Calculo de Fatorial, digite um numero inteiro: "))
cont = fat
multF = 1
while cont >= 1:
    print(f"{cont}!")
    multF *= cont
    cont -= 1
print(f"O fatorial de {fat} é {multF}")
