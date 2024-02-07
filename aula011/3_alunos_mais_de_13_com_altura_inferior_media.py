# Faça um programa que armazene as idades e as alturas de 4 alunos. Seu programa deve exibir quantos alunos com mais de 13 anos possuem uma altura inferior à altura média dentre todos os alunos.

# lista_idade = []
# lista_altura = []
# soma = 0

# for i in range(4):
#     altura = float(input('Digite a altura do aluno: '))
#     altura_media = 4/altura
#     # idade = int(input('Digite a idade do aluno: '))
#     # if idade > 13:
#     #     lista_idade.append(idade)
 
# print(f'A quantidade de alunos com mais de 13 anos é: {len(lista_idade)}')


# lista = []

# for i in range(4):
#     altura = int(input('Digite a altura do aluno: '))
# lista += altura
# print(lista)

# soma = 0
# for elemento in lista:
#     soma += elemento

# media = soma / len(lista)
# print("A média dos elementos da lista é:", media)


# for i in range(4):
#     altura = float(input('Digite a altura do aluno: '))
#     altura.append(lista)



# Armazenando as idades e alturas dos 4 alunos
idades = []
alturas = []

for i in range(4):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura (em metros) do {i+1}º aluno: "))
    idades.append(idade)
    alturas.append(altura)

# Calculando a altura média de todos os alunos
altura_media = sum(alturas) / len(alturas)

# Contando quantos alunos com mais de 13 anos têm uma altura inferior à média
alunos_mais_de_13_com_altura_inferior_media = 0

for i in range(4):
    if idades[i] > 13 and alturas[i] < altura_media:
        alunos_mais_de_13_com_altura_inferior_media += 1

# Exibindo o resultado
print(f"Alunos com mais de 13 anos e altura inferior à média: {alunos_mais_de_13_com_altura_inferior_media}")
