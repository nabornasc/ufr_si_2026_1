from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

somaI = 0

for c in range(1, 501):
    if c % 3 == 0:
        somaI = somaI + c
print(
    f"A soma de todos os números múltiplos de 3 no intervalo de 1 a 500 é: {somaI:,.2f}"
)
 