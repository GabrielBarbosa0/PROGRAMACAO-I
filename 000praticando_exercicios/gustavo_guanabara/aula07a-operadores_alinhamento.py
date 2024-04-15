# ordem de precedencia operadores aritmeticos

# 1 ()
# 2 **
# 3 * / // %
# 4 + -
# 25**(1/2) = raiz quadrada de 25 = 5
# 27**(1/3) = raiz cubica de 27 = 3
# print('='*20)

# teste de alinhamento
# nome = input('Qual é o seu nome? ')
# print(f'Prazer em te conhecer {nome:20}!')
# print(f'Prazer em te conhecer {nome:>20}!')
# print(f'Prazer em te conhecer {nome:<20}!')
# print(f'Prazer em te conhecer {nome:^20}!')
# print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {}, \n o produto é {}, \n a divisão é {:.2f}, \n a divisão inteira é {}, \n a potencia' .format(s, m, d, di, e))


