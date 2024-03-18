tupla = (1, 1, 2, 3, 5, 4, 4)
tupla_filtrada = ()

for i in tupla:
    if i not in tupla_filtrada:
        tupla_filtrada += i,

print(tupla_filtrada)
    







