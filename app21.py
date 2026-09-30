def mostrar_tabuada(numero: int):
    """Exibe a tabuada completa de 0 a 10 para o número informado."""
    print(f"\nTabuada do {numero}:")
    for i in range(0, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        # Solicita o número ao usuário
        entrada = input("Digite um número inteiro para ver a tabuada: ").strip()
        
        # Valida se é um número inteiro
        if not entrada.lstrip('-').isdigit():
            print("Erro: Você deve digitar um número inteiro válido.")
            return
        
        numero = int(entrada)
        
        # Exibe a tabuada
        mostrar_tabuada(numero)
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()