
import os
cls=lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
cls()

cont=0
somaT=0
while cont<101:
    somaT+=cont
    cont+=1
print(f'A soma total dos contadores é: {somaT}')
