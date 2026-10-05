# Programa para calcular a soma dos números de 1 a 100

def soma_com_loop(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1):
        soma += numero
    return soma

def soma_com_formula(inicio, fim):
    n = fim - inicio + 1
    return n * (inicio + fim) // 2 

if __name__ == "__main__":
    inicio = 1
    fim = 100

    # Cálculo com loop
    soma_loop = soma_com_loop(inicio, fim)
    print(f"Soma de {inicio} a {fim} (loop): {soma_loop}")

    # Cálculo com fórmula
    soma_formula = soma_com_formula(inicio, fim)
    print(f"Soma de {inicio} a {fim} (fórmula): {soma_formula}")