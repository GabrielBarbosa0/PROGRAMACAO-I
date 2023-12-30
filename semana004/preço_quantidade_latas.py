import math

metros = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litro = metros / 3
result = litro / 18
# o "math.ceil" serve para arredondar o numero para cima
total = math.ceil(result)

print("Preço total: R$", total * 80, " Quantidade de lata(s) de tinta necessárias: ", total)

