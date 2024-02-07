# Faça um programa que leia 2 strings e informe o conteúdo delas seguido doseu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

primeira_string = 'osso'
segunda_string = 'A base do teto desaba'

print ('A primeira string','"', primeira_string,'"', 'possui: ',(len(primeira_string)), 'caracteres')

print ('A segunda string','"', segunda_string,'"', 'possui: ',(len(segunda_string)), 'caracteres')

if len(primeira_string) == len(segunda_string):
    print('As variaveis possuem a mesma quantidade de caracteres')
else:
    print('As variaveis possuem quantidade diferentes de caracteres')

if primeira_string == segunda_string:
    print('As variaveis são iguais')
else:
    print('As variaveis são diferentes')
