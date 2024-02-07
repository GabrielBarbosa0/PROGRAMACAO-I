numero = int(input('digite um numero inteiro: '))

if numero % 3 == 0 and numero % 4 == 0 : print('O valor é divisivel por 3 e 4')
elif numero % 3 == 0 : print('O valor é divisivel por 3')
elif numero % 4 == 0 : print('O valor é divisivel por 4')
else : print('O valor não é divisivel por 3 ou 4')