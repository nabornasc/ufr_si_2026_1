# a = int(input('Quer iniciar em [-1/0/1]: '))
# b = int(input('Quer ir até [10,100,…: '))
# c = int(input('Quer contar de quanto em quanto [1,2,…]: '))
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
# from sys import flags

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

#
# qtd=0
# for cont in range(4):
#     num=int(input('Digite um numero: '))
#     if num==0:
#         qtd+=1
# print(f'\n Quantidade de numero NULOS é: {qtd}, que da {qtd*100/4}% dos digitados.')
#
# fat=1
# for cont in range(1,4):
#     fat*=cont
# print(f'O fatorial de {cont} é: {fat:,.2f}')


# qtd=0
# for cont in range(5):
#     num=int(input('Digite um Numero: '))
#     if num<5:
#         qtd+=1
# if qtd>0:
#     print(f'Tivemos um total de {qtd} numero Menor que 5.')

# ic=int(input('Inicia em [0/1]: '))
# fm=int(input('Termina em [10/100]: '))
# ps=int(input('Passos [1/1;2/2]: '))
# qd=str(input('Cacular Quadrado [S/N]: ')).lower()
# el=str(input('Cacular Potencia [S/N]: ')).lower()
# pt=int(input('Potencia de [2;3]: '))
#
#
# for termo in range(ic,fm+1,ps):
#     if qd=='s':
#         quad=termo**2
#         print(f'O Quadrado de {termo} é {quad}')
#     elif el=='s':
#         pot=pt**termo
#         print(f'O numero {termo} na Potencia {pt} é {pot}')
#     else:
#         print(termo)
#

# fórmula PA = a1 + i * r, sendo a1 e r informados pelo usuário
#
# a1=int(input('Digite o 1º termo da PA: '))
# rz=int(input('Digite a razão da PA: '))
#
# for cont in range(a1,10,rz):
#     pa=a1+cont*rz
# print(pa)

# cont=1
# soma=0
# while(cont<101):
#     soma+=2
#     cont+=1
# print(soma)
#
# num=1
# while(num!=0):
#     num=int(input('Digite um numero qualquer, ou ZERO [0] para sair: '))
#     if num!=0:
#         print(f'O numero digitado foi {num}')

# flag=''
# while flag.lower() != 's':
#     num=int(input('Digite um numero: '))
#     quad=num**2
#     print(f'O numero {num} é {quad} ao quadrado.')
#     flag=str(input('Deseja Sair [S/N]: ')).lower()


# cont=0
# while cont<=100:
#     print(cont)
#     cont+=1

op=''
while op != 's':
    num=int(input('Digite um numero: '))

    if num<2:
        print(f'O numero {num}, não é Primo!')
    else:
        div=2
        pri=True

        while div*div<=num:
            if num % div == 0:
                pri=False
                break
            div+=1
        if pri:
            print(f'O numero {num}, é Primo!')
        else:
            print(f'O numero {num}, Não é Primo pois tem +{div} divisores.')
    op=str(input('Deseja [S]air:')).lower()
