import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

print("Oi Mundo")

matA = [10, 25, 32, 71, 57, 13, 29]
for cont in range(len(matA)):
    print(matA[cont])
