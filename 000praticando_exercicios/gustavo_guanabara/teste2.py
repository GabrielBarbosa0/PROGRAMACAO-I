# 5 ///////////////////////////////////////////////////////

string1 = str(input('digite uma string: '))
string2 = str(input('digite outra string: '))
lista1 = ''
lista2 = ''
caracteres_presentes_duas_listas = ''
caracteres_exclusivos_lista1 = ''
caracteres_exclusivos_lista2 = ''
remover_caracteres_repetidos = ''


for i in(string1):
    lista1+=i

for i in(string2):
    lista2+=i

for i in(string1):
    if i in string2:
        caracteres_presentes_duas_listas += i

for i in (string1):
    if i not in string2:
        caracteres_exclusivos_lista1 += i

for i in (string2):
    if i not in string1:
        caracteres_exclusivos_lista2 += i

caracteres_exclusivos_das_duas_listas = caracteres_exclusivos_lista1+caracteres_exclusivos_lista2


for i in(caracteres_exclusivos_das_duas_listas):
    if i not in remover_caracteres_repetidos:
        remover_caracteres_repetidos+= i

salvar_caracteres_presentes_duas_listas = caracteres_presentes_duas_listas

tupla = (salvar_caracteres_presentes_duas_listas, remover_caracteres_repetidos)
print(tupla)
