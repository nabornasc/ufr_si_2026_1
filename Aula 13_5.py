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
print(soma)