
numeros = list(range(1, 11))
for n in numeros:
    print(n)

    print()

    contador = 1
    print()
    print()
for numero in range(2, 21, 2):
    print(numero)
    print()
    print()
   # Programa para imprimir a tabuada do 5 de 1 a 10

def tabuada(numero: int, inicio: int = 1, fim: int = 10):
    """
    Imprime a tabuada de 'numero' do intervalo [inicio, fim].
    """
 
    if not isinstance(numero, int) or not isinstance(inicio, int) or not isinstance(fim, int):
        raise ValueError("Todos os parâmetros devem ser inteiros.")
    if inicio > fim:
        raise ValueError("O valor inicial deve ser menor ou igual ao final.")

    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    try:
        tabuada(5)  
    except Exception as e:
        print(f"Erro: {e}")
        
        print()
        print()

while contador <= 10:
    print(f"Contador: {contador}")
    contador += 1

print()