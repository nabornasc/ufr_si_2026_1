import os

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def armstrong(num):
    soma = 0

    for digito in str(num):
        soma += int(digito) ** len(str(num))

    return soma == num


def listar_armstrong(inicio, fim):

    encontrados = []

    for num in range(inicio, fim + 1):

        if armstrong(num):
            encontrados.append(num)

    return encontrados


# Programa Principal
limpar()

print('=== NÚMEROS DE ARMSTRONG ===')

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

resultado = listar_armstrong(inicio, fim)

print(f'\nArmstrong encontrados entre {inicio} e {fim}:')

for numero in resultado:
    print(numero)