# Gabriel Gomes Barbosa

# 1. Crie um programa que receba um número inteiro, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 2021 , então a saída deve ser 4. Obs: O número não deve ser convertido para nenhum outro tipo, logo, todas as operações devem ser realizadas sobre o número inteiro.

# num = int(input('Digite um numero: '))
# count = 0
# while num > 0:
#     count+= 1
#     num //= 10
# print(count)

# 2. Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura) e em seguida, calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5 m².

# import math
# comprimento = float(input('Digite o comprimento da parede'))
# largura = float(input('Digite o largura da parede'))
# altura = float(input('Digite o altura da parede'))
# area = ((comprimento * altura) * 2) + ((largura * altura) * 2)
# azulejo = 1.5
# total = math.ceil(area / azulejo)
# print(total)


# 3. Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas formadas pelos seus dois primeiros e dois últimos dígitos. (1297 = 12 e 97; 5314 = 53 e 14). Escreva um programa quelê um número inteiro n (de 4 algarismos) e verifica se a raiz quadrada de n é igual a soma das dezenas de n. 

# Ex.: n = 9801, dezenas de n = 98 + 01, soma das dezenas = 99, raiz quadrada de n = 99. Portanto,a raiz quadrada de 9801 é igual a soma de suas dezenas.


numero_natual = str(input('Digite um numero natural de quatro algarismos'))
primeiro_par = numero_natual[:2]
segundo_par = numero_natual[2:4]
soma = int(primeiro_par) + int(segundo_par)

raiz = round(int(numero_natual) ** 0.5, 1)
if raiz == soma:
    print('Portanto,a raiz quadrada de 9801 é igual a soma de suas dezenas.', raiz)
print(soma)
print(raiz)

