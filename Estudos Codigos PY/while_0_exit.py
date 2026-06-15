import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

flag = True
somaN = 0

while flag:
    num = int(input(f"Digite um numero para soma [Sair=0]: "))
    somaN += num
    if num == 0:
        flag = False
print(f"O total da soma é: {somaN}")
