lista1 = []
lista2 = []

for i in range(10):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista1.append(num)
    else: lista2.append(num)
    
print(f'A lista de numeros pares é: {lista1}')
print(f'A lista de numeros ímpares é: {lista2}')
    