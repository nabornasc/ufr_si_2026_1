# a = int(input('Quer iniciar em [0/1]: '))
# b = int(input('Quer ir até [10,100,..: '))
# c = int(input('Quer contar de quanto em quanto [1,2,..]: '))
# d = str(input('Crescente ou decrescente [C/D]: ').lower())
#
# for i in range(a, b + 1, c):
#     if d == 'c':
#         print(i)
#         i += i
#     elif d == 'd':
#         print(b)
#         b -= c
# ============================================================

# rep=int(input('Deseja executar quantas X: '))
#
# soma=0
# resul=0
#
# for cont in range(rep):
#     num = float(input('Digite um numero para SOMA: '))
#     resul+=num
#     cont+=1
# print(resul)

# ============================================================
#
# print('Programa para somar "P.As"')
# pa=int(input('Deseja uma PA "Progressão Aritmética de quantos números: '))
# rz=int(input('Qual a razão dessa PA "1/1; 2/2; 3/3.. : '))
# soma=0
# print('Passo a passo |   |   |')
# for cont in range(1,pa+1):
#     if rz==1:
#         print('Passo a passo ',soma,'+',cont)
#         soma+=cont
#     else:
#         print('Passo a passo ',soma,'+',cont*rz)
#         soma+=cont*rz
# print(soma)

# ============================================================
from os import system,name

def limpar():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def progA():
    print('Programa para somar "P.As"')
    pa=int(input('Deseja uma PA "Progressão Aritmética de quantos números: '))
    rz=int(input('Qual a razão dessa PA "1/1; 2/2; 3/3.. : '))
    soma=0
    print('Passo a passo |   |   |')
    for cont in range(1,pa+1):
        if rz==1:
            print('Passo a passo ',soma,'+',cont)
            soma+=cont
        else:
            print('Passo a passo ',soma,'+',cont*rz)
            soma+=cont*rz
    print('Soma final: ',soma)

def fatorial(n):
    mult = 1
    for cont in range(1,n+1,1):
        mult = mult * cont
        if cont < n:
            print(cont,end="*")
        else:
            print(cont,end=" ")
            print(f'= {mult:,}')
    return mult

def somNum():
    num=int(input('Calculo de somatórios: '))
    calc=0
    for cont in range(1,num+1,1):
        calc=calc+1/(2*cont)
        cont+=cont
    return print(f'O somatório de 0 a {num} fazendo 1/(2*n) = {calc}')

print('Escolha a Função!')
print('[1] PA "Progressão Aritimetica"')
print('[2] Fatorial')
print('[3] Somatório Matemático')

opc=int(input())
limpar()

if opc == 1:
    limpar()
    progA()
elif opc == 2:
    limpar()
    fatorial(int(input('Digite n!: ')))
elif opc == 3:
    limpar()
    somNum()