acu=0
cont=1
while acu<100:
    acu+=cont
    print(f'{acu if acu<100 else "Acabou"}')
    cont+=1