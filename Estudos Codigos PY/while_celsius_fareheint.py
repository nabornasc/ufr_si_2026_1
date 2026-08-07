cont=0
while(cont<101):
    x=(cont*1.8)+32
    print(f'{cont:7.2f}ºC em{x:7.2f}ºF ||',end="")
    if cont%5==0:
        print()
    cont+=1
