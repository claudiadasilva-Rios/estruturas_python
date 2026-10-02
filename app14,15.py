# Loop while

#while True:
   # print("looping") looping infinito


import os
os.system('cls')

while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")


    if x == '1':
        print('Vai comer')
        input('Tecle [Enter] para continuar.')
        

    if x == '2':
         print('Vai beber água')
         input('Tecle [Enter] para continuar.')
       
    if x == '3':
         print('Vá vê lá')
         input('Tecle [Enter] para continuar.')

         # Nenhuma das opções acima é válida
    

    if x == '0':
         print('Acabou')
         break

    else:
        print('\nNão entendi!')
        input('Tecle [Enter] para continuar.')        