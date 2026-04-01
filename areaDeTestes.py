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
'''
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
'''
'''
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
'''