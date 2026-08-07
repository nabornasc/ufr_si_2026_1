from os import name, system
from time import sleep

cls = lambda: system("cls") if name == "nt" else system("clear")
cls()
print("Contagem regressiva:")
for c in range(10, 0, -1):
    print(f"{c}...")
    sleep(1)
print("Fogo!")
