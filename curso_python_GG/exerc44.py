from os import name, system

cls = lambda: system("cls") if name == "nt" else system("clear")

cls()

print("{:=^50}".format(" Lojas Nascimento "))
preco = float(input("Digite o preço do produto: R$ "))

opc = int(
    input("""Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite a opção: """)
)

if opc == 1:
    preco_final = preco - (preco * 10 / 100)
elif opc == 2:
    preco_final = preco - (preco * 5 / 100)
elif opc == 3:
    preco_final = preco
    parcela = preco_final / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros.")
elif opc == 4:
    preco_final = preco + (preco * 20 / 100)
    parcela = preco_final / 3
    print(f"Sua compra será parcelada em 3x de R$ {parcela:.2f} com juros.")

print(f"O preço final do produto é R$ {preco_final:.2f}")
