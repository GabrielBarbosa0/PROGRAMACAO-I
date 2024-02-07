#Faça um programa que solicite uma string ao usuário e em seguida a imprima em formato de escada.

# # Solicita a string ao usuário
# entrada_usuario = input("Digite uma string: ")

# # Imprime a string em formato de escada
# for i in range(len(entrada_usuario)):
#     print(' ' * i + entrada_usuario[i])

entrada = input("Digite uma string: ")
escada = ''

for caractere in entrada:
    escada = escada + caractere
    print(escada)

