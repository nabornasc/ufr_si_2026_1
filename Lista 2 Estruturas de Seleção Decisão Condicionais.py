# Lista 2 Estruturas de Seleção/Decisão/Condicionais 

# =========================================
'''
Seção de cabeçalho
Nome do algoritmo/programa: Lista estruturas de decisão -
Ex. 01
Função/Descrição: 1.    Escreva
um algoritmo que leia dois números inteiros.
Mostre na tela e diga se eles são iguais ou diferentes.
Autor: Waine Teixeira Júnior
Data: 31/05/2019
Número de controle de versão: 1.0
'''
# =========================================
'''
Seção de Declarações de variáveis
 
'''
# =========================================
# inicio do algoritmo/programa
 
#entrada de dados
# print ('Digite o primeiro número')
# n1 = int (input())
# print ('Digite o segundo número')
# n2 = int (input())
 
#processamento e saida
 
# if (n1 == n2):
#     print (n1, ' e ',n2,' são iguais')
# else:
#     print (n1, ' e ',n2,' são diferentes')
 
# =========================================
# fim do algoritmo/programa


# exercício 1
# algorimto que leia A e B, que serão valores inteiros digitados pelo teclado.
# Determine e mostre somente se A é maior que B. Nesse caso mostrar a mensagem:
# A é maior que B

# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))

# if A > B:
#     print("A é maior que B")
# elif A == B:
#     print("A é igual a B")
# else:
#     print("A não é maior que B")
    
# exercício 2
# algoritmo um menu de opções de operações matemáticas

# print("Menu de opções para calcular:")
# print("1. Adição")
# print("2. Subtração")
# print("3. Multiplicação")
# print("4. Divisão")

# opcao=int(input("Digite a opção desejada: "))

# if opcao == 1:
#     print("Você escolheu Adição")
#     valor1 = float(input("Digite o primeiro número: "))
#     valor2 = float(input("Digite o segundo número: "))
#     resultado = valor1 + valor2
#     print(f'O resultado da adição é: {resultado:,.2f}')

# elif opcao == 2:
#     print("Você escolheu Subtração")
#     valor1 = float(input("Digite o primeiro número: "))
#     valor2 = float(input("Digite o segundo número: "))
#     resultado = valor1 - valor2
#     print(f'O resultado da subtração é: {resultado:,.2f}')

# elif opcao == 3:
#     print("Você escolheu Multiplicação")
#     valor1 = float(input("Digite o primeiro número: "))
#     valor2 = float(input("Digite o segundo número: "))
#     resultado = valor1 * valor2
#     print(f'O resultado da multiplicação é: {resultado:,.2f}')
    
# elif opcao == 4:
#     print("Você escolheu Divisão")
#     valor1 = float(input("Digite o primeiro número: "))
#     valor2 = float(input("Digite o segundo número: "))
#     if valor2 != 0:
#         resultado = valor1 / valor2
#         print(f'O resultado da divisão é: {resultado:,.2f}')
#     else:
#         print("Erro: Divisão por zero não é permitida.")
# else:
#     print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    
# exercício 3
# algoritmo que receba a idade de uma pessoa.
# Suponha a entrada de um valor válido.
# Verifique se ela é uma criança (menor de 12 anos),
# um adolescente (entre 12 e 18 anos) ou um adulto (maior de 18 anos).

# idade=int(input('Digite a idade para verificar se é criança, adolescente ou adulto: '))
# if idade < 12:
#     print('A pessoa é uma criança.')
# else:
#     if idade >= 12 and idade <= 18:
#         print('A pessoa é um adolescente.')
#     else:
#         print('A pessoa é um adulto.')

# exercício 4
# algoritmo em que leia a idade de uma pessoa e informe a sua classe eleitoral
# idade=int(input('Digite a idade para verificar a classe eleitoral: '))
# if idade < 16:
#     print('A pessoa é não-eleitor.')
# else:
#     if idade >= 16 and idade < 18 or idade >= 65:
#         print('A pessoa é eleitor facultativo.')
#     else:
#         print('A pessoa é eleitor obrigatório.')

# exercício 5
# algoritmo que receba a temperatura em graus Celsius e classifique-a 
# como "Frio" (abaixo de 15°C), "Moderado" (entre 15°C e 30°C) 
# ou "Quente" (acima de 30°C).

# temperatura=float(input('Digite a temperatura em graus Celsius para classificar: '))
# if temperatura < 15:
#     print('A temperatura é classificada como Frio.')
# else:
#     if temperatura >= 15 and temperatura <= 30:
#         print('A temperatura é classificada como Moderado.')
#     else:
#         print('A temperatura é classificada como Quente.')

# exercício 6
# algoritmo que receba três notas de um aluno e determine se ele está 
# "Reprovado" (média abaixo de 5), em "Recuperação" 
# (média entre 5 e 7) ou "Aprovado" (média acima de 7).

# nota1=float(input('Digite a primeira nota: '))
# nota2=float(input('Digite a segunda nota: '))
# nota3=float(input('Digite a terceira nota: '))

# media = (nota1 + nota2 + nota3) / 3

# if media < 5:
#     print('O aluno está Reprovado.')
# elif media >= 5 and media <= 7:
#     print('O aluno está em Recuperação.')
# else:
#     print('O aluno está Aprovado.')

# exercício 7
# algoritmo que receba o peso de uma pessoa e classifique-a como 
# "Abaixo do peso" (IMC menor que 18.5), "Peso normal" 
# (IMC entre 18.5 e 24.9) ou "Acima do peso" (IMC maior que 24.9).

# peso=float(input('Digite o peso da pessoa em kg: '))
# altura=float(input('Digite a altura da pessoa em cm: '))

# imc=peso/((altura/100)**2)

# if imc < 18.5:
#     print(f'Seu IMC é {imc:.2f}, classificado como Abaixo do peso.')
# elif imc >= 18.5 and imc <= 24.9:
#     print(f'Seu IMC é {imc:.2f}, classificado como Peso normal.')
# else:
#     print(f'Seu IMC é {imc:.2f}, classificado como Acima do peso.')

# exercício 8
# algoritmo que receba o valor de uma compra e aplique um desconto 
# de acordo com o valor: "Desconto de 5%" (para compras abaixo de 100 
# reais), "Desconto de 10%" (para compras entre 100 e 500 reais) ou 
# "Desconto de 15%" (para compras acima de 500 reais).

# valor_compra=float(input('Digite o valor da compra em reais: '))

# if valor_compra < 100:
#     desconto = valor_compra * 0.05
#     print(f'Você recebeu um desconto de 5%. O valor da compra com desconto é: R$ {valor_compra-desconto:.2f}')
# elif valor_compra >= 100 and valor_compra <= 500:
#     desconto = valor_compra * 0.1
#     print(f'Você recebeu um desconto de 10%. O valor da compra com desconto é: R$ {valor_compra-desconto:.2f}')
# else:
#     desconto = valor_compra * 0.15
#     print(f'Você recebeu um desconto de 15%. O valor da compra com desconto é: R$ {valor_compra-desconto:.2f}')

# exercício 9
# Programa para sorteio e verificação de número digitado pelo usuário,
# mostrar se ganhou ou perdeu. 

# import random

# numeroSorteado = random.randint(1, 6)

# numeroUsuario = int(input('Digite um número entre 1 e 6 para tentar ganhar: '))

# if numeroUsuario == numeroSorteado:
#     print('Parabéns! Você acertou o número sorteado.')
# else:
#     print(f'Que pena! O número sorteado foi {numeroSorteado}.')

# exercício 10
# algoritmo que gere um número inteiro aleatório entre 1 e 3,
# onde cada número representa uma previsão do tempo. 
# O número 1 indica "Ensolarado", o número 2 indica "Nublado" e 
# o número 3 indica "Chuvoso". Exiba a previsão correspondente.

# import random

# numeroSorteado = random.randint(1, 3)

# if numeroSorteado == 1:
#     print('A previsão do tempo é: Ensolarado.')
# elif numeroSorteado == 2:
#     print('A previsão do tempo é: Nublado.')
# else:
#     print('A previsão do tempo é: Chuvoso.')

# exercício 11
# algoritmo que gere um número inteiro aleatório entre 1 e 100.
# Verifique se o número está no intervalo de 1 a 33, 34 a 66, ou 67 a 100, 
# e exiba uma mensagem correspondente: "Você ganhou um prêmio de bronze!", 
# "Você ganhou um prêmio de prata!" ou "Você ganhou um prêmio de ouro!"

# import random

# numeroSorteado = random.randint(1, 100)

# if numeroSorteado >= 1 and numeroSorteado <= 33:
#     print(f'Número sorteado: {numeroSorteado}. Você ganhou um prêmio de bronze!')
# elif numeroSorteado >= 34 and numeroSorteado <= 66:
#     print(f'Número sorteado: {numeroSorteado}. Você ganhou um prêmio de prata!')
# else:
#     print(f'Número sorteado: {numeroSorteado}. Você ganhou um prêmio de ouro!')

# exercício 12
# algoritmo que gere um número inteiro aleatório entre 1 e 3 
# para representar a escolha de um caminho em um jogo. O número 1 
# indica "Caminho da floresta", o número 2 indica "Caminho da montanha" 
# e o número 3 indica "Caminho do deserto"

# import random

# numeroSorteado = random.randint(1, 3)

# if numeroSorteado == 1:
#     print(f'{numeroSorteado} - Foi sorteado! O seu Caminho é da floresta.')
# elif numeroSorteado == 2:
#     print(f'{numeroSorteado} - Foi sorteado! O seu Caminho é da montanha.')
# else:
#     print(f'{numeroSorteado} - Foi sorteado! O seu Caminho é do deserto.')

# exercício 13
# Algoritmo que receba 2 numero inteiro e ordene-os em ordem crescente.

# num1=int(input('Digite o primeiro número inteiro: '))
# num2=int(input('Digite o segundo número inteiro: '))
# if num1 == num2:
#     print(f'Os números são iguais: {num1}, {num2}')
# else:
#     if num1 < num2:
#         print(f'Os números em ordem crescente são: {num1}, {num2}')
#     else:
#         print(f'Os números em ordem crescente são: {num2}, {num1}')

# exercício 14
# algoritmo em Python para simular a brincadeira de "Par ou Ímpar" 
# entre o usuário e o computador

import random

while True:
    escolhaUsuario = input('Escolha P = Par ou I = Ímpar: ').strip().upper()
    if escolhaUsuario in ('P', 'I'):
        break
    print('Escolha inválida. Por favor digite P ou I.')

print(f'Você escolheu {"PAR" if escolhaUsuario == "P" else "IMPAR"}')

while True:
    try:
        numeroUsuario = int(input('Digite um número de 1 a 10: '))
        if numeroUsuario < 1 or numeroUsuario > 10:
            print('Número fora do intervalo. Digite um número entre 1 e 10.')
            continue
        break
    except ValueError:
        print('Digite apenas números inteiros.')

escolhaMaquina = 'I' if escolhaUsuario == 'P' else 'P'
# print(escolhaMaquina)
print(f'\nComputador escolheu: {"Par" if escolhaMaquina == "P" else "Ímpar"}')

numeroMaquina = random.randint(1,10)
# print(numeroMaquina)
print(f'Computador jogou: {numeroMaquina}')

soma = numeroMaquina + numeroUsuario
resultado = 'P' if soma % 2 == 0 else 'I'

print(f'\nSoma: {numeroUsuario} + {numeroMaquina} = {soma} → {"Par" if resultado == "P" else "Ímpar"}')

if resultado == escolhaUsuario:
    print('\nVocê ganhou!\n')
else:
    print('\nVocê perdeu!\n')