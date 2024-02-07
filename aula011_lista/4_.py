# Modifique o programa da questão 3 para que o usuário indique a quantidade de alunos que será utilizada no programa. Assim antes de começar a leitura de idades e alturas, o programa deve solicitar ao usuário o quantitativo de alunos

# Armazenando as idades e alturas dos 4 alunos
idades = []
alturas = []

quantidade_alunos = int(input('Digite a quantidade de alunos: '))

for i in range(quantidade_alunos):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura (em metros) do {i+1}º aluno: "))
    idades.append(idade)
    alturas.append(altura)

# Calculando a altura média de todos os alunos
altura_media = sum(alturas) / len(alturas)

# Contando quantos alunos com mais de 13 anos têm uma altura inferior à média
alunos_mais_de_13_com_altura_inferior_media = 0

for i in range(quantidade_alunos):
    if idades[i] > 13 and alturas[i] < altura_media:
        alunos_mais_de_13_com_altura_inferior_media += 1

# Exibindo o resultado
print(f"Quantidade de alunos: {quantidade_alunos}")
print(f"Quantidade de alunos: {quantidade_alunos}")

print(f"Alunos com mais de 13 anos e altura inferior à média: {alunos_mais_de_13_com_altura_inferior_media}")