# nome completo, n nomes, 3 ... 4 , inicial de cada nome em maiusculo

nome = str(input('Digite seu nome: '))
partes = nome.split(' ')
iniciais = ''
# print(partes)

for i in partes:
    iniciais += i[0]

iniciais = iniciais.upper()

print(iniciais)