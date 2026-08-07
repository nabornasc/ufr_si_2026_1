"""
LISTA 4 - DECISÕES MÚLTIPLAS
Exercícios com múltiplas condições e estruturas complexas.

Autor: Nabor N. Silva (revisado)
Versão: 2.0
"""

import random
import math


def exercicio_1() -> None:
    """Classifica triângulo por seus lados."""
    print("\n=== EXERCÍCIO 1: Classificacao de Triângulo ===")
    try:
        lado_a: float = float(input("Digite o lado A: "))
        lado_b: float = float(input("Digite o lado B: "))
        lado_c: float = float(input("Digite o lado C: "))
        
        if (lado_a + lado_b > lado_c and 
            lado_a + lado_c > lado_b and 
            lado_b + lado_c > lado_a):
            
            if lado_a == lado_b == lado_c:
                print("Triângulo Equilátero")
            elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
                print("Triângulo Isósceles")
            else:
                print("Triângulo Escaleno")
        else:
            print("Triângulo Inválido")
    except ValueError:
        print("Erro: Digite valores válidos!")


def exercicio_2() -> None:
    """Calcula media de aluno com pesos."""
    print("\n=== EXERCÍCIO 2: Media Ponderada de Aluno ===")
    try:
        id_aluno: str = input("Digite o ID do aluno: ")
        nota1: float = float(input("Digite a nota P1: "))
        nota2: float = float(input("Digite a nota P2: "))
        nota3: float = float(input("Digite a nota P3: "))
        media_exercicios: float = float(input("Digite a media de exercícios: "))
        
        media_final: float = (nota1 + nota2*2 + nota3*3 + media_exercicios) / 7
        
        status: str = "Aprovado" if media_final >= 6 else "Reprovado"
        print(f"\nAluno {id_aluno}: Média = {media_final:.2f} - {status}")
    except ValueError:
        print("Erro: Digite valores válidos!")


def exercicio_3() -> None:
    """Classifica IMC com categorias."""
    print("\n=== EXERCÍCIO 3: Classificacao de IMC ===")
    try:
        peso: float = float(input("Digite o peso (kg): "))
        altura: float = float(input("Digite a altura (m): "))
        
        imc: float = peso / (altura ** 2)
        
        if imc > 30:
            categoria = "Obesidade Mórbida"
        elif imc >= 25:
            categoria = "Obesidade"
        elif imc >= 18.5:
            categoria = "Peso Normal"
        else:
            categoria = "Abaixo do peso"
        
        print(f"IMC: {imc:.2f} - {categoria}")
    except (ValueError, ZeroDivisionError):
        print("Erro: Digite valores válidos!")


def exercicio_4() -> None:
    """Magic 8-Ball."""
    print("\n=== EXERCÍCIO 4: Magic 8-Ball ===")
    respostas = {
        1: "Sim",
        2: "Não",
        3: "Provavelmente sim",
        4: "Provavelmente não",
        5: "Não posso prever agora",
        6: "Concentre-se e pergunte novamente",
        7: "Melhor não te dizer agora",
        8: "Pergunte novamente mais tarde"
    }
    
    while True:
        pergunta: str = input("\nDigite sua pergunta (ou 'sair'): ").strip()
        if pergunta.lower() in ['sair', 'exit', 'fim']:
            break
        
        resposta: int = random.randint(1, 8)
        print(f"Resposta: {respostas[resposta]}")


def exercicio_5() -> None:
    """Sistema de casas Hogwarts."""
    print("\n=== EXERCÍCIO 5: Distribuicao de Casas Hogwarts ===")
    nome: str = input("Qual seu nome? ").strip()
    print(f"\n{nome}, bem-vindo ao castelo de Hogwarts!")
    
    escolha: int = random.randint(1, 4)
    casas = {
        1: "GRIFINÓRIA",
        2: "SONSERINA",
        3: "CORVINAL",
        4: "LUFA-LUFA"
    }
    
    print(f"{nome} foi distribuído para a casa {casas[escolha]}!")


def exercicio_6() -> None:
    """Traduz dia da semana."""
    print("\n=== EXERCÍCIO 6: Traducao de Dias ===")
    dias = [
        ("Domingo", "Sunday", "Domingo"),
        ("Segunda-feira", "Monday", "Lunes"),
        ("Terca-feira", "Tuesday", "Martes"),
        ("Quarta-feira", "Wednesday", "Miercoles"),
        ("Quinta-feira", "Thursday", "Jueves"),
        ("Sexta-feira", "Friday", "Viernes"),
        ("Sábado", "Saturday", "Sabado")
    ]
    
    try:
        dia: int = int(input("Digite um dia (1-7): "))
        if 1 <= dia <= 7:
            pt, en, es = dias[dia-1]
            print(f"Português: {pt}\nInglês: {en}\nEspanhol: {es}")
        else:
            print("Erro: Digite um número de 1 a 7!")
    except ValueError:
        print("Erro: Digite um número válido!")


def exercicio_7() -> None:
    """Categorias de competidores."""
    print("\n=== EXERCÍCIO 7: Categorias de Competicao ===")
    categorias = {
        (0, 4): "Não qualificado",
        (5, 7): "Infantil A",
        (8, 10): "Infantil B",
        (11, 13): "Juvenil A",
        (14, 17): "Juvenil B",
        (18, 999): "Sênior"
    }
    
    while True:
        try:
            idade: int = int(input("Digite a idade (99 para sair): "))
            if idade == 99:
                break
            
            categoria: str = ""
            for (min_idade, max_idade), cat in categorias.items():
                if min_idade <= idade <= max_idade:
                    categoria = cat
                    break
            
            print(f"Categoria: {categoria}")
        except ValueError:
            print("Erro: Digite um número válido!")


def exercicio_8() -> None:
    """Peso em outros planetas."""
    print("\n=== EXERCÍCIO 8: Peso em Outros Planetas ===")
    planetas = {
        1: ("Mercúrio", 0.38),
        2: ("Vênus", 0.90),
        3: ("Marte", 0.38),
        4: ("Júpiter", 2.53),
        5: ("Saturno", 1.06),
        6: ("Urano", 0.89),
        7: ("Netuno", 1.14)
    }
    
    while True:
        try:
            print("\n[1] Mercúrio [2] Vênus [3] Marte [4] Júpiter")
            print("[5] Saturno [6] Urano [7] Netuno [0] Sair")
            opcao: int = int(input("Escolha um planeta: "))
            
            if opcao == 0:
                break
            elif opcao in planetas:
                peso_terra: float = float(input("Digite seu peso (kg): "))
                nome_planeta, gravidade = planetas[opcao]
                peso_planeta: float = peso_terra * gravidade
                print(f"Seu peso em {nome_planeta}: {peso_planeta:.2f} kg")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Digite valores válidos!")


def exercicio_9() -> None:
    """Funcao especial."""
    print("\n=== EXERCÍCIO 9: Funcao Especial ===")
    try:
        valor_real: float = float(input("Digite um valor real: "))
        
        if valor_real <= 1:
            resultado: float = 1
        elif valor_real <= 2:
            resultado = 2
        elif valor_real <= 3:
            resultado = valor_real ** 2
        else:
            resultado = valor_real ** 3
        
        print(f"f({valor_real}) = {resultado}")
    except ValueError:
        print("Erro: Digite um valor válido!")


def exercicio_10() -> None:
    """Calculo de aumento por profissao."""
    print("\n=== EXERCÍCIO 10: Aumento Salarial por Profissao ===")
    profissoes = {
        'm': ('Médico', 0.20),
        'e': ('Engenheiro', 0.15),
        'p': ('Professor', 0.10),
        'o': ('Outro', 0.05)
    }
    
    while True:
        try:
            profissao: str = input("Digite profissão [M/E/P/O] (ou sair): ").lower()
            
            if profissao in ['sair', 'exit', 'fim']:
                break
            elif profissao in profissoes:
                salario: float = float(input("Digite o salário: R$ "))
                nome, percentual = profissoes[profissao]
                novo_salario: float = salario * (1 + percentual)
                print(f"{nome}: R$ {novo_salario:,.2f}")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Erro: Digite valores válidos!")


def exercicio_11() -> None:
    """Desconto por condicao de pagamento."""
    print("\n=== EXERCÍCIO 11: Desconto por Forma de Pagamento ===")
    condicoes = {
        'v': ('À Vista', 0.15, True),
        'c': ('Cheque', 0.15, True),
        'cc': ('Cartão de Crédito', 0.10, True),
        'cc2': ('Crédito em 2x', 0, False),
        'cc3': ('Crédito em 3x', 0.10, False)
    }
    
    try:
        valor: float = float(input("Digite o valor da mercadoria: R$ "))
        print("\n[V] À Vista [C] Cheque [CC] Cartão Crédito [CC2] 2x [CC3] 3x")
        condicao: str = input("Digite a condicao: ").lower()
        
        if condicao in condicoes:
            nome, taxa, eh_desconto = condicoes[condicao]
            if eh_desconto:
                valor_final: float = valor - (valor * taxa)
            else:
                valor_final = valor + (valor * taxa)
            
            print(f"{nome}: R$ {valor_final:,.2f}")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Erro: Digite valores válidos!")


def exercicio_12() -> None:
    """Maior e menor entre 4 valores."""
    print("\n=== EXERCÍCIO 12: Maior e Menor Entre 4 Valores ===")
    try:
        valores: list = [float(x) for x in input("Digite 4 valores (separados por espaço): ").split()]
        
        if len(valores) == 4:
            print(f"Maior: {max(valores)}")
            print(f"Menor: {min(valores)}")
        else:
            print("Erro: Digite exatamente 4 valores!")
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")


def menu_principal() -> None:
    """Menu principal para selecao de exercicios."""
    opcoes = {
        '1': ('Classificacao de Triângulo', exercicio_1),
        '2': ('Media Ponderada', exercicio_2),
        '3': ('Classificacao de IMC', exercicio_3),
        '4': ('Magic 8-Ball', exercicio_4),
        '5': ('Casas Hogwarts', exercicio_5),
        '6': ('Traducao de Dias', exercicio_6),
        '7': ('Categorias de Competicao', exercicio_7),
        '8': ('Peso em Planetas', exercicio_8),
        '9': ('Funcao Especial', exercicio_9),
        '10': ('Aumento Salarial', exercicio_10),
        '11': ('Desconto Pagamento', exercicio_11),
        '12': ('Maior e Menor', exercicio_12),
    }
    
    while True:
        print("\n" + "="*60)
        print("LISTA 4 - DECISÕES MÚLTIPLAS")
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
