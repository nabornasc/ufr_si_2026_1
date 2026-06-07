numF=int(input('Calculo de Fatorial, digite um numero: '))
fat=1
for cont in range(1,numF+1):
    fat=fat*cont
print(f'\nO fatorial de {numF} é: {fat:,}!')