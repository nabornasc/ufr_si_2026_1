flag = True
cont = int(input("Digite um numero: "))
while flag:
    if cont > 1:
        cont //= 2
        print(f"quociente = {cont}, resto = {cont%2}")
    else:
        flag = False
