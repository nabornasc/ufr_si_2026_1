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

