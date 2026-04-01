#n1=int(input('Digite 1º valor Inteiro aqui: '))
#n2=int(input('Digite 2º valor Inteiro aqui: '))

#if (n1==n2):
#    print(f'Os valores {n1} e {n2} são identicos!')
#if (n1!=n2):
#    print(f'Os valores {n1} e {n2} são diferentes.')

#if (n1%2==0):
#    print(f'{n1} esse numero é PAR!')
#else:
#    print(f'{n1} esse numero é IMPAR!')
#import math
#print(f'{math.pi:.3f}')

'''
nome = "Ana",'Nabor'
idade = 30
preco = 19.987

print(f"Olá, {nome}. Você tem {idade} anos.")
print(f"O preço é R$ {preco:.2f}")
print(f"Resultado: {2 * 5} = 10")
print(f"Debug: {nome=}")
'''
'''
print('Digite a opcao desejada')
print('1 - somar')
print('2 - subtracao')
print('3 - multiplicacao')
print('4 - divisao')

opcao=int(input())

if (opcao==1):
    n1=int(input('Soma selecionada.\n Digite o 1º valor: '))
    n2=int(input(' Digite o 2º valor: '))
    print(f'O valor da soma de {n1} mais {n2} é: {n1+n2} ')
elif (opcao==2):
    n1=int(input('Subtracao selecionada.\n Digite o 1º valor: '))
    n2=int(input(' Digite o 2º valor: '))
    print(f'O valor da subtracao de {n1} menos {n2} é: {n1-n2} ')
elif (opcao==3):
    n1=int(input('Multiplicacao selecionada.\n Digite o 1º valor: '))
    n2=int(input(' Digite o 2º valor: '))
    print(f'O valor da multiplicacao de {n1} vezes {n2} é: {n1*n2} ')
elif (opcao==4):
    n1=float(input('Divisao selecionada.\n Digite o 1º valor: '))
    n2=float(input(' Digite o 2º valor: '))
    if (n1==0) or (n2==0):
        print('nao existe divisao por 0')
    else:
        print(f'O valor da divisao de {n1} por {n2} é: {n1/n2} ')
else:
    print('Opcao Invalida!')
''' 
        

        
        
        
        
        
        
        
        
        
        