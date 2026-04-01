'''Programa: CalculoDobro
Descrição: Este programa solicita um valor ao usuário e calcula o dobro desse valor.
Autor: NaborNSilva
Data de Criação: 29-03-26
Versão: 1.0
Bibliotecas Utilizadas: Nenhuma
Este programa foi desenvolvido como exemplo de implementação em Python.
O objetivo é demonstrar o uso de entrada e saída de dados, além de operações aritméticas básicas.
'''

'''Declaração de variáveis
numero    # variável que armazenará o valor informado pelo usuário
            do tipo decimal (ponto flutuante)
quadrado    # variável que armazenará o resultado do dobro
'''
'''
numero = 0
quadrado = 0
FATOR = 3

# entrada de dados

numero = float(input('Digite aqui um numero: '))

# processo de calculo

quadrado = numero**FATOR

# saida

print(f'O quadrado de {numero} é {quadrado:.3f}.')
'''

'''tipos de variaveis
inteiro: int
decimal: float
texto: str
booleano: bool
'''
'''
numero=int(input('Digite um numero inteiro: '))
numero=numero+1
print(f'Numero da variavel é {numero}')
'''
'''
a=10
a=a+1
print(f'O valor da variavel é {a}')
'''
'''
a=int(input('Digite um numero inteiro: '))
b=int(input('Digite outro numero inteiro: '))

soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b

print(f'A soma de {a} e {b} é {soma}.') 
print(f'A subtracao de {a} e {b} é {subtracao}.') 
print(f'A multiplicacao de {a} e {b} é {multiplicacao}.') 
print(f'A divisao de {a} e {b} é {divisao}.') 
'''
'''
potencia=2
x=float(input('Digite um numero decimal: '))
result=x**potencia
print(f'O numero {x} elevado a potencia {potencia} é {result:.2f}.')
'''
'''
tipoDeRaiz=int(input('Digite 2 para raiz quadrada ou 3 para raiz cubica ou etc: '))

numero=float(input('Digite um numero decimal: '))
calculo=numero**(1/tipoDeRaiz)
print(f'A raiz {tipoDeRaiz} de {numero} é {calculo:.2f}.')
'''

# a=float(input('Digite um numero decimal: '))
# b=float(input('Digite outro numero decimal: '))

# divisao=a/b
# quociente=a//b
# resto=a%b

# print(f'A divisao de {a} por {b} é {divisao:.2f}.')
# print(f'O quociente da divisao de {a} por {b} é {quociente:.2f}.')
# print(f'O resto da divisao de {a} por {b} é {resto:.2f}.')

# numero=int(input('Digite um numero inteiro: '))
# dezena=numero//10
# unidade=numero%10
# # print(f'O inverso de {numero} é {unidade}{dezena}.') # para numeros de 2 digitos
# def inverso(numero): # para numeros de 2 ou mais digitos, usando string
#     return str(numero)[::-1]
# print(f'O inverso de {numero} é {inverso(numero)}.') # para numeros de 2 ou mais digitos, usando fatiamento de string

# horas_4dig=int(input('Digite um numero inteiro de 4 digitos representando horas: '))
# horas=horas_4dig//100
# # print(horas)
# minutos=horas_4dig%100
# # print(minutos)
# convertidoSegundos=horas*3600+minutos*60
# convertidoMinutos=convertidoSegundos/60
# print(f'{horas} horas e {minutos} minutos representam {convertidoMinutos} minutos.')
# print(f'{convertidoMinutos} minutos representam {convertidoSegundos} segundos.')

# valorInical=float(input('Digite um valor inicial: '))
# taxa=float(input('Digite a taxa de crescimento (em porcentagem): '))
# valorFinalComAcrescimo=valorInical*(1+taxa/100)
# valorFinalComDesconto=valorInical*(1-taxa/100)
# print(f'O valor final após o crescimento de {taxa}% é {valorFinalComAcrescimo:.2f}.')
# print(f'O valor final após o desconto de {taxa}% é {valorFinalComDesconto:.2f}.')

# print('Este programa calcula a expressão\n y = (a^potencia1 / b^potencia2 + c)^(1/raiz).')
# a=float(input('Digite um numero decimal para A: '))
# b=float(input('Digite outro numero decimal para B: '))
# potencia1=int(input('Digite a potencia para o numero a: '))
# potencia2=int(input('Digite a potencia para o numero b: '))
# c=float(input('Digite um numero decimal C para ser somado: '))
# raiz=int(input('Digite a raiz para o resultado final: '))
# y=((a**potencia1)/(b**potencia2+c))**1/raiz
# print(f'O resultado da expressão é {y:.2f}.')

# a=int(input('Digite 1º numero inteiro: '))
# b=int(input('Digite 2º numero inteiro: '))
# c=a 
# d=b
# print(f'Antes da troca: a={a}, b={b}')
# print(f'Depois da troca: a={d}, b={c}')

# a=int(input('Numero a ser previsto, antecessor e sucessor: '))
# antecessor=a-1
# sucessor=a+1
# print(f'O numero {a} tem como antecessor {antecessor} e sucessor {sucessor}.')

# numReal=float(input('Digite um numero real, que vamos separar o inteiro; do fracionado; e o arredondado: '))
# parteInteira=int(numReal)
# parteFracionada=numReal-parteInteira
# parteArredondada=round(numReal)
# print(f'O numero real digitado é {numReal}.')
# print(f'A parte inteira do numero é {parteInteira}.')
# print(f'A parte fracionada do numero é {parteFracionada:.2f}.')
# print(f'O numero arredondado é {parteArredondada}.')

# # O programa deve receber a razão da PA e a posição do termo desejado como entrada. Ambos os valores devem ser números reais.
# print('Formular geral da PA: a(n) = a(1) + (n - 1) * r,\nonde a(n) é o termo na posição n,\na(1) é o primeiro termo da PA,\nr é a razão da PA e n é a posição do termo desejado.')
# razao=float(input('Digite a razão da PA: '))
# posicao=int(input('Digite a posição do termo desejado: '))
# # O programa deve calcular o termo da PA usando a fórmula: termo = primeiro_termo + (posição - 1) * razão. O primeiro termo da PA é considerado como 0.
# primeiro_termo=int(input('Digite o primeiro termo da PA: '))
# termo=primeiro_termo+(posicao-1)*razao
# # O programa deve exibir o termo da PA correspondente à posição desejada.
# print(f'O termo da PA na posição {posicao} é {termo:.2f}.')

# #algoritmo que efetue o cálculo da quantidade de litros de combustível gastos em uma viagem
# distancia=float(input('Digite a distancia da viagem em km: '))
# consumo=float(input('Digite o consumo do veículo em km/l: '))
# litros_gastos=distancia/consumo
# print(f'Para percorrer {distancia} km, o veículo gastará {litros_gastos:.2f} litros de combustível.')
# #apresentar os valores da velocidade média, tempo gasto na viagem, distância percorrida e a quantidade de litros utilizados na viagem
# velocidade_media=float(input('Digite a velocidade média da viagem em km/h: '))
# tempo_gasto=distancia/velocidade_media
# horas=int(tempo_gasto)
# minutos=int((tempo_gasto-horas)*60)
# print(f'Para percorrer {distancia} km a uma velocidade média de {velocidade_media} km/h,\no tempo gasto na viagem será de {horas} horas e {minutos} minutos.')
