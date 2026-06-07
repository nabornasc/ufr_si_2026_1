soma=0
sinal=1

for n1 in range(1,82,2):
    fat=1
    for n2 in range(1,n1+1):
        fat*=n2
        
    soma += sinal * fat
    print(f'{'+'if sinal==1 else '-'} {n1}! = {sinal*fat}')
    
    sinal*=-1
    
print(f'\nResultado:{soma:,}')