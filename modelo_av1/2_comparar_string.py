# # Duas listas para comparação
# lista1 = ['A', 'B', 'C', 'D', 'E', 'F']
# lista2 = ['C', 'D', 'E', 'F', 'G', 'H']

# # Convertendo todos os elementos das listas para minúsculas
# lista1_lower = [elemento.lower() for elemento in lista1]
# lista2_lower = [elemento.lower() for elemento in lista2]

# # A) Valores comuns às duas listas
# valores_comuns = []
# for elemento in lista1_lower:
#     if elemento in lista2_lower:
#         valores_comuns.append(elemento)
# print("Valores comuns às duas listas:", valores_comuns)

# # B) Valores que só existem na primeira lista
# valores_apenas_lista1 = []
# for elemento in lista1_lower:
#     if elemento not in lista2_lower:
#         valores_apenas_lista1.append(elemento)
# print("Valores que só existem na primeira lista:", valores_apenas_lista1)

# # C) Valores que existem apenas na segunda lista
# valores_apenas_lista2 = []
# for elemento in lista2_lower:
#     if elemento not in lista1_lower:
#         valores_apenas_lista2.append(elemento)
# print("Valores que só existem na segunda lista:", valores_apenas_lista2)

# # D) Lista com elementos não repetidos das duas listas
# elementos_nao_repetidos = list(set(lista1_lower + lista2_lower))
# print("Elementos não repetidos das duas listas:", elementos_nao_repetidos)







# Duas listas para comparação
lista1 = ['A', 'B', 'C', 'D', 'E', 'F', 'g', 'Gabriel', True]
lista2 = ['C', 'D', 'E', 'F', 'G', 'H', 'a', True]

# A) Valores comuns às duas listas
valores_comuns = []
for elemento in lista1:
    if elemento in lista2:
        valores_comuns.append(elemento)
print("Valores comuns às duas listas:", valores_comuns)

# B) Valores que só existem na primeira lista
valores_apenas_lista1 = []
for elemento in lista1:
    if elemento not in lista2:
        valores_apenas_lista1.append(elemento)
print("Valores que só existem na primeira lista:", valores_apenas_lista1)

# C) Valores que existem apenas na segunda lista
valores_apenas_lista2 = []
for elemento in lista2:
    if elemento not in lista1:
        valores_apenas_lista2.append(elemento)
print("Valores que só existem na segunda lista:", valores_apenas_lista2)

# D) Lista com elementos não repetidos das duas listas
elementos_nao_repetidos = list(set(lista1 + lista2))
print("Elementos não repetidos das duas listas:", elementos_nao_repetidos)
