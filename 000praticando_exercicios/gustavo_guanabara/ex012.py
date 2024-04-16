preco = float(input('digite o preco original do produto: '))

desconto = preco/100*5
preco_desconto = preco - desconto
# print(desconto)
print(f'R${preco_desconto}')