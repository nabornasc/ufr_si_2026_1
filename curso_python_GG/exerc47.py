from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

print("Números pares de 1 a 50:")
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
