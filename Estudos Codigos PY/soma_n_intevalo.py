inc=int(input('Digite o numero inicial [0/1]: '))
fim=int(input('Digite o numero final: '))
somaN=0
for cont in range(inc,fim+1):
    somaN+=cont
print(f'A Soma dos numeros entre {inc} e {fim}, resultam: {somaN}')