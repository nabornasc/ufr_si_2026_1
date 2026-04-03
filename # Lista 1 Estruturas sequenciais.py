'''# Lista 1 Estruturas sequenciais

# Exercício 1
varInteiro=int(input("Digite um número inteiro: "))
varReal=float(input("Digite um número real: "))
varTexto=str(input("Digite um texto: "))

resultado=varInteiro+varReal
print("O resultado da soma do número inteiro e do número real é: ", resultado)
print("O texto digitado foi: ", varTexto)  
'''
'''
# Exercício 2
# algoritmo que leia dois números inteiros do teclado, um de cada vez, e realizar a troca dos valores dessas variáveis sem que os valores sejam perdidos durante a troca
var1=int(input("Digite o primeiro número inteiro: "))
var2=int(input("Digite o segundo número inteiro: "))
print("Valores antes da troca:")
print("Variável 1:", var1)
print("Variável 2:", var2)
# Realizando a troca dos valores
var1, var2 = var2, var1
# 2 opção:
var3, var4 = var2, var1
print("Valores depois da troca:")
print("Variável 1:", var1)
print("Variável 2:", var2)
# print("Variável 1:", var4)
# print("Variável 2:", var3)
'''
'''
# Exercício 3
# algoritmo que leia um número inteiro do teclado e calcule o antecessor e o sucessor desse número
var=int(input("Digite um número inteiro: "))
antecessor=var-1
sucessor=var+1
print(f"O antecessor do número é: {antecessor}", f'e o sucessor do número é: {sucessor}')
'''
'''
# Exercício 4
# algoritmo que receba um número real, calcule e imprima a parte inteira do número, a parte fracionária do número e o número arredondado
var=float(input('Digite um número real para segmentar a parte inteira, a parte fracionária e o número arredondado: '))
parteInteira=int(var)
parteFracionaria=var-parteInteira
numeroArredondado=round(var)
print(f"A parte inteira do número é: {parteInteira}")
print(f"A parte fracionária do número é: {parteFracionaria:.2f}")
print(f"O número arredondado é: {numeroArredondado}")
'''
'''
# Exercício 5
# algoritmo que solicite a razão de uma Progressão Aritmética (PA) e a posição do termo a ser calculado,valorTermo = 1 + (posicao_termo - 1) * razao
print('valorTermo = 1 + (posicao_termo - 1) * razao')
razao=float(input("Digite a razão da Progressão Aritmética (PA): "))
posicaoTermo=int(input("Digite a posição do termo a ser calculado: ")) 
valorTermo = 1 + (posicaoTermo - 1) * razao
print(f"O valor do termo na posição {posicaoTermo} é: {valorTermo}")
'''

# # Exercício 6
# # algoritmo que efetue o cálculo da quantidade de litros de combustível gastos em uma viagem, considerando que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade média
# print('Calculo de distância percorrida e litros gastos em uma viagem')
# tempoGasto=float(input('Digite o tempo gasto na viagem (em horas): '))
# velocidadeMedia=float(input('Digite a velocidade média durante a viagem (em km/h):'))
# eficiencia=float(input('Digite a eficiência do carro (km por litro): '))
# distPerc=tempoGasto*velocidadeMedia
# litrosGastos=distPerc/eficiencia
# print(f'A quantidade de litros de combustível gastos na viagem de {distPerc:.2f} km, foi de: {litrosGastos:.2f} litros')

# # Exercício 7
# # programa que, dados dois números inteiros como entrada, realiza a operação de divisão e exibe o dividendo, divisor, quociente e resto
# print('Programa para realizar a operação de divisão entre dois números inteiros e exibir o dividendo, divisor, quociente e resto')
# dividendo=int(input('Digite o dividendo (número inteiro): '))
# divisor=int(input('Digite o divisor (número inteiro): '))
# quociente=dividendo//divisor
# resto=dividendo%divisor
# print(f'Dividendo: {dividendo}')
# print(f'Divisor: {divisor}')
# print(f'Quociente: {quociente}')
# print(f'Resto: {resto}')

# # Exercício 8
# # algoritmo que receba um número de quatro dígitos e mostre as unidades, dezenas, centenas e milhares que compõem esse número.
# print('Algoritmo para decompor um número de quatro dígitos em unidades, dezenas, centenas e milhares')
# numero=int(input('Digite um número de quatro dígitos: '))
# unidades=numero%10
# dezenas=(numero//10)%10
# centenas=(numero//100)%10
# milhares=numero//1000
# print(f'Número: {numero}')
# print(f'Milhares: {milhares}')
# print(f'Centenas: {centenas}')
# print(f'Dezenas: {dezenas}')
# print(f'Unidades: {unidades}')

# # Exercício 9
# # algoritmo que leia uma informação de latitude no formato GGMMSS (Graus, Minutos e Segundos) e decomponha esta informação em graus, minutos e segundos
# print('Algoritmo para decompor uma informação de latitude no formato GGMMSS em graus, minutos e segundos')
# latitude=int(input('Digite a latitude no formato GGMMSS: '))
# if 0<=latitude<=999999:

#     graus=latitude//10000
#     minutos=(latitude//100)%100
#     segundos=latitude%100

#     print(f'Latitude: {latitude}')
#     print(f'Graus: {graus}')
#     print(f'Minutos: {minutos}')
#     print(f'Segundos: {segundos}')  

# else:
#     print('Valor de latitude inválido. Por favor, insira um número no formato GGMMSS (0 a 999999).')

# # Exercício 10
# # algoritmo que receba um número no formato DU (dezena e unidade) e imprima esse número invertido, ou seja, no formato UD.
# print('Algoritmo para inverter um número no formato DU (dezena e unidade) para UD')
# numero=int(input('Digite um número no formato DU (dezena e unidade): '))
# if 0<=numero<=99:
#     dezena=numero//10
#     unidade=numero%10
#     numeroInvertido=unidade*10+dezena

#     print(f'Número original: {numero}')
#     print(f'Número invertido: {numeroInvertido}')
# else:
#     print('Valor de número inválido. Por favor, insira um número no formato DU (0 a 99).')

# # Exercício 11
# # algoritmo que receba um número no formato CDU (centena, dezena e unidade) e imprima esse número invertido
# print('Algoritmo para inverter um número de 3 digitos no formato CDU (centena, dezena e unidade) para UDC')
# numero=int(input('Digite um número no formato CDU (centena, dezena e unidade): '))
# if 0<=numero<=999:
#     centena=numero//100
#     dezena=(numero//10)%10
#     unidade=numero%10
#     numeroInvertido=unidade*100+dezena*10+centena

#     print(f'Número original: {numero}')
#     print(f'Número invertido: {numeroInvertido}')
# else:
#     print('Valor de número inválido. Por favor, insira um número no formato CDU (0 a 999).')

# # # Exercício 12
# # Conversões e cálculo de tempo

# from datetime import *

# print('Teste das variaveis de data e hora')

# dataHoraAtual=datetime.now()
# print(f'Data e hora atual: {dataHoraAtual}')

# dataAtual=dataHoraAtual.date()
# print(f'Data atual: {dataAtual}')

# horaAtual=dataHoraAtual.time()
# print(f'Hora atual: {horaAtual}')

# dataHoraEspecifica=datetime(2024, 6, 30, 15, 30, 0)
# print(f'Data e hora específica: {dataHoraEspecifica}')

# dataEspecifica=dataHoraEspecifica.date()
# print(f'Data específica: {dataEspecifica}')

# horaEspecifica=dataHoraEspecifica.time()
# print(f'Hora específica: {horaEspecifica}')

# dataHoraFormatada=dataHoraAtual.strftime('%d/%m/%Y %H:%M:%S')
# print(f'Data e hora atual formatada: {dataHoraFormatada}')

# dataFormatada=dataAtual.strftime('%d/%m/%Y')
# print(f'Data atual formatada: {dataFormatada}')

# horaFormatada=horaAtual.strftime('%H:%M:%S')
# print(f'Hora atual formatada: {horaFormatada}')

# dataHoraConvertida=datetime.strptime('30/06/2024 15:30:00', '%d/%m/%Y %H:%M:%S')
# print(f'Data e hora convertida: {dataHoraConvertida}')

# dataConvertida=datetime.strptime('30/06/2024', '%d/%m/%Y')
# print(f'Data convertida: {dataConvertida}')

# horaConvertida=datetime.strptime('15:30:00', '%H:%M:%S')
# print(f'Hora convertida: {horaConvertida}')

# print('Fim dos testes de data e hora')

# Exercício 13
# algoritmo que leia a idade de uma pessoa em anos e mostre esse valor convertido em dias, horas, minutos e segundos, considerando o tempo decorrido até o momento em que o algoritmo foi executado
# from datetime import datetime

# print('Algoritmo para converter a idade completa.')

# dataString=input('Digite a data de nascimento da pessoa no formato DDMMAAAA: ')
# dataNascimento=datetime.strptime(dataString,'%d%m%Y')
# dataAtual=datetime.now()

# idadeAnos=dataAtual.year-dataNascimento.year 
# # print(f'Idade em anos: {idadeAnos}')
# idadeMeses=dataAtual.month-dataNascimento.month 
# # print(f'Idade em meses: {idadeMeses}')
# idadeDias=dataAtual.day-dataNascimento.day 
# # print(f'Idade em dias: {idadeDias}')


# if idadeMeses<0 or (idadeMeses==0 and idadeDias<0):
#     idadeAnos-=1
#     idadeMeses+=12
#     idadeDias+=30

# diferencaDias=(dataAtual-dataNascimento).days
# # print(f'Diferença em dias: {diferencaDias}')
# idadeHoras=diferencaDias*24
# # print(f'Idade em horas: {idadeHoras}')
# idadeMinutos=idadeHoras*60
# # print(f'Idade em minutos: {idadeMinutos}')
# idadeSegundos=idadeMinutos*60
# # print(f'Idade em segundos: {idadeSegundos}')

# def formatar(n):
#     return f'{n:,}'.replace(',', '.')

# print('\nIdade detalhada:')
# print(f'Anos: {formatar(idadeAnos)}\nMeses: {formatar(idadeMeses)}\nDias: {formatar(idadeDias)}')

# print(f'Horas: {formatar(idadeHoras)}\nMinutos: {formatar(idadeMinutos)}\nSegundos: {formatar(idadeSegundos)}')

# exercício 14
# algoritmo que receba a informação de data (dia e mês, no formato DDMM) e calcular e mostrar o total de dias cumpridos no ano
# v1 - manual 
# from datetime import datetime


# print('Algoritmo para calcular o total de dias cumpridos no ano a partir de uma data no formato DDMM') 
# dataStr=input('Digite a data no formato DDMM: ')
# data=datetime.strptime(dataStr,'%d%m')

# dia=data.day
# mes=data.month

# diasCumpridos=0 

# if mes>1:
#     diasCumpridos+=31
# if mes>2:
#     diasCumpridos+=29
# if mes>3:
#     diasCumpridos+=31
# if mes>4:
#     diasCumpridos+=30
# if mes>5:
#     diasCumpridos+=31
# if mes>6:
#     diasCumpridos+=30
# if mes>7:
#     diasCumpridos+=31
# if mes>8:    
#     diasCumpridos+=31
# if mes>9:
#     diasCumpridos+=30
# if mes>10:
#     diasCumpridos+=31
# if mes>11:
#     diasCumpridos+=30

# diasCumpridos+=dia

# print(f'Total de dias cumpridos no ano até a data {dataStr}: {diasCumpridos}')

# # v2 - usando lista
# from datetime import datetime

# print('Algoritmo para calcular o total de dias cumpridos no ano a partir de uma data no formato DDMM')
# dataStr=input('Digite a data no formato DDMM: ')
# data=datetime.strptime(dataStr, '%d%m')
# dia=data.day
# mes=data.month
# diasPorMes=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# diasCumpridos=sum(diasPorMes[:mes-1])+dia
# print(f'Total de dias cumpridos no ano até a data {dataStr}: {diasCumpridos}')

# # v3 - usando datetime
# from datetime import datetime

# print('Algoritmo para calcular o total de dias cumpridos no ano a partir de uma data no formato DDMM')

# try:

#     dataStr=input('Digite a data no formato DDMM: ')

#     ano=datetime.now().year

#     data=datetime.strptime(dataStr+str(ano), '%d%m%Y')

#     diasCumpridos=(data.timetuple().tm_yday)

#     print(f'Total de dias cumpridos no ano até a data {dataStr}: {diasCumpridos}')

# except ValueError:

#     print('Data inválida. Por favor, insira uma data no formato DDMM (ex: 15 de junho no formato 1506).')

# # exercício 15
# # algoritmo que leia um valor em horas e minutos, representado por um número inteiro de 4 dígitos, e informe quantos minutos se passaram desde o início do dia

# print('Algoritmo para calcular quantos minutos se passaram desde o início do dia a partir de um valor em horas e minutos no formato HHMM')

# tempo=int(input('Digite um valor em H e M no formato HHMM:'))
# minutos=tempo//100*60+tempo%100 # calculo usando o quociente para obter as horas e multiplicando por 60, e usando o resto para obter os minutos
# print(f'Minutos passados desde o início do dia: {minutos} minutos!')

# #  exercício 16
# # algoritmo que receba a informação de hora e minutos no formato HHMM e calcular e mostrar o total de horas e total de minutos que faltam para o final do dia

# print('Algoritmo para calcular quantas horas e minutos faltam para o final do dia a partir de um valor em horas e minutos no formato HHMM')
# tempo=int(input('Digite um valor em H e M no formato HHMM:'))
# horas=tempo//100
# minutos=tempo%100
# horasFaltam=23-horas
# minutosFaltam=60-minutos
# if minutosFaltam==60:
#     minutosFaltam=0
#     horasFaltam+=1

# print(f'Faltam {horasFaltam} horas e {minutosFaltam} minutos para o final do dia!')

# # exercício 17
# # algoritmo que receba a informação de data e hora (formato DDMMHHMM - dia mês hora minutos) e calcular e mostrar o total de tempo para finalizar o ano comercial, também no formato DDMMHHMM

# print('Algoritmo para calcular o tempo restante para finalizar o ano comercial a partir de uma data e hora no formato DDMMHHMM')
# from datetime import datetime

# try: # usando try para tratar possíveis erros de formato na entrada do usuário

#     dataHoraStr=input('Digite a data e hora no formato DDMMHHMM: ')

#     ano=datetime.now().year

#     dataHora=datetime.strptime(dataHoraStr+str(ano), '%d%m%H%M%Y')

#     dataHoraFim=datetime(ano, 12, 31, 23, 59)

#     tempoRestante=dataHoraFim-dataHora

#     dias=tempoRestante.days
#     horas=tempoRestante.seconds//3600
#     minutos=(tempoRestante.seconds%3600)//60

#     print(f'Tempo restante para finalizar o ano comercial: {dias} dias, {horas} horas e {minutos} minutos!')
# except ValueError: # caso o usuário insira um valor que não esteja no formato esperado, o programa exibirá uma mensagem de erro 

#     print('Data e hora inválida. Por favor, insira uma data e hora no formato DDMMHHMM (ex: 15 de junho às 14:30 no formato 15061430).')

# # exercício 18
# # algoritmo que receba dois números inteiros de 4 dígitos, representando horas e minutos (por exemplo: 1545, equivalente a 15:45h), e calcular quantas horas estão contidas na soma desses dois valores

# print('Algoritmo para calcular quantas horas estão contidas na soma de dois valores de horas e minutos no formato HHMM')
# tempo1=int(input('Digite o primeiro valor em H e M no formato HHMM:'))
# tempo2=int(input('Digite o segundo valor em H e M no formato HHMM:'))
# minutos1=tempo1//100*60+tempo1%100
# print(f'Minutos do primeiro valor: {minutos1} minutos!')
# minutos2=tempo2//100*60+tempo2%100
# print(f'Minutos do segundo valor: {minutos2} minutos!')
# somaMinutos=minutos1+minutos2
# print(f'Soma dos minutos dos dois valores: {somaMinutos} minutos!')
# horas=somaMinutos//60 # calculo usando o quociente para obter o número de horas contidas na soma dos minutos
# print(f'Na soma dos dois valores, existem {horas} horas!')

# # exercício 19
# # algoritmo que leia uma temperatura em graus Celsius e a converta para graus Fahrenheit. A fórmula de conversão é TF = (TC * 1.8) + 32.

# print('Algoritmo para converter uma temperatura de graus Celsius para graus Fahrenheit')
# tempDigitado=float(input('Digite a temperatura em graus Celsius ou Fahrenheit: '))

# tempFahrenheit=(tempDigitado*1.8)+32
# tempCelsius=(tempDigitado-32)/1.8

# print(f'A temperatura digitada foi: {tempDigitado:.2f}°C ou {tempDigitado:.2f}°F')
# print(f'A temperatura convertida é: {tempFahrenheit:.2f}°F ou {tempCelsius:.2f}°C')

