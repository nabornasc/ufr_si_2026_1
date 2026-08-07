"""
LISTA 2 - ESTRUTURAS DE DECISÃO/CONDICIONAIS
Exercícios com operadores lógicos e estruturas if/elif/else.

Autor: Nabor N. Silva (revisado)
Versão: 2.0
"""

import random


def exercicio_1() -> None:
    """Compara dois números e verifica se são iguais ou diferentes."""
    print("\n=== EXERCÍCIO 1: Comparação de Números ===")
    try:
        a: int = int(input("Digite o valor de A: "))
        b: int = int(input("Digite o valor de B: "))
        
        if a > b:
            print(f"{a} é maior que {b}")
        elif a == b:
            print(f"{a} é igual a {b}")
        else:
            print(f"{a} é menor que {b}")
    except ValueError:
        print("Erro: Digite números inteiros válidos!")


def exercicio_2() -> None:
    """Menu de operações matemáticas."""
    print("\n=== EXERCÍCIO 2: Menu de Operações ===")
    print("\n[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    
    try:
        opcao: int = int(input("\nDigite a opção desejada: "))
        
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida!")
            return
        
        valor1: float = float(input("Digite o primeiro número: "))
        valor2: float = float(input("Digite o segundo número: "))
        
        operacoes = {
            1: ("Adição", valor1 + valor2),
            2: ("Subtração", valor1 - valor2),
            3: ("Multiplicação", valor1 * valor2),
            4: ("Divisão", valor1 / valor2 if valor2 != 0 else None)
        }
        
        nome_op, resultado = operacoes[opcao]
        
        if resultado is None:
            print("Erro: Divisão por zero!")
        else:
            print(f"O resultado da {nome_op} é: {resultado:,.2f}")
    except ValueError:
        print("Erro: Digite valores válidos!")


def exercicio_3() -> None:
    """Classifica pessoa por idade."""
    print("\n=== EXERCÍCIO 3: Classificação por Idade ===")
    try:
        idade: int = int(input("Digite a idade: "))
        
        if idade < 12:
            print("A pessoa é uma criança.")
        elif idade <= 18:
            print("A pessoa é um adolescente.")
        else:
            print("A pessoa é um adulto.")
    except ValueError:
        print("Erro: Digite uma idade válida!")


def exercicio_4() -> None:
    """Classifica eleitor por idade."""
    print("\n=== EXERCÍCIO 4: Classificação Eleitoral ===")
    try:
        idade: int = int(input("Digite a idade: "))
        
        if idade < 16:
            print("A pessoa é não-eleitor.")
        elif idade < 18 or idade >= 65:
            print("A pessoa é eleitor facultativo.")
        else:
            print("A pessoa é eleitor obrigatório.")
    except ValueError:
        print("Erro: Digite uma idade válida!")


def exercicio_5() -> None:
    """Classifica temperatura."""
    print("\n=== EXERCÍCIO 5: Classificação de Temperatura ===")
    try:
        temperatura: float = float(input("Digite a temperatura em graus C: "))
        
        if temperatura < 15:
            classificacao = "Frio"
        elif temperatura <= 30:
            classificacao = "Moderado"
        else:
            classificacao = "Quente"
        
        print(f"A temperatura é classificada como {classificacao}.")
    except ValueError:
        print("Erro: Digite uma temperatura válida!")


def exercicio_6() -> None:
    """Classifica desempenho de aluno."""
    print("\n=== EXERCÍCIO 6: Classificação de Aluno ===")
    try:
        nota1: float = float(input("Digite a primeira nota: "))
        nota2: float = float(input("Digite a segunda nota: "))
        nota3: float = float(input("Digite a terceira nota: "))
        
        media: float = (nota1 + nota2 + nota3) / 3
        
        if media < 5:
            status = "Reprovado"
        elif media <= 7:
            status = "Recuperacao"
        else:
            status = "Aprovado"
        
        print(f"Media: {media:.2f} - Aluno {status}")
    except ValueError:
        print("Erro: Digite notas válidas!")


def exercicio_7() -> None:
    """Classifica IMC."""
    print("\n=== EXERCÍCIO 7: Calculo de IMC ===")
    try:
        peso: float = float(input("Digite o peso (kg): "))
        altura: float = float(input("Digite a altura (m): "))
        
        imc: float = peso / (altura ** 2)
        
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif imc <= 24.9:
            categoria = "Peso normal"
        else:
            categoria = "Acima do peso"
        
        print(f"IMC: {imc:.2f} - {categoria}")
    except (ValueError, ZeroDivisionError):
        print("Erro: Digite valores válidos!")


def exercicio_8() -> None:
    """Aplica desconto por valor."""
    print("\n=== EXERCÍCIO 8: Calculo de Desconto ===")
    try:
        valor_compra: float = float(input("Digite o valor da compra (R$): "))
        
        if valor_compra < 100:
            desconto = valor_compra * 0.05
            percentual = 5
        elif valor_compra <= 500:
            desconto = valor_compra * 0.10
            percentual = 10
        else:
            desconto = valor_compra * 0.15
            percentual = 15
        
        valor_final: float = valor_compra - desconto
        print(f"Desconto de {percentual}%: R$ {desconto:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
    except ValueError:
        print("Erro: Digite um valor válido!")


def exercicio_9() -> None:
    """Sorteio de número."""
    print("\n=== EXERCÍCIO 9: Sorteio de Número ===")
    numero_sorteado: int = random.randint(1, 6)
    
    try:
        numero_usuario: int = int(input("Digite um número de 1 a 6: "))
        
        if numero_usuario == numero_sorteado:
            print("Parabéns! Você acertou!")
        else:
            print(f"Que pena! O número sorteado foi {numero_sorteado}.")
    except ValueError:
        print("Erro: Digite um número válido!")


def exercicio_10() -> None:
    """Previsao de tempo aleatória."""
    print("\n=== EXERCÍCIO 10: Previsao do Tempo ===")
    numero_sorteado: int = random.randint(1, 3)
    
    previsoes = {
        1: "Ensolarado",
        2: "Nublado",
        3: "Chuvoso"
    }
    
    print(f"Previsao: {previsoes[numero_sorteado]}")


def exercicio_11() -> None:
    """Sorteio de prêmio."""
    print("\n=== EXERCÍCIO 11: Sorteio de Prêmio ===")
    numero_sorteado: int = random.randint(1, 100)
    
    if 1 <= numero_sorteado <= 33:
        premio = "Bronze"
    elif 34 <= numero_sorteado <= 66:
        premio = "Prata"
    else:
        premio = "Ouro"
    
    print(f"Número sorteado: {numero_sorteado}")
    print(f"Você ganhou um prêmio de {premio}!")


def exercicio_12() -> None:
    """Sorteio de caminho."""
    print("\n=== EXERCÍCIO 12: Escolha de Caminho ===")
    numero_sorteado: int = random.randint(1, 3)
    
    caminhos = {
        1: "Floresta",
        2: "Montanha",
        3: "Deserto"
    }
    
    print(f"Seu caminho é o da {caminhos[numero_sorteado]}!")


def exercicio_13() -> None:
    """Ordena dois números."""
    print("\n=== EXERCÍCIO 13: Ordenacao de Números ===")
    try:
        num1: int = int(input("Digite o primeiro número: "))
        num2: int = int(input("Digite o segundo número: "))
        
        if num1 == num2:
            print(f"Os números são iguais: {num1}")
        elif num1 < num2:
            print(f"Ordem crescente: {num1}, {num2}")
        else:
            print(f"Ordem crescente: {num2}, {num1}")
    except ValueError:
        print("Erro: Digite números inteiros válidos!")


def exercicio_14() -> None:
    """Par ou Impar contra computador."""
    print("\n=== EXERCÍCIO 14: Par ou Impar ===")
    
    try:
        escolha_usuario = input("Escolha P (Par) ou I (Impar): ").strip().upper()
        if escolha_usuario not in ['P', 'I']:
            print("Escolha inválida!")
            return
        
        numero_usuario: int = int(input("Digite um número de 1 a 10: "))
        if not 1 <= numero_usuario <= 10:
            print("Número fora do intervalo!")
            return
        
        numero_maquina: int = random.randint(1, 10)
        soma: int = numero_usuario + numero_maquina
        resultado = 'P' if soma % 2 == 0 else 'I'
        
        print(f"\nVocê escolheu: {'Par' if escolha_usuario == 'P' else 'Impar'}")
        print(f"Computador escolheu: {'Par' if resultado == 'P' else 'Impar'}")
        print(f"Soma: {numero_usuario} + {numero_maquina} = {soma}")
        
        if resultado == escolha_usuario:
            print("Você ganhou!")
        else:
            print("Você perdeu!")
    except ValueError:
        print("Erro: Digite valores válidos!")


def exercicio_15() -> None:
    """Verifica se números são iguais."""
    print("\n=== EXERCÍCIO 15: Comparacao Simples ===")
    try:
        num1: int = int(input("Digite o primeiro número: "))
        num2: int = int(input("Digite o segundo número: "))
        
        if num1 == num2:
            print(f"Os números {num1} e {num2} são iguais!")
        else:
            print(f"Os números {num1} e {num2} são diferentes!")
    except ValueError:
        print("Erro: Digite números inteiros válidos!")


def menu_principal() -> None:
    """Menu principal para selecao de exercicios."""
    opcoes = {
        '1': ('Comparacao de Números', exercicio_1),
        '2': ('Menu de Operacoes', exercicio_2),
        '3': ('Classificacao por Idade', exercicio_3),
        '4': ('Classificacao Eleitoral', exercicio_4),
        '5': ('Classificacao de Temperatura', exercicio_5),
        '6': ('Classificacao de Aluno', exercicio_6),
        '7': ('Calculo de IMC', exercicio_7),
        '8': ('Calculo de Desconto', exercicio_8),
        '9': ('Sorteio de Número', exercicio_9),
        '10': ('Previsao do Tempo', exercicio_10),
        '11': ('Sorteio de Prêmio', exercicio_11),
        '12': ('Escolha de Caminho', exercicio_12),
        '13': ('Ordenacao de Números', exercicio_13),
        '14': ('Par ou Impar', exercicio_14),
        '15': ('Comparacao Simples', exercicio_15),
    }
    
    while True:
        print("\n" + "="*60)
        print("LISTA 2 - ESTRUTURAS DE DECISAO/CONDICIONAIS")
        print("="*60)
        for key, (desc, _) in opcoes.items():
            print(f"[{key:2}] {desc}")
        print("[0] Sair")
        print("="*60)
        
        escolha = input("Escolha uma opcao: ").strip()
        
        if escolha == '0':
            print("Até logo!")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()
        else:
            print("Opcao inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
