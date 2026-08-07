soma=0
n=int(input('Digite um numero >0 : '))
for cont in range(1,n):
    if n%cont==0:
        soma+=cont
        print(f'{cont} é divisor de {n}')
if soma==n:
    print(f'\n{n} é um numero PERFEITO')
else:
    print(f'\n{n} NÃO é um numero PERFEITO')