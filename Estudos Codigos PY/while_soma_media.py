import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

flag = True
cont, soma, media = 0, 0, 0

while flag:
    num = int(input("Digite um numero [Sair=0]: "))
    if num == 0:
        flag = False

    soma += num
    cont += 1

print(
    f"A soma dos números digitados é: {soma}\n A media deu: {soma}/{cont-1} = {soma/(cont-1):.2f}"
)
