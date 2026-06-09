flag=False
for cont in range(5):
    num=int(input('Digite um numero: '))
    if num%2==0:
        flag=True
if flag==False:
    print('Nenhum numero PAR digitado')
else:
    print('Teve numero PAR digitado')
