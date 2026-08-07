inc=int(input('Digite o numero inicial [0/1]: '))
fim=int(input('Digite o numero final: '))
somaI=0
for cont in range(inc,fim+1):
    if cont%2!=0:
        somaI+=cont
        print(somaI,end="+")
print(f'\b\b\b\b = {somaI}')
print(f'\nA Soma dos numeros Impares entre {inc} e {fim}, resultam: {somaI}')
