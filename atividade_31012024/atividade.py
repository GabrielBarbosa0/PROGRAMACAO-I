#GABRIEL GOMES BARBOSA

#Questão 1. Faça um programa que leia um número inteiro e o imprima.

numero = int(input("Digite um numero: "))
print(f'Seu numero: {numero}')

#////////////////////////////////////////////

#Questão 2. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma = n1 + n2 + n3

print(f'A soma dos números é: {soma}')

#///////////////////////////////////////////

#Questão 3. Desenvolva um algoritmo em python que leia um número inteiro e imprima o seu antecessor e seu sucessor.

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print(f'{numero} \n Antecessor: {antecessor} \n Sucessor: {sucessor}')

#//////////////////////////////////////////


#Questão 4. Leia uma temperatura em graus Celsius e apresente-a convertida em graus
#Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a
#temperatura em Fahrenheit e C a temperatura em Celsius.

graus_celsius = float(input("Digite o graus Celsius: "))

fahrenheit = graus_celsius*(9.0/5.0)+32.0

print(f'({graus_celsius:2f} °C x 9/5) + 32 = {f:2} °F')

#//////////////////////////////////////////

#Questão 5. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertidaem m/s (metros por segundo). A fórmula de conversão é: M= K/3.6, sendoKavelocidade em km/h e M em m/s. 

km_h = float(input("Digite um valor em Km/h: "))
m_s = km_h/3.6
print(f'Valor de {km_h}Km/h em m/s: {m_s:2f}m/s')

#//////////////////////////////////////////

#Questão 6. Leia quatro notas, calcule a média aritmética e imprima o resultado. 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f'A média das notas é: {media:.2f}')

#//////////////////////////////////////////

#Questão 7. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares. 

real_brasileiro = float(input("Digite o valor em BR$: "))

#VALOR DO DOLAR ATUAL DIA 27/01/2024 US$ 1.00 = R$ 4.9167 ~ 4.92
dolar_americano = 4.9167

conversor = real_brasileiro/dolar_americano

print(f'{conversor:.2f}')

#//////////////////////////////////////////

#Questão 8. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é π*r² , considere π = 3.141592. 

raio = float(input("Digite o valor do raio: "))
PI = 3.141592

area_circle = PI * (raio ** 2)
print(f'''O valor da área de raio: {raio} é: {area_circle}
Valor Reduzido: {area_circle:.2f}''')

#//////////////////////////////////////////

#Questão 9. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total: 
#    - O primeiro ganhador receberá 46%; 
#    - O segundo receberá 32%; 
#    - O terceiro receberá o restante;
#    Calcule e imprima a quantia ganha por cada um dos ganhadores.

valor_premio = 780000.00

primeiro_ganhador = valor_premio * 0.46
segundo_ganhador = valor_premio * 0.32
terceiro_ganhador = valor_premio - (primeiro_ganhador + segundo_ganhador)

print(f'''O Primeiro lugar ganha: R$ {primeiro_ganhador:.2f}
          O Segundo lugar ganha: R$ {segundo_ganhador:.2f}
          O terceiro ganhador ganha: R$ {terceiro_ganhador:.2f}''')

#//////////////////////////////////////////


# Estruturas condicionais


#Questão 10. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: 
#- O número digitado ao quadrado 
#- A raiz quadrada do número digitado 

numero = int(input("Digite um número: "))

if numero > 0:
    quadrado = numero ** 2
    raiz = numero ** 0.5
    print(f'''          
O número {numero} elevado ao quadrado: {quadrado}
A Raiz do número {numerom} é: {raiz}
''')
    
elif numero == 0:
    print("Seu número é 0 logo todos os resultados serão 0")
else:
    print("Seu número é negativo")

#//////////////////////////////////////////
    
#Questão 11. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar, positivo ou negativo. 

numero = int(input("Digite um número: "))

if numero >= 0 and numero %2==0:
    print(f'{numero} é Positivo e é Par')
elif numero > 0 and numero %2 == 1:
    print(f'{numero} é Positivo e é Ímpar')
elif numero < 0 and numero %2==0:
    print(f'{numero} é Negativo e é Par')
elif numero < 0 and numero %2 == 1:
    print(f'{numero} é Negativo e é Ímpar')


#//////////////////////////////////////////
    
#Questão 12. Faça um programa que leia 2 notas de um aluno, verifique se as notas sãoválidas e exiba na tela a média destas notas. Uma nota válida deveser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possuaumvalor válido, este fato deve ser informado ao usuário e o programa termina. 

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

if primeira_nota < 0 or segunda_nota < 0:
    print("Desculpe uma das notas é inválidas!!")
elif primeira_nota > 10 or segunda_nota > 10:
    print("Desculpe uma das notas é maior que 10")
else:
    media = (primeira_nota + segunda_nota) / 2
    print(f'Sua média é: {media}')

#//////////////////////////////////////////


#Questão 13. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura): 
#- Homens: (72.7 * h) − 58 
#- Mulheres: (62, 1 * h) − 44, 7 

nome = input("Digite Seu nome: ").capitalize()
altura = float(input(f'Certo {nome}, agora digite sua altura: '))
sexo = input("Estamos quase lá, agora digite seu sexo, (M) para Masculino e (F) para feminino: ").upper()

if sexo == "F":
   peso = (62.1 * altura) - 44.7
   print(f"Olá {nome}, Seu peso ideal é: {peso:.2f}Kg")
elif sexo == "M":
    peso =(72.7 * altura) - 58
    print(f"Olá {nome}, Seu peso ideal é: {peso:.2f}Kg")
else:
    print("Algum dado digitado é inválido")


#//////////////////////////////////////////
    

#Questão 14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela seoaluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias. 

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segubda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

if primeira_nota < 0 or segunda_nota < 0 or terceira_nota < 0:
    print("Erro!, nota não pode ser menor que 0")
elif primeira_nota > 10 or segunda_nota > 10 or terceira_nota > 10:
    print("Erro!, notas não pode ser maior que 10: ")
else:
    primeira_nota *= 2
    segunda_nota *= 3
    terceira_nota *= 5
    peso_total = 2 + 3 + 5
    media = (primeira_nota + segunda_nota + terceira_nota) / peso_total
    if media >= 0 and media <= 2.9:
        print(f"{media:.2f}: Que pena, esse aluno está reprovado")
    elif media >= 3 and media <= 4.9:
        print(f"{media:.2f}: Que pena, esse aluno está de recuperação")
    else:
        print(f"{media:.2f}: Parabéns esse aluno foi aprovado!")


#//////////////////////////////////////////

#Questão 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
#- "Telefonou para a vítima?" 
#- "Esteve no local do crime?" 
#- "Mora perto da vítima?" 
#- "Devia para a vítima?" 
#- "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deveser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

print("Responda todas as perguntas com SIM ou NÃO!!")

count = 0

pergunta1 = input("Telefonou para a vítima?" ).upper()
if pergunta1 == "SIM":
    count += 1

pergunta2 = input("Esteve no local do crime?" ).upper()
if pergunta2 == "SIM":
    count += 1

pergunta3 = input("Mora perto da vítima?" ).upper()
if pergunta3 == "SIM":
    count += 1

pergunta4 = input("Devia para a vítima?" ).upper()
if pergunta4 == "SIM":
    count += 1

pergunta5 = input("Já trabalhou com a vítima?" ).upper()
if pergunta5 == "SIM":
    count += 1

if count == 2:
    print("Você é considerado suspeito!")
elif count == 3 or count == 4:
    print("Você é considerado cúmplice!!")
elif count == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente")


#//////////////////////////////////////////

#Questão 16. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são: 
#- Ter pelo menos 65 anos, 
#- Ou ter trabalhado pelo menos 30 anos, 
#- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade: "))
tempo_trabalho = int(input("Digite o tempo de total de trabalho: "))

if idade < tempo_trabalho:
    print("Erro!, digite um valor válido!!")
else:
    if idade >= 65 or tempo_trabalho >= 30:
      print("Aposentadoria aprovada!!")
    elif idade >= 60 and tempo_trabalho >= 25:
      print("Aposentadoria aprovada!!")
    else:
       print("Aposentadoria negada!")


#//////////////////////////////////////////
    
#Questão 17. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagemdeacordo com a tabela abaixo: 
# MENOR QUE 8 = VENDA O CARRO
# ENTRE 8 E 14 = ECONIMICO
# MAIOR QUE 14 = SUPER ECONOMICO
#OBS: NO PDF O MAIOR QUE TA 12

distancia = int(input("Digite a distancia: "))
kilometro_litro = int(input("Digite a quantidade em Litros de gasolina: "))

distancia_kilometro = distancia / kilometro_litro

if distancia_kilometro < 8:
    print("Por favor venda o carro!!")
elif distancia_kilometro >= 8 and distancia_kilometro <= 14:
    print("Carro econômico!")
elif distancia_kilometro > 14:
    print("Carro super econômico!!")

#//////////////////////////////////////////

'''■ Estruturas de repetição '''

#Questão 18. Escreva um programa que escreva na tela, de 1 até 100, de 1 em1, 2 vezes. A primeira vez deve usar a estrutura de repetição “for”, a segunda vez a estrutura “while”. 

#WHILE
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

#FOR
for i in range(1, 101):
    print(i, end=" ")

#//////////////////////////////////////////

#Questão 19. Faça um programa que peça ao usuário para digitar 10 valores e some-os e imprima o resultado. 

soma = 0
for i in range(1,11):
    num = int(input("Digite um número: "))
    sum += num
print(f'A soma dos números é: {soma}')

#//////////////////////////////////////////

#Questão 20. Faça um programa que leia 10 inteiros e imprima sua media

sum_num = 0
for i in range(1, 11):
    num = int(input("Digite um numero: "))
    sum_num += num
media_num = sum_num / 10
print(f'A media dos numeros digitados e: {media_num:.2f}')

#//////////////////////////////////////////

#Questão 21. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média. 

sum = 0
count = 0
for i in range(1, 11):
    num = int(input("Digite um numero 13: "))
    if num > 0:
        sum += num
        count += 1
       
media = sum / count
print(f'A média dos números é: {media}')

#//////////////////////////////////////////

#Questão 22. Faça um programa que leia um numero inteiro “N” e depois imprima os Nprimeiros números naturais ímpares. 


num = int(input("Digite um número inteiro (N): "))
impar = 1
for i in range(num):
    print(impar, end=' ')
    impar += 2

#//////////////////////////////////////////
    
#Questão 23. Faça um programa que leia um numero inteiro positivo “N” e imprima todos os números naturais de 0 até “N” em ordem crescente.

num = int(input("Digite um número: "))
i = 0

if num >= 0:
    while i <= num:
      print(i, end=" ")
      i += 1
else:
    print("Digite um valor válido!!")
#//////////////////////////////////////////
    
#Questão 24. Faça um programa que leia um numero inteiro positivo “N” e imprima todos osnúmeros naturais de 0 até N em ordem decrescente. 

num = int(input("Digite um número: "))

if num > 0:
    while num >= 0:
     print(num, end=" ")
     num -= 1
else:
    print("Digite um valor válido!!")

#//////////////////////////////////////////

#Questão 25. Faça um programa que receba dois números. Calcule e mostre: - a soma dos números pares desse intervalo de números, incluindo os númerosdigitados; 

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

sum = 0
mult = 1

if num1 < num2:
    while num1 <= num2:
  
      if num1 %2 == 0:
        sum += num1
        mult *= num1
      num1 += 1
elif num1 > num2:
    while num1 >= num2:
  
      if num1 %2 == 0:
        sum += num1
        mult *= num1
      num1 -= 1

print(f'''
      
As somas dos números pares desse intervalo: {sum}
A multiplicação desse intervalo é: {mult}

''')

#/////////////////////////////////

#Questão 26. Faça um programa que imprima a tabuada de multiplicação de 1 a 9; 

num = int(input("Qual número que deseja saber a tabuada? "))

i = 1
while i < 10:
    mult = num * i
    print(f'{num} X {i:2} = {mult:2}')
    i+=1

#/////////////////////////////////

#27. Escreva um programa que leia um numero inteiro positivo “N” e emseguida
#imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6, temos:

#1 
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
#16 17 18 19 20 21


numero_inteiro = int(input("Digite um número inteiro: "))

numero = 1

for li in range(1, numero_inteiro+1):
    for coluna in range(1, li+1):
        print(numero, end=" ")
        numero += 1
    print()

#/////////////////////////////////