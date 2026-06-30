import os

cls=lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
cls()

cont=1
somaDiv=0
while cont<51:
    somaDiv+=1/cont
    print(f'1/{cont} = {somaDiv:.4f}')
    cont+=1
print(f'A soma dos disvisores de 1 a 50 é: {somaDiv:.4f}')
