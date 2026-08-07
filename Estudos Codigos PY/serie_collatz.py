n = int(input("Digite um número inteiro positivo: "))

print("Sequência de Collatz:")
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(f" → {n}", end="")

print()  