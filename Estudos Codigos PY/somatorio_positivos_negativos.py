somaP=0
somaN=0
somaT=0
for cont in range(1,101,1):
    num=int(input('Digite um numero: '))
    if num>=0:
        somaP+=num
    else:
        somaN+=num
somaT=somaP+somaN
print(f'\nA soma dos numeros Positivos digitados deu {somaP}')
print(f'A soma dos numeros Negativos digitados deu {somaN}')
print(f'\nA soma dos numeros Positivos+Negativos deu {somaT}')