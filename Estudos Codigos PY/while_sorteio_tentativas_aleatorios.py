import random, os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

flag = True
cont = 0

while flag:
    numSort = random.randint(0, 9)
    numDig = int(input("\nDigite um numero de 0 a 9: "))
    if numDig == numSort:
        print("\nParabéns voce acertou o numero sorteado")
        flag = False
    else:
        cls()
        print(f"\nVoce errou! numero sorteado era {numSort}")
        cont += 1
print(f"\nNumero de tentativas: {cont} ")
