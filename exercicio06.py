#Programa para solicitar a senha para o usuário

def solicitar_senha():
    senha_correta = "2855"  # Defina a senha correta
    while True:
        senha = input("Digite a senha: ").strip()  # Remove espaços extras
        if senha == senha_correta:
            print("✅ Senha correta! Acesso concedido.")
            break
        else:
            print("❌ Senha incorreta. Tente novamente.")

if __name__ == "__main__":
    try:
        solicitar_senha()
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")