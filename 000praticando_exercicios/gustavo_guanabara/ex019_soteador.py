import random

aluno1 = str(input('digite o nome do aluno 1: '))
aluno2 = str(input('digite o nome do aluno 2: '))
aluno3 = str(input('digite o nome do aluno 3: '))
aluno4 = str(input('digite o nome do aluno 4: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista_alunos)

print(f'o aluno {escolhido} foi o escolhido')

# num_aluno = random.randint(1, 4)
# print(num_aluno)

# if num_aluno == 1:
#     print(f'o aluno {aluno1} foi o sorteado')
# elif num_aluno == 2:
#     print(f'o aluno {aluno2} foi o sorteado')
# elif num_aluno == 3:
#     print(f'o aluno {aluno3} foi o sorteado')
# else:
#     print(f'o aluno {aluno4} foi o sorteado')