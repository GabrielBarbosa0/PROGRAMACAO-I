cat_invalid = 'categoria invalida'
a = 'infantil a'
b = 'infantil b'
c = 'juvenil a'
d = 'juvenil b'
e = 'adulto'

idade = int(input('insira a idade:'))
if idade >=5 and idade<= 7: print(a)
elif idade >= 8 and idade<= 10: print(b)
elif idade >=11 and idade<= 13: print(c)
elif idade >=14 and idade<=17: print(d)
elif idade > 18: print(e)
else: print(cat_invalid)