num=int(input('Quantos termo da Serie de fibonacci: '))
a,b=1,1
print(a)
for cont in range(1,num):
    print(b)
    a,b=b,a+b
