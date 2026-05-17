
a=int(input('Quer iniciar em [0/1]: '))
b=int(input('Quer ir até [10,100,..: '))
c=int(input('Quer contar de quanto em quanto [1,2,..]: '))

for i in range (a,b+1,c):
    print(i)
    i+=i
