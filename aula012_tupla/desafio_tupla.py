tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)

tupla_vazia = ()

for i in tupla:
    if i not in tupla_vazia:
        tupla_vazia+= i,
print(tupla_vazia)


