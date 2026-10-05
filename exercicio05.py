# Programa para imprimir numeros, contagem regressiva de 10 a 1

def contagem_regressiva(inicio=10):
   
    if not isinstance(inicio, int) or inicio <= 0:
        raise ValueError("O valor inicial deve ser um inteiro positivo.")

    numero = inicio
    while numero >= 1:
        print(numero)
        numero -= 1  

if __name__ == "__main__":
    try:
        contagem_regressiva(10)
    except ValueError as e:
        print(f"Erro: {e}")