# Dada uma lista de números, escreva um programa Python para criar uma 
# lista de tuplas tendo o primeiro elemento como o número e o segundo 
# elemento como o cubo do número.

lista = [1, 2, 3]
tulpa_vazia = [lista]

for i in lista:
    tulpa_vazia += (i, i**3)
print(tulpa_vazia)

