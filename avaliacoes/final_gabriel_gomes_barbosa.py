# Gabriel Gomes Barbosa


# 1 ///////////////////////////////////////////////////////
# num1 = float(input("Digite o primeiro numero: "))
# num2 = float(input("Digite o segundo numero: "))
# num3 = float(input("Digite o terceiro numero: "))

# if num1 <= num2 and num1 <= num3:
#     menor = num1
#     if num2 <= num3:
#         medio = num2
#         maior = num3
#     else:
#         medio = num3
#         maior = num2
# elif num2 <= num1 and num2 <= num3:
#     menor = num2
#     if num1 <= num3:
#         medio = num1
#         maior = num3
#     else:
#         medio = num3
#         maior = num1
# else:
#     menor = num3
#     if num1 <= num2:
#         medio = num1
#         maior = num2
#     else:
#         medio = num2
#         maior = num1

# print(menor, medio, maior)


# 2 ///////////////////////////////////////////////////////

# n = int(input("Digite o valor de N: "))

# num = 1
# count = 1
# while count <= n:
#     for i in range(1, count + 1):
#         print(num, end=" ")
#         num += 1
#     print()
#     count += 1


# # 3 ///////////////////////////////////////////////////////

# alunos = []

# for i in range(4):
#     idade = int(input(f"Digite a idade do aluno {i + 1}: "))
#     altura = float(input(f"Digite a altura do aluno {i + 1}: "))
#     alunos.append((idade, altura))

# soma_alturas = sum(altura for _, altura in alunos)
# media_alturas = soma_alturas / len(alunos)

# contador = 0
# for idade, altura in alunos:
#     if idade > 13 and altura < media_alturas:
#         contador += 1

# print(f"quantidade de alunos com mais de 13 anos e altura inferior a  media: {contador}")


# 4 ///////////////////////////////////////////////////////

# def fatorial_duplo(n):
#     if n <= 0 or n % 2 == 0:
#         return -1
    
#     resultado = 1
#     for i in range(n, 0, -2):
#         resultado *= i
#     return resultado

# numero = int(input("digite um numero inteiro positivo e impar: "))
# resultado = fatorial_duplo(numero)
# if resultado != -1:
#     print("fatorial duplo:", resultado)
# else:
#     print("numero nao e positivo ou nao e impar.")


# 5 ///////////////////////////////////////////////////////

# string1 = str(input('digite uma string: '))
# string2 = str(input('digite outra string: '))
# lista1 = ''
# lista2 = ''
# caracteres_presentes_duas_listas = ''
# caracteres_exclusivos_lista1 = ''
# caracteres_exclusivos_lista2 = ''
# remover_caracteres_repetidos = ''


# for i in(string1):
#     lista1+=i

# for i in(string2):
#     lista2+=i

# for i in(string1):
#     if i in string2:
#         caracteres_presentes_duas_listas += i

# for i in (string1):
#     if i not in string2:
#         caracteres_exclusivos_lista1 += i

# for i in (string2):
#     if i not in string1:
#         caracteres_exclusivos_lista2 += i

# caracteres_exclusivos_das_duas_listas = caracteres_exclusivos_lista1+caracteres_exclusivos_lista2


# for i in(caracteres_exclusivos_das_duas_listas):
#     if i not in remover_caracteres_repetidos:
#         remover_caracteres_repetidos+= i

# salvar_caracteres_presentes_duas_listas = caracteres_presentes_duas_listas

# tupla = (salvar_caracteres_presentes_duas_listas, remover_caracteres_repetidos)
# print(tupla)
