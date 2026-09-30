# Menu simples em Python
def mostrar_menu():
    """Exibe o menu no terminal."""
    print("\n=== MENU ===")
    print("1 - Olá")
    print("2 - Python")
    print("3 - Sair")

def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção (1-3): ").strip())
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 3.")
            continue

        if opcao == 1:
            print("Olá!")
        elif opcao == 2:
            print("Python")
        elif opcao == 3:
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Escolha entre 1 e 3.")

if __name__ == "__main__":
    main()