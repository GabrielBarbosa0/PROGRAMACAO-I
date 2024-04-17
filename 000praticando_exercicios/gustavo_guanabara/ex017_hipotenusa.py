from math import hypot

cateto_oposto = float(input('digite o valor do cateto oposto: '))
cateto_adjacente = float(input('digite o valor do cateto adjacente: '))

# hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2))**(1/2)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'o valor da hipotenusa é: {hipotenusa:.2f}')