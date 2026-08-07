from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

for c in range(1, 11):
    for tb in range(1, 11):
        print(f"{c:^3} x {tb:^3} = {c * tb:^3}")
    print("-=" * 10)
