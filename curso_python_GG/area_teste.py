# import os
from os import system,name

cls = lambda: system('cls' if name=='NT' else 'clear')

cls()
print('Oi')
