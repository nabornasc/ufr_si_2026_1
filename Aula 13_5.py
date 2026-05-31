# a = int(input('Quer iniciar em [-1/0/1]: '))
# b = int(input('Quer ir até [10,100,..: '))
# c = int(input('Quer contar de quanto em quanto [1,2,..]: '))
# d = str(input('Crescente ou decrescente [C/D]: ').lower())
#
# for i in range(a, b + 1, c):
#     if d == 'c':
#         print(i)
#         i += i
#     else:
#         print(b)
#         b -= c
# =====================================================================
#
# mat = []
#
# for contX in range(3):
#     linha = []
#     for contY in range(2):
#         valor = input(f'[{contX}] [{contY}]: ')
#         linha.append(valor)
#     mat.append(linha)
# print(mat)
# from random import randint

# =====================================================================
# aprendendo a criar e manipular matrizes

# qtLin=int(input('Digite quantas linhas deseja na Matriz: '))
# qtCol=int(input('Digite quantas colunas deseja na Matriz: '))
#
# for lin in range(qtLin):
#     for col in range(qtCol):
#         rd = randint(1,60)
#         print(f'{rd:4}',end='')
#     print()

# =====================================================================
#  contagem regressiva usando as propriedades, e manipulando incrementador
# for lin in range(10,-1,-1):
#     print(lin)

# =====================================================================
# e6.1
# for lin in range(0,20,1):
#     print('Alg')

# =====================================================================
# e6.2/3 - calcular o quadrado do número

# rept=int(input('Quantas X deseja repetir: '))
#
# for lin in range(rept):
#     num=int(input('Digite um numero para calcular ao quadrado: '))
#     resp=num*num
#     print(f'O quadrado do nº: {num}, é {resp}')

# =====================================================================
# e6.4

# for cont in range(0,101,1):
#     print(f'{cont:4}',end='')
#     if (cont+1)%20==0:
#         print()

# list=[]
# for cont in range(1,101):
#     if cont%3==0 and cont%5==0:
#         print(f'{cont} é divisivel por 3 e 5 ao mesmo tempo.')
#         list.append(cont)
# print(list)

# =====================================================================
# e6.5
#
# for cont in range(0,101):
#     tempF=cont*1.8+32
#     # print(f'{tempF:10.1f}ºF',end='') # metodo f-string
#     print(str(round(tempF,1)).rjust(10),'ºF',end='') # metodo round+rjust
#     # print('{:10.1f}ºF'.format(tempF),end="") # metodo format

# =====================================================================
# e6.6

# for tab1 in range(1,11):
#     for tab2 in range(1,11):
#         calc=tab2*tab1
#         print(f'{tab1} x {tab2} = {calc}',end='\n')
#         if tab2%10==0:
#             print()

# a=0
# qtd=0
# qtdI=0
# for cont in range(1,11):
#     a=a+cont
#     print(a)
#     if a%2==0:
#         qtd+=1
#     else:
#         qtdI+=1
# print(f'\nTemos um total de {qtd} numeros Pares e {qtdI} de Impares.')

# matA = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# soma=0
# qtd=0
# for l in range(3):
#     for c in range(3):
#         if matA[l][c]%2==0:
#             soma+=matA[l][c]
#             qtd+=1
#             print(matA[l][c])
# print(f'\n O total da soma é {soma}, divido pela quantidade {qtd} vai dar a media {soma/qtd}')

