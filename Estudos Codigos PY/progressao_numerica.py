num=int(input('Desseja quantos termos, da serie de PN "Progressão Numerica": '))
k=1
for cont in range(1,num+1):
    if cont%3==1:
        print(k,end=' ')
    elif cont%3==2:
        print(k+3,end=' ')
    else:
        print(k+3,end=' ')
        k+=1
print()