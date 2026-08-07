qtd=0

for cont in range(2,1001):
    primo=True
    
    for cont1 in range(2,cont):
        if cont%cont1==0:
            primo=False
            break
        
    if primo:
        print(cont,end=" ")
        qtd+=1
        
print(f'\n\nTotal de primos encontrados: {qtd}')