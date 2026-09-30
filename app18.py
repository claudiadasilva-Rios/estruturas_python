

def somar_numeros():
    soma = 0

    while True:
        try:
            numero = float(input("Digite um número (0 para sair): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue 
        if numero == 0:
            break  

        soma += numero 

    print(f"A soma dos números digitados é: {soma}")

if __name__ == "__main__":
    somar_numeros()