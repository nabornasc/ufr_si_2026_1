num=int(input('Digite um número Inteiro: '))
soma=0
for c in range(1,num):
    if num%c==0:
        soma+=c
        print(c)
        
if soma==num:
    print(f'\n{num} é um numero Perfeito!')
else:
    print(f'\n{num} NÃO é um numero Perfeito!')