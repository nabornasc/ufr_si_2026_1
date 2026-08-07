from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

somaP = 0

for c in range(6):
    num = int(input(f"Digite o {c + 1}º número: "))
    if num % 2 == 0:
        somaP = somaP + num
print(f"A soma dos números pares digitados é: {somaP}")
