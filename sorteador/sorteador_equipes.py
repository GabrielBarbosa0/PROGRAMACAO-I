import random

# Receber nomes dos alunos
alunos = input("Digite os nomes dos alunos separados por vírgula: ").split(",")

# Receber quantidade de pessoas por grupo
tamanho_grupo = int(input("Digite a quantidade de pessoas por grupo: "))

# Receber quantidade de grupos
quantidade_grupos = int(input("Digite a quantidade de grupos: "))

# Embaralhar a lista de alunos
random.shuffle(alunos)

# Dividir os alunos em grupos
grupos = []
for i in range(quantidade_grupos):
    grupo = alunos[i * tamanho_grupo: (i + 1) * tamanho_grupo]
    grupos.append(grupo)

# Exibir os grupos
for i, grupo in enumerate(grupos, start=1):
    print(f"Grupo {i}: {', '.join(grupo)}")
