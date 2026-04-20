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

# a,b,c=map(float,input().split())

# delta=(b**2)-4*a*c

# if a==0 or delta<0:
#     print('Impossivel calcular')
# else:
#     r1=(-b+delta**(1/2))/(2*a)
#     r2=(-b-delta**(1/2))/(2*a)
#     print(f'R1 = {r1:.5f}')
#     print(f'R2 = {r2:.5f}')
    
# valor=float(input())

# if valor<0 or 100<valor:
#     print('Fora de intervalo')
# else:
#     if valor >= 0 and valor <= 25:
#         print('Intervalo [0,25]')
#     else:
#         if valor>25 and valor <= 50:
#             print('Intervalo (25,50]')
#         else:
#             if valor>50 and valor <= 75:
#                 print('Intervalo [50,75]')
#             else:
#                 print('Intervalo (75,100]')
 
# ======================================================
 
# codigoItem,quantItem=map(int,input().split())

# if codigoItem==1:
#     preco=4
# elif codigoItem==2:
#     preco=4.5
# elif codigoItem==3:
#     preco=5
# elif codigoItem==4:
#     preco=2
# elif codigoItem==5:
#     preco=1.5
    
# total=preco*quantItem

# print(f'Total: R$ {total:.2f}')

# ======================================================

# codItem,quantItem=map(int,input().split())

# preco={1:4,2:4.5,3:5,4:2,5:1.5}

# total=preco[codItem]*quantItem

# print(f'Total: R$ {total:.2f}')

# ======================================================

# n1,n2,n3,n4=map(float,input().split())

# media=(n1*2+n2*3+n3*4+n4*1)/10

# if media>=7:
#     print(f'Media: {media:.1f}')
#     print('Aluno aprovado.')
# elif media>=5:
#     n5=float(input())
#     print(f'Media: {media:.1f}')
#     print('Aluno em exame.')
#     print(f'Nota do exame: {n5:.1f}')
#     novaMedia=(media+n5)/2
#     if novaMedia >= 5:
#         print('Aluno aprovado.')
#         print(f'Media final: {novaMedia:.1f}')
#     else:
#         print('Aluno reprovado.')
#         print(f'Media final: {novaMedia:.1f}')
# else:
#     print(f'Media: {media:.1f}')
#     print('Aluno reprovado.')

# ======================================================

# n1, n2, n3, n4 = map(float, input().split())

# media = (n1*2 + n2*3 + n3*4 + n4) / 10

# print(f"Media: {media:.1f}")

# if media >= 7:
#     print("Aluno aprovado.")

# elif media < 5:
#     print("Aluno reprovado.")

# else:
#     print("Aluno em exame.")
    
#     exame = float(input())
#     print(f"Nota do exame: {exame:.1f}")
    
#     media_final = (media + exame) / 2
    
#     if media_final >= 5:
#         print("Aluno aprovado.")
#     else:
#         print("Aluno reprovado.")
    
#     print(f"Media final: {media_final:.1f}")

# ======================================================

# x,y=map(float,input().split())

# if x==y==0:
#     print('Origem')
# elif x==0 or y==0:
#     print('Eixo X' if x==0 else 'Eixo Y')
# else:
#     if x>0 and y>0:
#         print('Q1')
#     elif x<0 and y>0:
#         print('Q2')
#     elif x<0 and y<0:
#         print('Q3')
#     else:
#         print('Q4')

# ======================================================


a,b,c=map(int,input().split())

if a<b<c:
    print(f'{a}\n{b}\n{c}\n')
    print(f'{a}\n{b}\n{c}')
else:
    if a<c<b:
        print(f'{a}\n{c}\n{b}\n')
        print(f'{a}\n{b}\n{c}')
    else:
        if b<a<c:
            print(f'{b}\n{a}\n{c}\n')
            print(f'{a}\n{b}\n{c}')
        else:
            if b<c<a:
                print(f'{b}\n{c}\n{a}\n')
                print(f'{a}\n{b}\n{c}')
            else:
                if c<a<b:
                    print(f'{c}\n{a}\n{b}\n')
                    print(f'{a}\n{b}\n{c}')
                else:
                    print(f'{c}\n{b}\n{a}\n')
                    print(f'{a}\n{b}\n{c}') 

