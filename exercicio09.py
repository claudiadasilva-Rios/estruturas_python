# Programa para imprimir o tamanho do quadrado
linhas = 6
colunas = 6

for i in range(linhas):          # Loop para as linhas
    for j in range(colunas):     # Loop para as colunas
        print("*", end="")       # Imprime sem quebrar a linha
    print()                      # Quebra a linha ao final de cada linha