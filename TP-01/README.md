# Implementação do Algoritmo de Karatsuba em Python

Implementação do algoritmo de Karatsuba para multiplicação de números inteiros.

---

## 🧐 O que é?

O algoritmo de Karatsuba é uma técnica eficiente para multiplicação de números inteiros grandes, introduzida por Anatolii Karatsuba em 1960. Ele melhora a complexidade da multiplicação em comparação ao método tradicional de multiplicação direta.

### Como o algoritmo funciona

O algoritmo funciona dividindo cada número em duas partes e usando apenas três multiplicações recursivas:

1. **Divisão**: Divide cada número em duas metades (a, b) e (c, d)
2. **Multiplicações recursivas**: Calcula ac, bd e (a+b)(c+d)
3. **Combinação**: Usa a fórmula: `ac × 10^n + ((a+b)(c+d) - ac - bd) × 10^(n/2) + bd`

**Análise linha por linha da função `karatsuba(x, y)`:**
- **Linha 16**: Caso base - se os números são pequenos (< 10), usa multiplicação direta
- **Linha 18**: Calcula o número de dígitos do maior número
- **Linha 20**: Verifica se n é ímpar e ajusta para par se necessário
- **Linha 22**: Calcula metade do número de dígitos
- **Linhas 24-27**: Divide os números em duas partes usando divisão inteira e módulo
- **Linhas 29-30**: Calcula recursivamente ac e bd
- **Linha 32**: Calcula (a+b)(c+d) - ac - bd = ad + bc
- **Linha 34**: Combina os resultados usando a fórmula de Karatsuba
- **Linha 36**: Retorna o resultado final

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior

### Execução
1. **Clone ou baixe o repositório**
2. **Navegue até o diretório do projeto**
   ```bash
   cd FPAA/TP-01
   ```
3. **Execute o programa**
   ```bash
   python main.py
   ou
   python3 main.py
   ```

### Exemplo de Execução
```
=== Algoritmo de Karatsuba ===

Teste: 1234 × 8765
Karatsuba: 10816010
--------------------------------------------------
Teste: 9999 × 8888
Karatsuba: 88871112
--------------------------------------------------
```

---

## 📊 Relatório Técnico

### Análise da Complexidade Ciclomática

#### Representação do Fluxo de Controle

A função `karatsuba(x, y)` possui o seguinte fluxo de controle:

```
Nó 1: Início da função
  ↓
Nó 2: Verificação do caso base (x < 10 or y < 10)
  ↓ (True)
Nó 3: Retorna x * y
  ↓ (False)
Nó 4: Calcula n = max(len(str(x)), len(str(y)))
  ↓
Nó 5: Verificação condicional (n % 2 != 0)
  ↓ (True)
Nó 6: n += 1
  ↓ (False)
Nó 7: Calcula half = n // 2
  ↓
Nó 8: Divide números em a, b, c, d
  ↓
Nó 9: Chama karatsuba(a, c)
  ↓
Nó 10: Chama karatsuba(b, d)
  ↓
Nó 11: Chama karatsuba(a + b, c + d)
  ↓
Nó 12: Calcula resultado final
  ↓
Nó 13: Retorna resultado
```

**📊 Diagrama de Fluxo Visual (adicionar aqui)**: 

#### Estrutura do Grafo de Fluxo

- **Nós (N)**: 13
- **Arestas (E)**: 16
- **Componentes conectados (P)**: 1

#### Cálculo da Complexidade Ciclomática

Usando a fórmula: **M = E - N + 2P**`

- M = 16 - 13 + 2(1)
- M = 16 - 13 + 2
- M = 5

**Complexidade Ciclomática = 5**

**Interpretação**: A função tem complexidade ciclomática baixa (5), indicando boa estrutura e facilidade de manutenção. Valores entre 1-10 são considerados aceitáveis.

**Detalhamento das arestas:**
- Nó 1 → Nó 2: fluxo principal
- Nó 2 → Nó 3: caso base (True)
- Nó 2 → Nó 4: caso recursivo (False)
- Nó 4 → Nó 5: fluxo principal
- Nó 5 → Nó 6: n é ímpar (True)
- Nó 5 → Nó 7: n é par (False)
- Nó 6 → Nó 7: fluxo após ajuste
- Nó 7 → Nó 8: fluxo principal
- Nó 8 → Nó 9: fluxo principal
- Nó 9 → Nó 10: fluxo principal
- Nó 10 → Nó 11: fluxo principal
- Nó 11 → Nó 12: fluxo principal
- Nó 12 → Nó 13: fluxo principal
- Nó 13 → Fim: retorno da função

---

### Análise da Complexidade Assintótica

#### Complexidade Temporal

**Fórmula de Recorrência:**
T(n) = 3T(n/2) + O(n)

**Resolução:**
- **Caso base**: T(1) = O(1)
- **Caso recursivo**: T(n) = 3T(n/2) + O(n)
- **Solução**: T(n) = O(n^log₂(3)) ≈ O(n^1.585)

**Análise dos Casos:**

1. **Melhor Caso**: O(1)
   - Quando x < 10 ou y < 10
   - Multiplicação direta em tempo constante

2. **Caso Médio**: O(n^1.585)
   - Quando os números têm tamanhos similares
   - Algoritmo divide e conquista de forma equilibrada

3. **Pior Caso**: O(n^1.585)
   - Quando os números têm muitos dígitos
   - Recursão máxima até atingir o caso base

#### Complexidade Espacial

**Pilha de Recursão:**
- **Profundidade máxima**: O(log n)
- **Espaço por nível**: O(n)
- **Total**: O(n log n)

**Variáveis auxiliares:**
- **Constante**: O(1) por chamada
- **Total**: O(n log n)

**Complexidade Espacial Total: O(n log n)**

---

## 🔍 Comparação com Algoritmos Tradicionais

| Algoritmo | Complexidade Temporal | Complexidade Espacial |
|-----------|----------------------|----------------------|
| Multiplicação Escolar | O(n²) | O(n²) |
| **Karatsuba** | **O(n^1.585)** | **O(n log n)** |
| Toom-Cook | O(n^1.465) | O(n) |
| Schönhage-Strassen | O(n log n log log n) | O(n) |

**Vantagens do Karatsuba:**
- Melhora significativa sobre multiplicação escolar
- Implementação relativamente simples
- Eficiente para números de tamanho médio

**Desvantagens:**
- Overhead para números pequenos
- Não é o mais eficiente para números muito grandes

---

## 📁 Estrutura do Projeto

```
FPAA/TP-01/
├── main.py          # Implementação do algoritmo
├── README.md        # Documentação completa
└── readme-example.md # Exemplo de referência
```

---

## 🧪 Testes e Validação

O programa inclui testes automáticos que validam:
- Números pequenos (caso base)
- Números de tamanho médio
- Números grandes
- Comparação com multiplicação padrão do Python

Todos os testes passam, confirmando a correção da implementação.

---

## 📚 Referências

- Karatsuba, A. A. (1962). "The complexity of computations". Proceedings of the Steklov Institute of Mathematics.
- Cormen, T. H., et al. (2009). "Introduction to Algorithms". MIT Press.
- Documentação Python: https://docs.python.org/
- Complexidade Ciclómatica: https://learn.microsoft.com/pt-br/visualstudio/code-quality/code-metrics-cyclomatic-complexity?view=vs-2022$0

