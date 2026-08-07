import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")

cls()

num = int(input("Digite um número inteiro: ").strip())

opc = int(
    input(
        "Escolha uma das bases para conversão:\n[1] Binário\n[2] Octal\n[3] Hexadecimal\nDigite a opção desejada: "
    )
)

if opc == 1:
    print(
        f"O número {num} convertido para Binário é {bin(num)[2:]}"
    )  # fatiamento da string para remover o prefixo '0b'
elif opc == 2:
    print(
        f"O número {num} convertido para Octal é {oct(num)[2:]}"
    )  # fatiamento da string para remover o prefixo '0o'
elif opc == 3:
    print(
        f"O número {num} convertido para Hexadecimal é {hex(num)[2:]}"
    )  # fatiamento da string para remover o prefixo '0x'
else:
    print("Opção inválida!")
