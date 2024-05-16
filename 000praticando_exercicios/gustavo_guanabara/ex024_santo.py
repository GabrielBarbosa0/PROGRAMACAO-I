nome = str(input('escreva o nome da sua cidade: ')).lower()

nome = (nome.split())
print(nome)

if 'santos' in nome[0]:
    print('a sua cidade começa com santo')
else:
    print('a sua cidade não começa com santo')

