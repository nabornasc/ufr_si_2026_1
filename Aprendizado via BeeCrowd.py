# Aprendizado via BeeCrowd


# raio=float(input())

# pi=3.14159

# area=pi*raio**2

# print(f'A={area:.4f}')

# ==============================

# A=int(input())
# B=int(input())

# soma=A+B

# print(f'SOMA = {soma}')

# ===============================


# valor1=int(input())
# valor2=int(input())

# prod=valor1*valor2

# print(f'PROD = {prod}')

# =================================

# a=float(input())*3.5
# b=float(input())*7.5

# media=(a+b)/11

# print(f'MEDIA = {media:.5f}')

# =================================

# a=float(input())*2
# b=float(input())*3
# c=float(input())*5

# media=(a+b+c)/10

# print(f'MEDIA = {media:.1f}')

# =================================

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())

# diferenca=(a*b-c*d)

# print(f'DIFERENCA = {diferenca}')

# =================================

# numFuncionario=int(input())
# numHorasTrab=int(input())
# valorPorHoras=float(input())

# salario=numHorasTrab*valorPorHoras

# print(f'NUMBER = {numFuncionario}')
# print(f'SALARY = {salario:.2f}')

# =================================

# nomeVendedor=str(input())
# salarioFixo=float(input())
# totalVendas=float(input())*0.15

# total=salarioFixo+totalVendas

# print(f'TOTAL = R$ {total:.2f}')

# =================================

# codigoPeca1, numPeca1, valorPeca1 = input().split()
# codigoPeca2, numPeca2, valorPeca2 = input().split()

# fatura = int(numPeca1) * float(valorPeca1) + int(numPeca2) * float(valorPeca2)

# print(f'VALOR A PAGAR: R$ {fatura:.2f}')

# codigoPeca1=int(input())
# numPeca1=int(input())
# valorPeca1=float(input())

# codigoPeca2=int(input())
# numPeca2=int(input())
# valorPeca2=float(input())

# fatura=(numPeca1*valorPeca1)+(numPeca2*valorPeca2)

# print(f'VALOR A PAGAR: R$ {fatura:.2f}')

# =================================

# r=float(input())**3

# pi=3.14159

# volume=(4/3)*pi*r

# print(f'VOLUME = {volume:.3f}')

# =================================

# try:
#     a, b, c = input().split()
#     a,b,c = float(a,b,c)
#     # b = float(b)
#     # c = float(c)
# except ValueError as e:
#     print(f"Erro: Entrada inválida. Esperava 3 números separados por espaço. Detalhes: {e}")
#     exit()

# pi = 3.14159

# triaguloretangulo = a*c/2
# areaCirculo = pi*c**2
# areaTrapezio = (a+b)*c/2
# areaQuadrado = b**2
# areaRetangulo = a*b

# print(f'TRIANGULO: {triaguloretangulo:.3F}')
# print(f'CIRCULO: {areaCirculo:.3F}')
# print(f'TRAPEZIO: {areaTrapezio:.3F}')
# print(f'QUADRADO: {areaQuadrado:.3F}')
# print(f'RETANGULO: {areaRetangulo:.3F}')

# =================================

# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

# maiorAB = (a + b + abs(a - b)) // 2

# if maiorAB < c:
#     print(f'{c} eh o maior')
# else:
#     print(f'{maiorAB} eh o maior')
    
x, y = input().split()
x, y = int(x), float(y)

consumoMedio=x/y

print(f'{consumoMedio:.3f} km/l')

