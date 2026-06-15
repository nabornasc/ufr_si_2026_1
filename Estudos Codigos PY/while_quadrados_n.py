import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

cont = 0
flag = True
while flag:
    mult = cont**2
    if mult < 100:
        print(mult)
    else:
        flag = False
    cont += 1
