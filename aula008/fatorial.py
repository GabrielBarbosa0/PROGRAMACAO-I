numero = int(input("Digite um número para calcular o fatorial: "))
# Escreva um programa para calcular o fatorial de um número fornecido pelo 
# usuário.

resultado = 1

for i in range(1, numero + 1):
    resultado *= i
    print(i, 'iterador')
    print(resultado, 'resultado')

print(f'O fatorial de {numero} é {resultado}')