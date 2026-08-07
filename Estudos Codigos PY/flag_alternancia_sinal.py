flag=True
somaP=0
somaN=0
for cont in range(2,101,2):

    if flag==True:
        somaP+=cont
        print(cont,f"= + {somaP}")
        flag=False
    else:
        somaN+=cont
        print(cont,f"= - {somaN}")
        flag=True
        
print(f'A soma dos Positivos é {somaP}, e dos Negativos é {somaN}. Resultado da Soma P+N {somaP-somaN}')