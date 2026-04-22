# Lista 4 - Desisoes multiplas

# from posixpath import sep


# ladA, ladB, ladC = map(int,(input('Digite as medidas dos lados do triangulo A, B, C: ') for _ in range(3)))

# if ladA+ladB>ladC and ladA+ladC>ladB and ladB+ladC>ladA:
#     if ladA==ladB==ladC:
#         print('Triangulo Equilatero')

#     elif ladA==ladB or ladA==ladC or ladB==ladC:
#         print('Triangulo Isosceles')

#     else:
#         print('Triangulo Escaleno')
# else:
#     print('Triangulo Invalido')


# exercício 2

# idAluno=input('Digite aqui codigo ID do aluno: ')
# nota1,nota2,nota3=[float(input(f'Digite aqui a nota P{n+1} do aluno: ')) for n in range(3)]
# mediaEx=float(input('Digite aqui a media dos exercicios: '))

# mediaFinal=(nota1+nota2*2+nota3*3+mediaEx)/7

# print(f'\nAluno ID: {idAluno} com notas P1= {nota1}, P2= {nota2}, e P3= {nota3}')
# print(f'\nCom media exercicios {mediaEx}')
# print(f'\nTeve media aproveitamento {mediaFinal:.2f}', "Aluno Aprovado" if mediaFinal>=6 else 'Aluno Reprovado')

# exercício 3

# peso=float(input('Digite o seu peso em Kg: '))
# altura=float(input('Digite sua altura em metros ex: 1.70: '))

# imc=peso/(altura**2)

# if imc>30:
#     print(f'\nSeu IMC é {imc:.2f}, classificado como Obesidade Morbida')
# elif imc>=25:
#     print(f'\nSeus IMC é {imc:.2f}, classificado como Obesidade')
# elif imc>=18.5:
#     print(f'\nSeus IMC é {imc:.2f}, classificado como Peso Normal')
# else:
#     print(f'\nSeus IMC é {imc:.2f}, classificado como Abaixo do peso')

# exercício 4
# import random
# print('Bem vindo ao Magic 8-Ball ')

# while True:
#     pergunta=input('Digite sua pergunta ou "sair": ')
#     if pergunta=='sair':
#         break
#     else:
#         resposta=random.randint(1,8)
#         if resposta==1:
#             print('Sim')
#         elif resposta==2:
#             print('Nao')
#         elif resposta==3:
#             print('Provavelmente sim')
#         elif resposta==4:
#             print('Provavelmente não')
#         elif resposta==5:
#             print('Não posso prever agora.')
#         elif resposta==6:
#             print('Concentre-se e pergunte novamente.')
#         elif resposta==7:
#             print('Melhor não te dizer agora.')
#         elif resposta==8:
#             print('Pergunte novamente mais tarde.')

# exercício 5
# import random

# print('Bem vindo a Horgwarts!\n Sente-se em breve sera chamado. =}')
# nome=input('\nOlá jovem aluno, qual seu nome? ') 

# print(f'\n{nome} seja bem-vindo ao castelo de Hogwarts, onde o mago e o feiticeiro se reúnem para ensinar os jovens magos a magia da escola!')
# desejo=input(f'\n{nome} escolha uma das opções abaixo: \n1 - Entra na CASA GRIFINÓRIA \n2 - Entra na CASA SONSERINA \n3 - Entra na CASA CORVINAL \n4 - Entra na CASA LUFA-LUFA \nQual é seu Desejo? ')
# escolha=random.randint(1,4)

# if escolha==1:
#     print(nome,'Seja bem-vindo a CASA GRIFINÓRIA!','\nÉ bom que sua bravura, coragem, ousadia e cavalheirismo se alinham com sua ALMA!' if desejo=='1' else '\nAcredito que seu caminho aqui seja o correto!')

# elif escolha==2:
#     print(nome,'Seja bem-vindo a CASA SONSERINA!','\nÉ bom que sua ambição, astúcia, engenhosidade e autopreservação se alinham com sua ALMA!' if desejo=='2' else '\nAcredito que seu caminho aqui seja o correto!')

# elif escolha==3:
#     print(nome,'Seja bem-vindo a CASA CORVINAL!','\nÉ bom que sua inteligência, sabedoria, criatividade e aprendizado se alinham com sua ALMA!' if desejo=='3' else '\nAcredito que seu caminho aqui seja o correto!')

# elif escolha==4:
#     print(nome,'Seja bem-vindo a CASA LUFA-LUFA!','\nÉ bom que sua lealdade, paciência, trabalho duro e honestidade se alinham com sua ALMA!' if desejo=='4' else '\nAcredito que seu caminho aqui seja o correto!')

# exercicio 6

# diaSemana=input('Digite um dia da semana "1 a 7": ')

# if diaSemana=='1':
#     print('\nEm Portugues é Domingo; \nEm Ingles é  Sunday; \nEm Espanhol é Domingo.')
# elif diaSemana=='2':
#     print('\nEm Portugues é Segunda-feira; \nEm Ingles é Monday; \nEm Espanhol é Lunes.')
# elif diaSemana=='3':
#     print('\nEm Portugues é Terca-feira; \nEm Ingles é Tuesday; \nEm Espanhol é Martes.')
# elif diaSemana=='4':
#     print('\nEm Portugues é Quarta-feira; \nEm Ingles é Wednesday; \nEm Espanhol é Miércoles.')
# elif diaSemana=='5':
#     print('\nEm Portugues é Quinta-feira; \nEm Ingles é Thursday; \nEm Espanhol é Jueves.')
# elif diaSemana=='6':
#     print('\nEm Portugues é Sexta-feira; \nEm Ingles é Friday; \nEm Espanhol é Viernes.')
# elif diaSemana=='7':
#     print('\nEm Portugues é Sabado; \nEm Ingles é Saturday; \nEm Espanhol é Sabado.')

# =================================================================

# dias = [
#     ('Domingo', 'Sunday', 'Domingo'),
#     ('Segunda-feira', 'Monday', 'Lunes'),
#     ('Terça-feira', 'Tuesday', 'Martes'),
#     ('Quarta-feira', 'Wednesday', 'Miércoles'),
#     ('Quinta-feira', 'Thursday', 'Jueves'),
#     ('Sexta-feira', 'Friday', 'Viernes'),
#     ('Sábado', 'Saturday', 'Sábado')
# ]
# while True:
#     try:
#         dia = int(input('Digite um dia da semana (1 a 7): '))
#         pt, en, es = dias[dia-1]
#         print(f'\nEm Português é {pt};\nEm Inglês é {en};\nEm Espanhol é {es}.')
#         break
#     except (ValueError, IndexError):
#         print('Valor inválido! Digite um número inteiro de 1 a 7.')

# =================================================================

# exercicio 7

# while True:
#     idadeCompetidor=int(input('Digite a idade do competidor (ou 99 para encerrar): '))

#     if idadeCompetidor<5:
#         print('Não qualificado para competição.')
#     elif idadeCompetidor==99:
#         break
#     else:
#         if idadeCompetidor>=18:
#             print('Sua categoria é Sênior.')
#         elif idadeCompetidor>=14:
#             print('Sua categoria é Juvenil: B')
#         elif idadeCompetidor>=11:
#             print('Sua categoria é Juvenil: A')
#         elif idadeCompetidor>=8:
#             print('Sua categoria é Infantil: B')
#         else:
#             print('Sua categoria é Infantil: A')

# ================================================================

# exercicio 8

while True:
    pesoTerra=float(input('Digite um peso em kg: '))
    opcaoPlaneta=int(input('Digite 0 para sair,\nDigite 1 para Mercúrio,\nDigite 2 para Vênus,\nDigite 3 para Marte,\nDigite 4 para Jupiter,\nDigite 5 para Saturno,\nDigite 6 para Urano,\nDigite 7 para Netuno,\n\nOpção:  '))
    
    if opcaoPlaneta>7:
        print('\nOpção inválida! Tente novamente.')
    
    elif opcaoPlaneta!=0:
        
        pesoPlaneta =  {
            (1, 'Mercúrio'): 0.38,
            (2, 'Vênus'): 0.90,
            (3, 'Marte'): 0.38,
            (4, 'Jupiter'): 2.53,
            (5, 'Saturno'): 1.06,
            (6, 'Urano'): 0.89,
            (7, 'Netuno'): 1.14
        }

        for chave, valor in pesoPlaneta.items():
            if chave[0]==opcaoPlaneta:
                print(f'\nSeu peso em {chave[1]} é {pesoTerra*valor:.2f} kg')

    else:
        break


