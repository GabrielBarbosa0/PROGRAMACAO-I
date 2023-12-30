# 5. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro. 
#c) o terceiro elevado ao cubo.

num1 = int (input('Digite um numero inteiro: '))
num2 = int (input('Digite outro numero inteiro: '))
num_real = float (input('Digite um numero real: '))

letra_a = num1*2 * (num2/2)
letra_b = num1*3 + num_real
letra_c = num_real**3

print('O produto do dobro do primeiro com metade do segundo: ', letra_a)
print('A soma do triplo do primeiro com o terceiro: ', letra_b)
print('O terceiro elevado ao cubo: ', letra_c)

