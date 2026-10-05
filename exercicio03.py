# Programa para gerar a tabuada de um número de 1 a 10

def gerar_tabuada(numero):
    """Gera e imprime a tabuada de 1 a 10 para o número fornecido."""
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        # Solicita o número ao usuário
        entrada = input("Digite um número inteiro: ").strip()
        
        # Valida se é inteiro
        if not entrada.lstrip('-').isdigit():
            print("Erro: Você deve digitar um número inteiro válido.")
            return
        
        numero = int(entrada)
        
        # Gera e exibe a tabuada
        gerar_tabuada(numero)
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()

'''
Exercício 3
Tabuada: Peça um número ao usuário e mostre sua tabuada de 1 a 10. 
'''

numero = int(input("Digite um número: "))

# Debug
# print(numero, type(numero))

for num in range(1, 11):
    print(f'{numero} x {num} = {numero * num}')