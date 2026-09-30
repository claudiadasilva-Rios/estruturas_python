# Programa para calcular a soma dos números de 1 a 100

def soma_com_loop(inicio, fim):
    """Calcula a soma usando um loop for."""
    soma = 0
    for numero in range(inicio, fim + 1):
        soma += numero
    return soma

def soma_com_formula(inicio, fim):
    """Calcula a soma usando a fórmula da soma de uma PA: n*(a1 + an)/2"""
    n = fim - inicio + 1
    return n * (inicio + fim) // 2  # // garante resultado inteiro

if __name__ == "__main__":
    inicio = 1
    fim = 100

    # Cálculo com loop
    soma_loop = soma_com_loop(inicio, fim)
    print(f"Soma de {inicio} a {fim} (loop): {soma_loop}")

    # Cálculo com fórmula
    soma_formula = soma_com_formula(inicio, fim)
    print(f"Soma de {inicio} a {fim} (fórmula): {soma_formula}")