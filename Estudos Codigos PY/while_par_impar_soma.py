import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

flag = True
somaP, somaI = 0, 0

while flag:
    num = int(input("Digite um numero [Sair=0]: "))
    if num == 0:
        flag = False
    elif num % 2 == 0:
        somaP += num
    else:
        somaI += num
print(f"A soma dos Pares digitados é: {somaP}\n A soma dos Impares é: {somaI}")
