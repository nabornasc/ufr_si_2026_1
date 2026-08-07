while(True):
    flag=0
    num=int(input('Digite um numero Inteiro [0 - P/ Sair]: '))
    
    for cont in range(1,num+1):
        if num%cont==0:
            print(cont)
            flag+=1
    
    if num==0:
        break
    
    if flag>2:
        print('Não é Primo')
    else:
        print('é Primo')