from math import radians, sin, cos, tan

angulo = float(input('digite o valor do angulo: '))
seno_angulo = sin(radians(angulo))
cosseno_angulo = cos(radians(angulo))
tangente_angulo = tan(radians(angulo))

print(f'seno = {seno_angulo:.2f} cosseno = {cosseno_angulo:.2f} tangente = {tangente_angulo:.2f}')