num = input('Digite um número de 0 a 9999: ')
num_int = int(num)

if num_int > 9999:
    print('Esse número é maior que 9999!')
elif num_int < 0 :
    print('Esse número é menor que 0!')
else:
    num = num.zfill(4)
    
    milhar = num[0]
    centena = num[1]
    dezena = num[2]
    unidade = num[3]

    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhar: {milhar}')

    
