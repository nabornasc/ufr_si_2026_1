import os

cls=lambda: os.system('cls' if os.name=='nt' else 'clear')

cls()

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))

media=(nota1+nota2)/2

if media<5:
    print(f'Sua média foi {media:.1f}. Você está REPROVADO.')
elif 7 > media >= 5:
    print(f'Sua média foi {media:.1f}. Você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi {media:.1f}. Você está APROVADO.')

