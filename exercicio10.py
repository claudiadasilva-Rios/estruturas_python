#Programa para imprimir as horas no formato de 12h

hora = 0

while hora < 12:  # Loop das horas
    minuto = 0
    while minuto < 60:  # Loop dos minutos
        print(f"{hora}:{minuto}")
        minuto += 1
    hora += 1
    print(f"{hora}:{minuto:02}")