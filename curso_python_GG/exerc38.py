from os import name, system

cls = lambda: system("cls") if name == "nt" else system("clear")

cls()

priNum = int(input("Digite o 1º número: "))
segNum = int(input("Digite o 2º número: "))

if priNum == segNum:
    print("Os números são iguais.")
elif priNum > segNum:
    print("O 1º número é maior que o 2º número.")
else:
    print("O 2º número é maior que o 1º número.")
