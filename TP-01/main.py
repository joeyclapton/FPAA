def karatsuba(x, y):
    """
    Implementação do algoritmo de Karatsuba para multiplicação de números inteiros.
    
    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro
    
    Returns:
        int: Produto de x * y
    """

    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    
    if n % 2 != 0:
        n += 1
    
    half = n // 2
    
    a = x // (10 ** half)
    b = x % (10 ** half)
    c = y // (10 ** half)
    d = y % (10 ** half)
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    
    result = ac * (10 ** n) + ad_plus_bc * (10 ** half) + bd
    
    return result


def main():
    print("=== Algoritmo de Karatsuba ===")
    print()
    
    test_cases = [
        (1234, 5678),
        (9999, 8888),
        (12345, 67890),
        (99999, 88888),
        (123456, 789012)
    ]
    
    for x, y in test_cases:
        karatsuba_result = karatsuba(x, y)
        
        standard_result = x * y
        
        print(f"Teste: {x} × {y}")
        print(f"Karatsuba: {karatsuba_result}")
        print(f"Padrão:    {standard_result}")
        print(f"Correto:   {karatsuba_result == standard_result}")
        print("-" * 50)
    
    print("\n=== Digite dois números para multiplicar ===")
    try:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        
        result = karatsuba(x, y)
        print(f"\nResultado usando Karatsuba: {x} × {y} = {result}")
        print(f"Verificação: {x * y}")
        
    except ValueError:
        print("Entrada inválida. Encerrando programa.")


if __name__ == "__main__":
    main()

