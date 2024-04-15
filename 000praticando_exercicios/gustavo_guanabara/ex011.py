import math

a = float(input('digite a altura da parede: '))
l = float(input('digite a largura da parede: '))

area = a*l
tinta = area/2
arredondado_para_cima = math.ceil(tinta)

print(f'a quantidade de linta necessaria é {arredondado_para_cima}')

