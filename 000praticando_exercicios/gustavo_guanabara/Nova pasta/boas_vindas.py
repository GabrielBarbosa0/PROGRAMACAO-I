nome = str(input('Digite seu nome: '))
dia_nascimento = int(input('Digite o dia do seu nascimento: '))
mes_nascimento = (input('Digite o mes do seu nascimento: '))

if nome == 'gabriel':
    print(nome,'é um nome engraçado! voce nasceu do dia', dia_nascimento, ' no mes ', mes_nascimento)
else:
    print(nome + ' é um nome bonito, voce nasceu do dia', dia_nascimento, 'no mes', mes_nascimento)