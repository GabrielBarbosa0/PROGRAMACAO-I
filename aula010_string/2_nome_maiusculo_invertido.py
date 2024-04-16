# Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome, o usuário pode digitar letras maiúsculas ou minúsculas.

nome = str(input('Digite seu nome: '))
texto_invertido = str

for i in range(len(nome)):
    texto_invertido = (nome[-i -1])
    print(texto_invertido.upper())
    