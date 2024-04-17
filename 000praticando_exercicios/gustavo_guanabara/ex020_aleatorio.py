import random

aluno1 = str(input('digite o nome do aluno 1: '))
aluno2 = str(input('digite o nome do aluno 2: '))
aluno3 = str(input('digite o nome do aluno 3: '))
aluno4 = str(input('digite o nome do aluno 4: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)
print('a ordem de apresentacao será: ')
print(lista_alunos)