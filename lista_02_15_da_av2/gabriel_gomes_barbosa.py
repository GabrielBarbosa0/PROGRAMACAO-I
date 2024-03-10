#Nome: Gabriel Gomes Barbosa

#Questão 1
'''
num = int(input('Digite um número inteiro: '))
cont = 0

while num > 0:
    digito = num % 10
    cont += 1
    num //= 10
print(f"o total de digitos desse número é: {cont}")
'''

#Questão 2
'''
import math
comprimento = float(input('Digite o valor do comprimento: '))
largura = float(input('Digite o valor da largura: '))
altura = float(input('Digite o valor da altura: '))
azulejo = 1.5

area_total = ((comprimento * altura * 2) + (largura * altura * 2))
total = math.ceil(area_total / azulejo)
print(f"A quantidade necessária de azulejos para a obra será: {total}")
'''

#Questão 3
'''
num = str(input('Digite um numero natural de quatro algarismos: '))
primeiro_par = num[:2]
segundo_par = num[2:4]
soma = int(primeiro_par) + int(segundo_par)

raiz = round(int(num) ** 0.5, 1)
if raiz == soma:
    print('A raiz quadrada do número é igual a soma de suas dezenas:', raiz)
else: 
    print (f'A raiz quadrada do número é diferente a soma de suas dezenas.')
    print(f'soma: {soma} ')
    print(f'raiz: {raiz} ')
'''

#Questão 4
'''
lista1 = ['lucas', 'coca','python',1,2,3]
lista2 = ['churras', 'lucas','abacate',2,3,4]

comuns = [valor for valor in lista1 if valor in lista2]
print(f'Os valores comuns das listas são: {comuns}')

somente_lista1 = [valor for valor in lista1 if valor not in lista2]
print(f'Os valores que existem somente na lista 1 são: {somente_lista1}')

somente_lista2 = [valor for valor in lista2 if valor not in lista1]
print(f'Os valores que existem somente na lista 2 são: {somente_lista2}')

unicos = list(set(lista1 + lista2))
print(f'Os elementos que não repetidos em ambas as listas são: {unicos}')

print(f'A primeira lista sem os elementos repetidos na segunda{somente_lista1}')
'''

#Questão 5

import random
'''
dado = [0] * 6
for _ in range(100):
    resultado = random.randint(1, 6)
    dado[resultado - 1] += 1

for i in range(6):
    print(f"O valor {i+1} foi obtido {dado[i]} vezes.")
'''

#Questão 6
'''
num = int(input())

print(num)
cedulas = [100, 50, 20, 10, 5, 2, 1]

for i in cedulas:
    quant = num//i
    print(f'{quant} nota(s) de R$ {i},00')
    num -= quant*i
'''

#Questão 7
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

cur = 300 * num1
boi = 1500 * num2
boto = 600 * num3
map = 1000 * num4
lara = 150 * num5

mandioca = cur + boi + boto + map + lara + 225
print(mandioca)
'''

#Questão 8
'''
cpf = str(input())
cpf_numero = cpf.replace(".","").replace("-","")

print(cpf_numero[0:3])
print(cpf_numero[3:6])
print(cpf_numero[6:9])
print(cpf_numero[9:11])
'''

#Questão 9
'''
distancia = int(input())

if distancia <= 800:
    print(1)
elif 800 < distancia <= 1400:
    print(2)
elif 1400 < distancia <= 2000:
    print(3)
'''

#Questão 10
'''
num = int(input())

for i in range (num):
    string = str(input())
    chave = int(input())
    resposta = ''.join([chr(((ord(letra) - 65 - chave + 26) % 26) + 65) for letra in string])
    
    print(resposta)
'''