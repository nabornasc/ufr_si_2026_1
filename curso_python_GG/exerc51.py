from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

priTerm = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

pa = []
for c in range(10):
    pa.append(priTerm + c * razao)
print("-=" * 10)
print("Os 10 primeiros termos da PA são:")
for term in pa:
    print(term, end=" ")
print()
print("-=" * 10)
