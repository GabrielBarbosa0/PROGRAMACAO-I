# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele 
# deseja ver a tabuada.

numero = int(input('Digite um número de 1 a 10: '))
resultado = 1

if 0 <= numero <=  10:
    for i in range(1, 10+1):
        resultado = numero * i 
        print(f'{numero} X {i} = {resultado}')
else:
    print('Número inválido, digite um número de 1 a 10')

