peso = float(input('digite o seu peso em kg: '))
altura = float(input('digite o sua altura em metros: '))
imc = peso/altura**2

if imc < 20 : av = ('Abaixo do peso')
elif imc >= 20 and imc <= 25 : av = ('Normal')
elif imc >= 25 and imc <= 30 : av = ('Sobrepeso')
elif imc >= 30 and imc <= 35 : av = ('Obesidade leve')
elif imc >= 35 and imc <= 40 : av = ('Obesidade moderada')
else : av = ('Obesidade mórbida')

print('O seu IMC é equivalente a {:.1f}'.format(imc),'e sua avaliação está na categoria:', av)