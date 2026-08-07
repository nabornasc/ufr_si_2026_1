
import os

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpar()

t1=int(input('Digite 1ºTermo: '))
t2=int(input('Digite 2ºTermo: '))

ult=20

print(f'{t1} - {t2}',end=' - ')

for cont in range(3,ult+1):

    if cont%2!=0:
        t3=t2-t1
    else:
        t3=t2+t1

    if cont==ult:
        print(f'{t3}')
    else:
        print(f'{t3}',end=' - ')

    t1=t2
    t2=t3
