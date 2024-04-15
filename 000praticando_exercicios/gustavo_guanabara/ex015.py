# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quantidade_dias = int(input('quantos dias o carro foi alugado: ')) * 60

km_percorrido = float(input('digite a quantidade de km percorrida pelo carro: ')) * 0.15

print(f'o total a ser pago é : R${km_percorrido + quantidade_dias}')