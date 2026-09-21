#Recebe o nome do usuário na variavél
name = input("Qual seu nome? ")

#Receba a idade do usuário na variavél
age = input("Qual a sua idade? ")

#Exibe uma mensagem formatada
print()
print("Olá", name , "!")
print("Você tem", age , "anos")

#Usando string formatada (f) -Melhor prática
print()
print(f"Olá {name}! Você tem {age} anos.")