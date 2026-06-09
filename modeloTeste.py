"""
ARQUIVO DE MODELO E TESTES
Exemplos de referência para práticas de programação Python.

Autor: Nabor N. Silva
Versão: 2.0
"""


def calculo_dobro(numero: float) -> float:
    """
    Calcula o dobro de um número.
    
    Args:
        numero (float): O número a ser dobrado
        
    Returns:
        float: O dobro do número
    """
    return numero * 2


def calculo_quadrado(numero: float) -> float:
    """
    Calcula o quadrado de um número.
    
    Args:
        numero (float): O número a ser elevado ao quadrado
        
    Returns:
        float: O quadrado do número
    """
    return numero ** 2


def calculo_cubo(numero: float) -> float:
    """
    Calcula o cubo de um número.
    
    Args:
        numero (float): O número a ser elevado ao cubo
        
    Returns:
        float: O cubo do número
    """
    return numero ** 3


def operacoes_aritmeticas(a: float, b: float) -> dict:
    """
    Realiza operações aritméticas básicas.
    
    Args:
        a (float): Primeiro número
        b (float): Segundo número
        
    Returns:
        dict: Dicionário com resultados de soma, subtração, multiplicação e divisão
    """
    return {
        'soma': a + b,
        'subtracao': a - b,
        'multiplicacao': a * b,
        'divisao': a / b if b != 0 else None,
        'modulo': a % b if b != 0 else None
    }


def raiz(numero: float, indice: int = 2) -> float:
    """
    Calcula a raiz de um número.
    
    Args:
        numero (float): O número
        indice (int): Índice da raiz (2 para quadrada, 3 para cúbica, etc)
        
    Returns:
        float: A raiz do número
    """
    if numero < 0 and indice % 2 == 0:
        return None
    return numero ** (1 / indice)


def inverso_numero(numero: int) -> int:
    """
    Inverte os dígitos de um número.
    
    Args:
        numero (int): O número a ser invertido
        
    Returns:
        int: O número invertido
    """
    return int(str(numero)[::-1])


def decomposicao_tempo(minutos_totais: int) -> dict:
    """
    Decomposição de minutos em horas e minutos.
    
    Args:
        minutos_totais (int): Total de minutos
        
    Returns:
        dict: Dicionário com horas e minutos
    """
    horas: int = minutos_totais // 60
    minutos: int = minutos_totais % 60
    return {'horas': horas, 'minutos': minutos}


def percentual(parte: float, total: float) -> float:
    """
    Calcula percentual de uma parte em relação ao total.
    
    Args:
        parte (float): A parte
        total (float): O total
        
    Returns:
        float: O percentual
    """
    if total == 0:
        return 0
    return (parte / total) * 100


def exemplo_interativo() -> None:
    """Exemplo de programa interativo com menu."""
    print("\n" + "="*50)
    print("EXEMPLOS DE REFERÊNCIA")
    print("="*50)
    
    while True:
        print("\n[1] Dobro de um número")
        print("[2] Quadrado de um número")
        print("[3] Cubo de um número")
        print("[4] Operações aritméticas")
        print("[5] Raiz de um número")
        print("[6] Inverso de um número")
        print("[7] Decomposição de tempo")
        print("[8] Cálculo de percentual")
        print("[0] Sair")
        
        opcao: str = input("\nEscolha uma opção: ").strip()
        
        if opcao == '0':
            print("Até logo!")
            break
        
        try:
            if opcao == '1':
                num: float = float(input("Digite um número: "))
                resultado: float = calculo_dobro(num)
                print(f"O dobro de {num} é {resultado}")
            
            elif opcao == '2':
                num: float = float(input("Digite um número: "))
                resultado: float = calculo_quadrado(num)
                print(f"O quadrado de {num} é {resultado:.2f}")
            
            elif opcao == '3':
                num: float = float(input("Digite um número: "))
                resultado: float = calculo_cubo(num)
                print(f"O cubo de {num} é {resultado:.2f}")
            
            elif opcao == '4':
                a: float = float(input("Digite o primeiro número: "))
                b: float = float(input("Digite o segundo número: "))
                resultados: dict = operacoes_aritmeticas(a, b)
                print(f"\nResultados:")
                for op, valor in resultados.items():
                    print(f"  {op}: {valor}")
            
            elif opcao == '5':
                num: float = float(input("Digite um número: "))
                indice: int = int(input("Digite o índice da raiz (padrão 2): ") or "2")
                resultado: float = raiz(num, indice)
                print(f"A raiz {indice} de {num} é {resultado:.4f}")
            
            elif opcao == '6':
                num: int = int(input("Digite um número: "))
                resultado: int = inverso_numero(num)
                print(f"O inverso de {num} é {resultado}")
            
            elif opcao == '7':
                minutos: int = int(input("Digite o total de minutos: "))
                resultado: dict = decomposicao_tempo(minutos)
                print(f"{minutos} minutos = {resultado['horas']}h {resultado['minutos']}min")
            
            elif opcao == '8':
                parte: float = float(input("Digite a parte: "))
                total: float = float(input("Digite o total: "))
                resultado: float = percentual(parte, total)
                print(f"{parte} é {resultado:.2f}% de {total}")
            
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Erro: Digite valores válidos!")
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    exemplo_interativo()
