"""
TESTES UNITÁRIOS - LISTA DE EXERCÍCIOS PYTHON
Testa funções principais das listas de exercícios.

Autor: Nabor N. Silva
Data: 2026-06-09
"""

import unittest
import io
import sys
from contextlib import redirect_stdout


class TestEstruturasSequenciais(unittest.TestCase):
    """Testes para Lista 1 - Estruturas Sequenciais."""
    
    def test_calculo_antecessor_sucessor(self) -> None:
        """Testa cálculo de antecessor e sucessor."""
        numero: int = 10
        antecessor: int = numero - 1
        sucessor: int = numero + 1
        
        self.assertEqual(antecessor, 9)
        self.assertEqual(sucessor, 11)
    
    def test_decomposicao_numero_real(self) -> None:
        """Testa decomposição de número real."""
        numero: float = 25.75
        parte_inteira: int = int(numero)
        parte_fracionaria: float = numero - parte_inteira
        
        self.assertEqual(parte_inteira, 25)
        self.assertAlmostEqual(parte_fracionaria, 0.75, places=2)
    
    def test_progressao_aritmetica(self) -> None:
        """Testa cálculo de PA."""
        primeiro_termo: float = 2.0
        razao: float = 3.0
        posicao: int = 5
        
        valor_termo: float = primeiro_termo + (posicao - 1) * razao
        self.assertEqual(valor_termo, 14.0)
    
    def test_divisao_com_detalhes(self) -> None:
        """Testa divisão com quociente e resto."""
        dividendo: int = 17
        divisor: int = 5
        
        quociente: int = dividendo // divisor
        resto: int = dividendo % divisor
        
        self.assertEqual(quociente, 3)
        self.assertEqual(resto, 2)
    
    def test_decomposicao_quatro_digitos(self) -> None:
        """Testa decomposição de número de 4 dígitos."""
        numero: int = 5678
        
        milhares: int = numero // 1000
        centenas: int = (numero // 100) % 10
        dezenas: int = (numero // 10) % 10
        unidades: int = numero % 10
        
        self.assertEqual(milhares, 5)
        self.assertEqual(centenas, 6)
        self.assertEqual(dezenas, 7)
        self.assertEqual(unidades, 8)


class TestEstruturasCondicionals(unittest.TestCase):
    """Testes para Lista 2 - Estruturas de Decisão."""
    
    def test_comparacao_numeros(self) -> None:
        """Testa comparação de números."""
        a: int = 10
        b: int = 5
        
        if a > b:
            resultado = "maior"
        else:
            resultado = "menor ou igual"
        
        self.assertEqual(resultado, "maior")
    
    def test_classificacao_temperatura(self) -> None:
        """Testa classificação de temperatura."""
        temperatura: float = 25.0
        
        if temperatura < 15:
            classificacao = "Frio"
        elif temperatura <= 30:
            classificacao = "Moderado"
        else:
            classificacao = "Quente"
        
        self.assertEqual(classificacao, "Moderado")
    
    def test_media_aluno(self) -> None:
        """Testa cálculo de média de aluno."""
        nota1: float = 7.0
        nota2: float = 8.0
        nota3: float = 9.0
        
        media: float = (nota1 + nota2 + nota3) / 3
        
        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"
        
        self.assertEqual(status, "Aprovado")
        self.assertAlmostEqual(media, 8.0, places=2)
    
    def test_imc_calculo(self) -> None:
        """Testa cálculo de IMC."""
        peso: float = 70.0
        altura: float = 1.75
        
        imc: float = peso / (altura ** 2)
        
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif imc <= 24.9:
            categoria = "Peso normal"
        else:
            categoria = "Acima do peso"
        
        self.assertGreater(imc, 20)
        self.assertLess(imc, 30)
        self.assertEqual(categoria, "Peso normal")
    
    def test_desconto_progressivo(self) -> None:
        """Testa desconto progressivo por valor."""
        valor: float = 250.0
        
        if valor < 100:
            desconto_pct = 5
        elif valor <= 500:
            desconto_pct = 10
        else:
            desconto_pct = 15
        
        desconto: float = valor * (desconto_pct / 100)
        valor_final: float = valor - desconto
        
        self.assertEqual(desconto_pct, 10)
        self.assertEqual(desconto, 25.0)
        self.assertEqual(valor_final, 225.0)


class TestDecisoesMúltiplas(unittest.TestCase):
    """Testes para Lista 4 - Decisões Múltiplas."""
    
    def test_classificacao_triangulo_equilatero(self) -> None:
        """Testa classificação de triângulo equilátero."""
        lado_a: float = 5.0
        lado_b: float = 5.0
        lado_c: float = 5.0
        
        eh_valido = (lado_a + lado_b > lado_c and 
                     lado_a + lado_c > lado_b and 
                     lado_b + lado_c > lado_a)
        
        self.assertTrue(eh_valido)
        
        if lado_a == lado_b == lado_c:
            tipo = "Equilátero"
        
        self.assertEqual(tipo, "Equilátero")
    
    def test_classificacao_triangulo_isosceles(self) -> None:
        """Testa classificação de triângulo isósceles."""
        lado_a: float = 5.0
        lado_b: float = 5.0
        lado_c: float = 8.0
        
        eh_valido = (lado_a + lado_b > lado_c and 
                     lado_a + lado_c > lado_b and 
                     lado_b + lado_c > lado_a)
        
        self.assertTrue(eh_valido)
        
        if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            tipo = "Isósceles"
        
        self.assertEqual(tipo, "Isósceles")
    
    def test_media_ponderada(self) -> None:
        """Testa cálculo de média ponderada."""
        nota1: float = 8.0
        nota2: float = 7.0
        nota3: float = 9.0
        media_ex: float = 8.5
        
        media_final: float = (nota1 + nota2*2 + nota3*3 + media_ex) / 7
        
        self.assertGreater(media_final, 6.0)
        self.assertLess(media_final, 10.0)
        self.assertAlmostEqual(media_final, 8.21, places=1)
    
    def test_maior_menor_valores(self) -> None:
        """Testa encontrar maior e menor valor."""
        valores: list = [15, 3, 42, 8]
        
        maior: int = max(valores)
        menor: int = min(valores)
        
        self.assertEqual(maior, 42)
        self.assertEqual(menor, 3)


class TestFuncoesUtilitárias(unittest.TestCase):
    """Testes para funções auxiliares."""
    
    def test_conversao_tipos(self) -> None:
        """Testa conversões de tipo."""
        numero_str: str = "42"
        numero_int: int = int(numero_str)
        numero_float: float = float(numero_str)
        
        self.assertEqual(numero_int, 42)
        self.assertEqual(numero_float, 42.0)
        self.assertEqual(type(numero_int).__name__, 'int')
        self.assertEqual(type(numero_float).__name__, 'float')
    
    def test_operadores_logicos(self) -> None:
        """Testa operadores lógicos."""
        a: bool = True
        b: bool = False
        
        self.assertTrue(a and True)
        self.assertFalse(a and b)
        self.assertTrue(a or b)
        self.assertFalse(b or False)
        self.assertTrue(not b)
    
    def test_validacao_intervalo(self) -> None:
        """Testa validação de intervalo."""
        valor: int = 15
        
        eh_valido: bool = 10 <= valor <= 20
        self.assertTrue(eh_valido)
        
        valor = 25
        eh_valido = 10 <= valor <= 20
        self.assertFalse(eh_valido)


def suite() -> unittest.TestSuite:
    """Cria suite de testes."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestEstruturasSequenciais))
    suite.addTests(loader.loadTestsFromTestCase(TestEstruturasCondicionals))
    suite.addTests(loader.loadTestsFromTestCase(TestDecisoesMúltiplas))
    suite.addTests(loader.loadTestsFromTestCase(TestFuncoesUtilitárias))
    
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    
    print("\n" + "="*60)
    print(f"Testes executados: {result.testsRun}")
    print(f"Sucessos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Falhas: {len(result.failures)}")
    print(f"Erros: {len(result.errors)}")
    print("="*60)
    
    exit(0 if result.wasSuccessful() else 1)
