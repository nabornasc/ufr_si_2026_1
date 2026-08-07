from os import name, system

cls = lambda: system("cls" if name == "nt" else "clear")

cls()

seg1 = float(input("Digite o comprimento da primeira reta: "))
seg2 = float(input("Digite o comprimento da segunda reta: "))
seg3 = float(input("Digite o comprimento da terceira reta: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
    if seg1 == seg2 == seg3:
        print("Tipo de triângulo: EQUILÁTERO")
    elif seg1 != seg2 != seg3 != seg1:
        print("Tipo de triângulo: ESCALENO")
    else:
        print("Tipo de triângulo: ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
