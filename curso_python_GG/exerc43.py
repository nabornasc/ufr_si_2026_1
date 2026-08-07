from os import name, system

cls = lambda: system("cls") if name == "nt" else system("clear")

cls()

peso = float(input("Digite o peso da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em metros): "))

imc = peso / (altura**2)
print(f"O IMC da pessoa é: {imc:.1f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")
