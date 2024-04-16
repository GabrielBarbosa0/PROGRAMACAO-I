l1 = float(input('indique o valor do primeiro lado do triângulo: '))
l2 = float(input('indique o valor do segundo lado do triângulo: '))
l3 = float(input('indique o valor do terceiro lado do triângulo: '))

if (l1 + l2 < l3) or (l2 + l3 < l1) or (l1 + l3 < l2):
    print ('A figura não é um triângulo.')
elif l1 == l2 == l3:
    print('O triângulo é equilátero.')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print ('O triângulo é isósceles.')
else : print ('O triângulo é escaleno.')