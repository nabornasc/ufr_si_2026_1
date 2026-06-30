"""# codigo para digitar nome e salvar em uma variavel
nome = str(input("Digite seu nome: "))
print("Olá, " + nome + "! Bem-vindo ao Python!")

# agora vai receber data de nascimento no formato ddmmaaaa, salvar em uma variavel e mostra minha idade em anos, meses e dias, considerando o ano atual.
ano_nascimento = int(input("Digite seu nascimento (ddmmaaaa): "))
# leia a data do pc para calcular a idade
from datetime import datetime
data_atual = datetime.now()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day
# extrai o dia, mês e ano do nascimento
dia_nascimento = ano_nascimento // 1000000
print(dia_nascimento)
mes_nascimento = (ano_nascimento // 10000) % 100
print(mes_nascimento)
ano_nascimento = ano_nascimento % 10000
print(ano_nascimento)
# calcula a idade em anos, meses e dias
idade_anos = ano_atual - ano_nascimento
idade_meses = mes_atual - mes_nascimento
idade_dias = dia_atual - dia_nascimento
print("Você tem " + str(idade_anos) + " anos, " + str(idade_meses) + " meses e " + str(idade_dias) + " dias.")
"""

"""
# codigo de verificação de condição positivo, negativo ou igual
# compare se é impar ou par

numero=int(input("Digite um numero para tester se é positivo, negativo ou igual a zero: "))
if numero > 0:
    if numero % 2 == 0:
        print("O numero é positivo e par.")
    else:
        print("O numero é positivo e ímpar.")
elif numero < 0:
    if numero % 2 == 0:
        print("O numero é negativo e par.")
    else:
        print("O numero é negativo e ímpar.")
else:
    print("O numero é igual a zero.")
"""
"""
# codigo que recebe 2 numero inteiros e compara se são iguais ou diferentes, e se são pares ou ímpares
numero1=int(input("Digite o primeiro numero inteiro: "))
numero2=int(input("Digite o segundo numero inteiro: "))

if numero1 == numero2:
    if numero1 % 2 == 0:
        print("O primeiro numero é par.")
    else:
        print("O primeiro numero é ímpar.")
    print("Os numeros são iguais.")
else:
    if numero1 % 2 == 0:
        print("O primeiro numero é par.")
    else:
        print("O primeiro numero é ímpar.")
    print("Os numeros são diferentes.")
    if numero2 % 2 == 0:
        print("O segundo numero é par.")
    else:
        print("O segundo numero é ímpar.")
"""
"""
import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

matA = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

for l in range(len(matA)):
    for c in range(len(matA[l])):
        print(matA[l][c], end=" ")
    print()


# Alternativa com lista
# list = (
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# )
#
# for l in range(len(list)):
#     for c in range(len(list[l])):
#         print(list[l][c], end=" ")
#     print()
"""
"""
valor = int(input())
meses =  {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

for m, n in meses.items():
    if n == valor:
        print(m)
"""

"""
qtdP=0
for cont in range(6):
    num=float(input())
    if num>0:
        qtdP+=1
print(f'{qtdP} valores positivos')
"""

"""
a = 90
b = 200
qa = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    qa += 1
    print(f"{qa:3} anos: Cidades - A={a:.2f}mi || B={b:.2f}mi")
"""
"""
soma = 0
cont = 1
while cont <= 100:
    soma = soma + cont
    cont = cont + 1
print(f"A soma dos 100 primeiros numeros é: {soma}")
"""
"""
massa = int(input("digite a massa inicial em gramas: "))
t = 50

while not (massa < 0.5):
    massa = massa - massa / 2
    t = t + 1

print("tempo de perda foi ", t)
"""


# import os

# cls = lambda: os.system("cls" if os.name == "nt" else "clear")
# cls()

# abc = range(97, 123)

# for l in abc:

#     print(chr(l), end=" ")


import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

vetNomes = ["Pedro", "Paulo", "Mario", "Andréia", "Julia", "Domingos", "Nabor"]
vetNumeros = [0, 11, 2, 5, 3, 6, 8, 4, 9, 7]

# print(vetNomes[4])
# print(vetNomes)
# print(vetNumeros[2:5])

# cont = len(vetNomes)

# for cont in range(0, cont):
#     print(f"Na posição {cont} tem {vetNomes[cont]}")
#     # if cont == len(vetNomes) - 1:
#     #     break

# nomes = []
# idades = []
# cont = 0
# flag = True

# while flag:
#     print(f"Digite os dados para posição {cont}")
#     nomes.insert(cont, input(f"Digite o nome: "))
#     idades.insert(cont, input(f"Digite a idade: "))
#     cont += 1
#     if cont > 2:
#         flag = False

# pesq = input(str("Digite um nome para pesquisar: "))

# for cont in range(len(nomes)):
#     if pesq == nomes[cont]:
#         print(f"O nome {pesq} esta na posição {cont} do vetor\n{nomes}")
        
# =======================================================

# list = (
#     [1,2,3],
#     [4,5,6],
#     [7,8,9], 
# )

# for l in range(len(list)):
#     for c in range(len(list[l])):
#         print(list[l][c], end=" ")
#     print()

# =====================================================================
soma = 0
qtdP = 0

for cont in range(len(vetNomes)):
    print(f"\nNa posição {cont} do vetor, tem {vetNomes[cont]}")
    soma+=vetNumeros[cont]
    if vetNumeros[cont]%2==0:
        qtdP+=1
        print(f"\nO numero {vetNumeros[cont]} do vetor é par")
print('\nA soma dos numeros do vetor é: ', soma)
print('A quantidade de numeros pares do vetor é: ', qtdP)