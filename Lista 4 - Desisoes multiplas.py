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
