
acu=1
tot=0
n=int(input('Digite N termo da serie: '))

for cont in range(1,n+1):
    acu+=2
    termo=cont/acu
    print(cont,"/",acu,"=",f'{termo:.2f}')
    tot+=termo
print(f'\n O total da soma é {tot:.3f}')
