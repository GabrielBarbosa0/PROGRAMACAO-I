# Escreva um programa para contar a quantidade de números pares entre dois números quaisquer fornecidos pelo usuário?

# FOR

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
contador_par = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        contador_par += 1
        
print(f'A quantidade de números pares é: {contador_par}')

# WHILE

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
contador_par = 0

numero_atual = num1

while numero_atual < num2:
    if numero_atual % 2 == 0:
        contador_par += 1
    numero_atual += 1

print(f'A quantidade de números pares é: {contador_par}')