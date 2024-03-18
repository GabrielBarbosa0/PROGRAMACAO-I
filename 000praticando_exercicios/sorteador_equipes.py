# import random

# # Receber nomes dos alunos
# alunos = input("Digite os nomes dos alunos separados por vírgula: ").split(",")

# # Receber quantidade de pessoas por grupo
# tamanho_grupo = int(input("Digite a quantidade de pessoas por grupo: "))

# # Receber quantidade de grupos
# quantidade_grupos = int(input("Digite a quantidade de grupos: "))

# # Embaralhar a lista de alunos
# random.shuffle(alunos)

# # Dividir os alunos em grupos
# grupos = []
# for i in range(quantidade_grupos):
#     grupo = alunos[i * tamanho_grupo: (i + 1) * tamanho_grupo]
#     grupos.append(grupo)

# # Exibir os grupos
# for i, grupo in enumerate(grupos, start=1):
#     print(f"Grupo {i}: {', '.join(grupo)}")


import random

alunos = input("Digite os nomes dos alunos separados por vírgula: ").split(",")

tamanho_grupo = int(input("Digite a quantidade de pessoas por grupo: "))

quantidade_alunos = len(alunos)
quantidade_grupos = quantidade_alunos // tamanho_grupo
alunos_restantes = quantidade_alunos % tamanho_grupo

random.shuffle(alunos)

grupos = []
inicio = 0
for i in range(quantidade_grupos):
    fim = inicio + tamanho_grupo
    grupo = alunos[inicio:fim]
    grupos.append(grupo)
    inicio = fim

if alunos_restantes > 0:
    for i in range(alunos_restantes):
        grupos[i].append(alunos[quantidade_grupos * tamanho_grupo + i])

for i, grupo in enumerate(grupos, start=1):
    print(f"Grupo {i}: {', '.join(grupo)}")
