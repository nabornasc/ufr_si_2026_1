# codigo para digitar nome e salvar em uma variavel
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

