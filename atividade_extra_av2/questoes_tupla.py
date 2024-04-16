# Gabriel Gomes Barbosa

# Questões de Tupla:

# Questão 1
'''
tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)
tupla_nova = ()

for elemento in tupla:
    if elemento not in tupla_nova:
        tupla_nova += (elemento,)

print(f'A tupla sem os valores duplicados: {tupla_nova}.')
'''

#Questão 2
'''
lista = [1, 5, 3, 9]
tupla_cubos = []
for num in lista:
    tupla_cubos += [(num, num ** 3)]

print(f'Lista de tuplas com números e seus cubos: {tupla_cubos}')
'''

# Questão 3
'''
texto = "A casa é bonita, a casa é azul"
palavras = texto.split()

contagem_ocorrencias = {}
for palavra in palavras:
    contagem_ocorrencias[palavra] = contagem_ocorrencias.get(palavra, 0) + 1

resultado = tuple((palavra, contagem) for palavra, contagem in contagem_ocorrencias.items())

print("Ocorrências de cada palavra:")
print(resultado)
'''

# Questão 4
'''
registro_alunos = []

registro_alunos.append(("Lucas",18,[9,5,6]))
registro_alunos.append(("Cleber",23,[7,8,2]))
registro_alunos.append(("Caio",4,[3,4,2]))

busca = input('Digite o nome do aluno: ')
aluno_encontrado = None
for aluno in registro_alunos:
    if aluno[0] == busca:
        aluno_encontrado = aluno
        break
    
if aluno_encontrado:
    print(f'OS dados do aluno {busca}:')
    print('Nome: ', aluno_encontrado[0])
    print('Idade: ', aluno_encontrado[1])
    print('Notas: ', aluno_encontrado[2])
else: print('Aluno não encontrado :(')
'''
