# 🎓 UFR SI 2026.1 - Repositório de Estudos Python

**Autor:** Nabor N. Silva  
**Período:** Março/2026 - Julho/2026  
**Disciplina:** Introdução à Programação (Estruturas de Dados e Lógica)

---

## 📚 Sobre este Repositório

Este repositório contém todos os exercícios, listas e estudos de programação Python desenvolvidos durante o **primeiro semestre de 2026** no curso de **Sistemas de Informação da UFR**.

Inclui:

- ✅ **3 Listas de Exercícios** com ~50+ exercícios resolvidos
- ✅ **26 Programas de Estudo Temático** (Fibonacci, números perfeitos, etc.)
- ✅ **Exemplos Práticos** de estruturas sequenciais, condicionais e loops
- ✅ **Type Hints** e documentação completa
- ✅ **Testes Unitários** para validação

---

## 📁 Estrutura do Projeto

```
ufr_si_2026_1/
├── README.md                              # Este arquivo
├── .gitignore                             # Configuração Git
├── tests.py                               # Testes unitários
│
├── Lista 1 Estruturas sequenciais.py      # Exercícios 1-9
├── Lista 2 Estruturas de Seleção Decisão Condicionais.py  # Exercícios 1-15
├── Lista 4 - Desisoes multiplas.py        # Exercícios 1-12
│
├── modeloTeste.py                         # Exemplos de referência
├── 01-06.py                               # Programa simples
├── areaDeTestes.py                        # Área de testes
│
└── Estudos Codigos PY/                    # 26 programas temáticos
    ├── sequencia_fibonacci.py             # Série Fibonacci
    ├── numero_perfeito.py                 # Números perfeitos
    ├── somatorio_1_n.py                   # Somatório 1..n
    ├── fatorial_7.py                      # Cálculo de fatorial
    └── ... (20+ mais)
```

---

## 🚀 Como Usar

### **Requisitos**

- Python 3.8+
- Sem dependências externas (usa apenas bibliotecas padrão)

### **Executar um Exercício**

```bash
# Lista 1 - Estruturas Sequenciais
python "Lista 1 Estruturas sequenciais.py"

# Lista 2 - Estruturas de Decisão
python "Lista 2 Estruturas de Seleção Decisão Condicionais.py"

# Lista 4 - Decisões Múltiplas
python "Lista 4 - Desisoes multiplas.py"

# Exercício de Estudo (ex: Fibonacci)
python "Estudos Codigos PY/sequencia_fibonacci.py"
```

### **Executar Testes**

```bash
python tests.py
```

---

## 📖 Conteúdo das Listas

### **Lista 1: Estruturas Sequenciais**

Exercícios sobre operações aritméticas, variáveis e tipos de dados:

- Leitura de tipos inteiro, real e texto
- Troca de variáveis
- Cálculo de antecessor e sucessor
- Decomposição de números
- Progressões aritméticas

### **Lista 2: Estruturas de Decisão/Condicionais**

Exercícios com operadores lógicos e estruturas if/elif/else:

- Comparações numéricas
- Menu de operações matemáticas
- Classificação por faixa de valores (idade, temperatura, IMC)
- Cálculo de descontos progressivos
- Simulações (sorteio, par/ímpar)

### **Lista 4: Decisões Múltiplas**

Exercícios com múltiplas condições e loops:

- Classificação de triângulos
- Cálculo de IMC com categorias
- Magic 8-Ball (simulação aleatória)
- Sistema de casas Hogwarts
- Tradução de dias da semana
- Cálculo de peso em outros planetas
- Equações de segundo grau

---

## 🧪 Exemplos de Uso

### **Exemplo 1: Estrutura Sequencial**

```python
# Lista 1, Exercício 1
# Entrada: número inteiro e real
# Saída: soma dos números
varInteiro = int(input("Digite um número inteiro: "))
varReal = float(input("Digite um número real: "))
resultado = varInteiro + varReal
print(f"Resultado: {resultado}")
```

### **Exemplo 2: Estrutura Condicional**

```python
# Lista 2, Exercício 3
# Classificar pessoa por faixa etária
idade = int(input("Digite a idade: "))
if idade < 12:
    print("É uma criança.")
elif idade <= 18:
    print("É um adolescente.")
else:
    print("É um adulto.")
```

### **Exemplo 3: Loop com Iteração**

```python
# Estudos: somatorio_1_n.py
# Somatório de 1/1 + 1/2 + 1/3 + ... + 1/50
soma = 0
for cont in range(1, 51):
    soma += 1/cont
    print(f'{soma:.2f}')
```

---

## 📚 Estudos Temáticos (Pasta: `Estudos Codigos PY/`)

| Arquivo                  | Descrição                           |
| ------------------------ | ----------------------------------- |
| `sequencia_fibonacci.py` | Série de Fibonacci                  |
| `numero_perfeito.py`     | Identificação de números perfeitos  |
| `somatorio_1_n.py`       | Somatório harmônico                 |
| `fatorial_7.py`          | Cálculo de fatorial                 |
| `progressao_numerica.py` | Progressões (aritmética/geométrica) |
| `flag_primo.py`          | Identificação de números primos     |
| `soma_multiplos_5.py`    | Soma de múltiplos de 5              |
| ...                      | (19+ mais programas)                |

---

## ✨ Características do Código

✅ **Type Hints** - Todos os arquivos possuem anotações de tipo  
✅ **Docstrings** - Documentação em todas as funções  
✅ **Validação** - Entrada de dados validada onde necessário  
✅ **Tratamento de Erros** - Try/except em operações críticas  
✅ **Comentários** - Código bem comentado e legível  
✅ **Testes** - Testes unitários disponíveis

---

## 🔍 Tecnologias

- **Linguagem:** Python 3.8+
- **Bibliotecas:** `random`, `math` (padrão)
- **Estilo:** PEP 8

---

## 📝 Notas Importantes

1. Todos os arquivos usam apenas **bibliotecas padrão do Python**
2. Os exercícios progridem de **básico → intermediário** em dificuldade
3. Cada arquivo é **independente** e pode ser executado isoladamente
4. Respostas estão **comentadas** para fins de aprendizado

---

## 📞 Autor

**Nabor N. Silva**  
Estudante de Sistemas de Informação - UFR  
Email: nabor.n@aluno.ufr.edu.br

---

## 📄 Licença

Este projeto é de uso educacional. Sinta-se livre para estudar, modificar e compartilhar.

**Última atualização:** Junho/2026
