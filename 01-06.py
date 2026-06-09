"""
PROGRAMA: Intervalo de Números
Descrição: Exibe todos os números de um intervalo (início até fim).

Autor: Nabor N. Silva
Data: 2026-06-09
Versão: 2.0
"""


def exibir_intervalo(inicio: int, fim: int) -> None:
    """
    Exibe todos os números de um intervalo.
    
    Args:
        inicio (int): Número inicial do intervalo
        fim (int): Número final do intervalo (inclusive)
    """
    print(f"\nNúmeros de {inicio} até {fim}:\n")
    for numero in range(inicio, fim + 1):
        print(numero, end=' ')
    print("\n")


def contar_intervalo(inicio: int, fim: int) -> int:
    """
    Conta quantos números há em um intervalo.
    
    Args:
        inicio (int): Número inicial
        fim (int): Número final
        
    Returns:
        int: Quantidade de números
    """
    return abs(fim - inicio) + 1


def soma_intervalo(inicio: int, fim: int) -> int:
    """
    Calcula a soma de todos os números em um intervalo.
    
    Args:
        inicio (int): Número inicial
        fim (int): Número final
        
    Returns:
        int: Soma dos números
    """
    return sum(range(inicio, fim + 1))


def media_intervalo(inicio: int, fim: int) -> float:
    """
    Calcula a média dos números em um intervalo.
    
    Args:
        inicio (int): Número inicial
        fim (int): Número final
        
    Returns:
        float: Média dos números
    """
    quantidade: int = contar_intervalo(inicio, fim)
    soma: int = soma_intervalo(inicio, fim)
    return soma / quantidade


def exibir_intervalo_com_analise(inicio: int, fim: int) -> None:
    """
    Exibe um intervalo com análise completa.
    
    Args:
        inicio (int): Número inicial
        fim (int): Número final
    """
    print("\n" + "="*50)
    print(f"ANÁLISE DO INTERVALO [{inicio}, {fim}]")
    print("="*50)
    
    exibir_intervalo(inicio, fim)
    
    quantidade: int = contar_intervalo(inicio, fim)
    soma: int = soma_intervalo(inicio, fim)
    media: float = media_intervalo(inicio, fim)
    
    print(f"Quantidade de números: {quantidade}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")
    print(f"Menor número: {min(inicio, fim)}")
    print(f"Maior número: {max(inicio, fim)}")
    print("="*50 + "\n")


def main() -> None:
    """Função principal."""
    try:
        print("\n" + "="*50)
        print("EXIBIDOR DE INTERVALO DE NÚMEROS")
        print("="*50)
        
        inicio: int = int(input("\nDigite o número inicial: "))
        fim: int = int(input("Digite o número final: "))
        
        if inicio > fim:
            print("\nAviso: Início é maior que o fim. Os números serão exibidos em ordem decrescente.")
            inicio, fim = fim, inicio
        
        exibir_intervalo_com_analise(inicio, fim)
        
    except ValueError:
        print("\nErro: Digite números inteiros válidos!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")


if __name__ == "__main__":
    main()
