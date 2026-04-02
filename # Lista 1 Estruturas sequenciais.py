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

