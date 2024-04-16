# A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. 
# Faça um algoritmo para coletar e armazenar dados sobre o salário e número 
# de filhos de cada habitante e após as leituras, escrever:
    
# a) Média de salário da população
# b) Média do número de filhos
# c) Maior salário dos habitantes
# d) Percentual de pessoas com salário menor que R$ 150,00

# Obs.: O final da leituras dos dados se dará com a entrada de um “salário negativo”.

salario = 0
num_filhos = 0
media_salario = 0
media_filhos = 0

while salario >= 0:
    salario = float(input('Digite seu salario: '))
    media_salario = salario
    num_filhos = int(input('Digite seu número de filhos: '))
    resultado_media_salario = media_salario
    media_salario = media_salario+resultado_media_salario


# Inicializar variáveis
soma_salarios = 0
soma_filhos = 0
maior_salario = float('-inf')  # Inicializar com um valor negativo infinito
contador_pessoas_menor_150 = 0

# Leitura inicial
salario = float(input("Digite o salário (digite um valor negativo para encerrar): "))

# Processamento dos dados
while salario >= 0:
    # Leitura do número de filhos
    numero_filhos = int(input("Digite o número de filhos: "))

    # Atualizar as variáveis
    soma_salarios += salario
    soma_filhos += numero_filhos

    # Verificar e atualizar o maior salário
    if salario > maior_salario:
        maior_salario = salario

    # Verificar se o salário é menor que R$ 150,00
    if salario < 150:
        contador_pessoas_menor_150 += 1

    # Leitura para a próxima iteração
    salario = float(input("Digite o salário (digite um valor negativo para encerrar): "))

# Calcular médias
media_salarios = soma_salarios / (contador_pessoas_menor_150 + 1)  # Evitar divisão por zero
media_filhos = soma_filhos / (contador_pessoas_menor_150 + 1)  # Evitar divisão por zero

# Calcular percentual de pessoas com salário menor que R$ 150,00




