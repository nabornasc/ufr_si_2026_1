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

# =================================
    
# x, y = input().split()
# x, y = int(x), float(y)

# consumoMedio=x/y

# print(f'{consumoMedio:.3f} km/l')

# =================================

# x1,y1=map(float,input().split())
# x2,y2=map(float,input().split())

# distancia=((x2-x1)**2+(y2-y1)**2)**(1/2)

# print(f'{distancia:.4f}')

# =================================

# tempo=int(input())*2

# print(f'{tempo} minutos')

# =================================

# tempoViagem=int(input())
# velocidadeMedia=int(input())

# quantLitros=(tempoViagem*velocidadeMedia)/12

# print(f'{quantLitros:.3f}')

# =================================

''' ENCONTRAR ERRO 
# n=int(input())
# resto=n

# nota100=(resto//100)
# resto=resto%100

# nota50=(resto//50)
# resto=resto%50

# nota20=(resto//20)
# resto=resto%20

# nota10=(resto//10)
# resto=resto%10

# nota5=(resto//5)
# resto=resto%5

# nota2=(resto//2)
# resto=resto%2

# nota1=(resto//1)

# print(f'{nota100} nota(s) de R$ 100,00')
# print(f'{nota50} nota(s) de R$ 50,00')
# print(f'{nota20} nota(s) de R$ 20,00')
# print(f'{nota10} nota(s) de R$ 10,00')
# print(f'{nota5} nota(s) de R$ 5,00')
# print(f'{nota2} nota(s) de R$ 2,00')
# print(f'{nota1} nota(s) de R$ 1,00')
'''

# =================================

# n = int(input())
# cedulas = [100, 50, 20, 10, 5, 2, 1]

# resto = n
# for cedula in cedulas:
#     quantidade = resto // cedula
#     resto = resto % cedula
#     print(f'{quantidade} nota(s) de R$ {cedula:,.2f}'.replace(',', '.'))

# =================================
    
# n=int(input())
# resto=n

# cedulas = [100,50,20,10,5,2,1]

# for cedula in cedulas:
#     quantidadeCedulas=resto//cedula
#     resto=resto%cedula
#     print(f'{quantidadeCedulas} nota(s) de R$ {cedula:.2f}'.replace('.',','))

# tempo=int(input())

# segundos=tempo%60
# print(segundos)
# minutos=(tempo//60)%60
# print(minutos)
# horas=tempo//3600
# print(horas)

# print(f'{horas}:{minutos}:{segundos}')


# idadeDias=int(input())

# ano=idadeDias//365
# mes=(idadeDias%365)//30
# dia=(idadeDias%365)%30

# print(f'{ano} ano(s)')
# print(f'{mes} mes(es)') 
# print(f'{dia} dia(s)')


# valor=float(input())
# centavos=round(valor*100)

# notas=[100,50,20,10,5,2]
# moedas=[1,.5,.25,.10,.05,.01]

# print('NOTAS:')
# for nota in notas:
#     quantNotas=valor//nota
#     valor=valor%nota
#     print(f'{int(quantNotas)} nota(s) de R$ {nota:.2f}'.replace(',','.'))

# print('MOEDAS:')
# for moeda in moedas:
#     quantMoedas=valor//moeda
#     valor=valor%moeda
#     print(f'{int(quantMoedas)} moeda(s) de R$ {moeda:.2f}'.replace(',','.'))

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())

# if b>c:
#     if d>a:
#         if c+d:
#             if a+b:
#                 if c % 2 == 0 and d % 2 == 0: # Positivos
#                     if a % 2 == 0: # par
#                         print('Valores aceitos')
# else:
#     print('Valores nao aceitos')
    

# a, b, c, d = map(int, input().split())

# if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
#     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")

# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# a=float(input())
# b=float(input())
# c=float(input())

# delta=(b**2)-4*a*c

# if a==0 or delta<0:
#     print('Impossivel calcular')
# else:
#     r1=(-b+delta**0.5)/(2*a)
#     r2=(-b-delta**0.5)/(2*a)
#     print(f'R1 = {r1:.5f}')
#     print(f'R2 = {r2:.5f}')

a,b,c=map(float,input().split())

delta=(b**2)-4*a*c

if a==0 or delta<0:
    print('Impossivel calcular')
else:
    r1=(-b+delta**(1/2))/(2*a)
    r2=(-b-delta**(1/2))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')