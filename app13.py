# Iterando dicionário
import os
os.system('cls')

prods = {
    "cod": "123abc",
    "name": "Caixa de sapato vazia",
    "fabr": "Caixeiro Viajante",
    "preco": 120.99
}

print(prods)
print()

for prod in prods:
    # print(prods[prod])
    print(f' • {prod} - {prods[prod]}')

print()
print('------', prods.keys())# Pega a chaves dos dicionários
for prod in prods.keys():
 print(prod)

print()
print('------', prods.values())# Pega os valores dos dicionários
for prod in prods.values():
 print(prod)        

for prod_key, prod_value in prods.items():  # Pega a chave e os valores dos dicionários
    
 print(prod_key , prod_value)    
 print()
print(f' • {prod_key} - {prod_value}')