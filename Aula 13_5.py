a = int(input('Quer iniciar em [0/1]: '))
b = int(input('Quer ir até [10,100,..: '))
c = int(input('Quer contar de quanto em quanto [1,2,..]: '))
d = str(input('Crescente ou decrescente [C/D]: ').lower())

for i in range(a, b + 1, c):
    if d == 'c':
        print(i)
        i += i
    elif d == 'd':
        print(b)
        b -= c
