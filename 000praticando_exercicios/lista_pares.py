# lista de numeros, soma de numeros pares

lista_num = str(input('Digite uma lista de numeros separados por virgula: '))
num_separados = lista_num.split(',')
num = 0

for i in num_separados:
    i = int(i)
    if i % 2 == 0:
        num += i
print(num)


