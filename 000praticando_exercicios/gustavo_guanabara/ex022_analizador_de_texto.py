nome = str(input('digite um nome: '))
contador = 0

print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(len(nome.replace(' ', '')))

nome_separado = (nome.split())
nome_separado = nome_separado[0]

for i in nome_separado:
    contador+=1

print(f'{contador}')

