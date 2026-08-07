from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"O número {num} não é primo")
            break
    else:
        print(f"O número {num} é primo")



