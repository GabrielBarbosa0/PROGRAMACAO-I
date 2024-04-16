# Escreva um programa para calcular o fatorial de um número fornecido pelo 
# usuário.

numero = int(input("Digite um número para calcular o fatorial: "))

resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print(f'O fatorial de {numero} é {resultado}')