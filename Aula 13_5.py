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
#     result+=num
#     cont+=1
# print(result)

# ============================================================
#
# print('Programa para somar "P.As"')
# pa=int(input('Deseja uma PA "Progressão Aritmética" de quantos números: '))
# rz=int(input('Qual a razão dessa PA "1/1; 2/2; 3/3…" : '))
# soma=0
# print('Passo a passo |   |   |')
# for cont in range(1,pa+1):
#     if rz==1:
#         print('Passo a passo ',soma,'+', cont)
#         soma+=cont
#     else:
#         print('Passo a passo ',soma,'+', cont*rz)
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

    print(f'O somatório de 0 a {num} fazendo 1/(2*n) = {calc}')

def somDiv():
    rep=int(input('Deseja repetir quantas X: '))
    limpar()
    cont_PI=str(input('Deseja contar os Pares/Impares [S/N]: ')).lower()
    limpar()
    cont_Pri=str(input('Deseja verificar se é Primo [S/N]: ')).lower()
    limpar()

    for cont in range(1,rep+1,1):
        calc=0
        numPar=0
        numImpar=0

        valor=int(input('Digite um valor INT > 0: '))
        for cont1 in range(1,valor+1,1):
            if valor % cont1 == 0:
                calc=calc+1
                print(f'{valor} / {cont1} = {valor/cont1}')
                numPar=numPar+1
            elif valor % cont1 != 0:
                numImpar=numImpar+1

        print(f'{valor} tem um total de {calc} de divisores.',end='\n\n')

        if cont_Pri == 's' and calc == 2:
            print(f'{valor} é um numero Primo!\n')
        else:
            print(f'{valor} não é um numero Primo!\n')

        if cont_PI == 's':
            print(f'A quantidade de pares do numero {valor} é = {numPar}.')
            print(f'A quantidade de ímpares do numero {valor} é = {numImpar}.')


print('Escolha a Função!')
print('[1] PA "Progressão Aritimetica"')
print('[2] Fatorial')
print('[3] Somatório Matemático')
print('[4] Somatório Divisores')


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
elif opc == 4:
    limpar()
    somDiv()
