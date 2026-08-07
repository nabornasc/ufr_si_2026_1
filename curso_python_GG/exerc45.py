# Jogo JOKENPO

from os import name, system
from random import randint
from time import sleep

cls = lambda: system("cls") if name == "nt" else system("clear")

cls()

opc = {1: "Pedra", 2: "Papel", 3: "Tesoura"}


def jogar():
    print(f"Bem-vindo ao Jogo!\n {'=' * 10} JOKENPO! {'=' * 10}")

    jogador = int(
        input(
            "Escolha!\n 1 para Pedra\n 2 para Papel\n 3 para Tesoura\n 0 para sair\n Digite sua escolha: "
        )
    )

    computador = randint(1, 3)

    print(f"{'=' * 30}")
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!")
    sleep(1)

    print(f"{'-=' * 15}")
    print(f"Você escolheu {opc[jogador]}.")
    print(f"O computador escolheu {opc[computador]}.")
    print(f"{'-=' * 15}")

    if (
        jogador == 1
        and computador == 3
        or jogador == 2
        and computador == 1
        or jogador == 3
        and computador == 2
    ):
        print("Você ganhou!\n")
    elif jogador == computador:
        print("Empate!\n")
    else:
        print("Você perdeu!\n")


jogar()
