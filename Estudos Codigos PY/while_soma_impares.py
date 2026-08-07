cont=1
somaI=0
while cont<6:
    print(f'Digite o {cont}º número: ',end="")
    num=int(input())
    if num%2!=0:
        somaI+=num
    cont+=1
print(f'A soma dos números ímpares é: {somaI}')