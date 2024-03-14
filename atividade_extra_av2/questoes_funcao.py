# Gabriel Gomes Barbosa

# Questões de Função:

# Questão 1
'''
def soma(n1, n2, n3):
    return n1+n2+n3
print(soma(1,2,3))
'''

#Questão 2
'''
def inteiro(n):
    if n > 0: return 'P'
    else: return 'N'    
n = int(input('Digite um número inteiro: '))

print(inteiro(n))
'''

#Questão 3
'''
def escada(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print (i, end=' ')
        print()

n = int(input('Digite um número inteiro: '))
print(escada(n))
'''

#Questão 4
'''
def reverso(n):
    n = str(n)
    return int(n[::-1])

n = int(input('Digite um número inteiro: '))
print(reverso(n))
'''

#Questão 5
'''
def valor(n):
    if not(type(n)==int):
        return 
    resultado = 1
    if n < 0: n *= -1
    while n > 0:
        n //= 10
        if n > 0: resultado += 1
    return resultado

n = int(input('Digite um número inteiro: '))
print(valor(n))
'''

#Questão 6
'''
def potencia(a, b):
    resultado = a
    if b == 0: return 1
    else:
        for i in range(2, b+1):
            resultado *= a
        return resultado

a = int(input('Digite um valor inteiro: '))
b = int(input('Digite um valor que será a potencia do valor anterior: '))
print(potencia(a, b))
'''

#Questão 7
'''
lista_romana = (  
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
)
def romana(n):
    result = ''
    for elemento, romana in lista_romana:
        cociente = n//elemento
        n = n % elemento      
        result += romana * cociente
    return result

n = int(input('Digite um número inteiro: '))
print(romana(n))
'''

#Questão 8
'''
def analisar_parametros(*args):
    contagem_tipos = {
        'int': 0,
        'float': 0,
        'str': 0,
        'bool': 0,
        'list': 0,
        'tuple': 0,
        'dict': 0
    }
    
    numeros = []
    
    for arg in args:
        tipo = type(arg)._name_
        
        if tipo in contagem_tipos:
            contagem_tipos[tipo] += 1
        
        if isinstance(arg, (int, float)):
            numeros.append(arg)
        elif isinstance(arg, (list, tuple, dict)):
            contagem_tipos[tipo] += len(arg)
    
    
    for tipo, quantidade in contagem_tipos.items():
        print(f"Quantidade de parâmetros do tipo {tipo}: {quantidade}")
    
    if numeros:
        print(f"Maior valor numérico: {max(numeros)}")
        print(f"Menor valor numérico: {min(numeros)}")


analisar_parametros(1, 2, 3, "texto", 4.5, True, False, "outra string", -10, [1, 2, 3], (4))
'''

#Questão 9
''''
def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return -numero

num = -5
print(f"O valor absoluto de {num} é: {valor_absoluto(num)}")
'''

#Questão 10
'''
def fizz_buzz(numero):
    for i in range(1, numero):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(16)
'''

#Questão 11 
'''
def decrescente(n):
    if n < 0:
        return
    print(n)
    decrescente(n - 1)

n = int(input('Digite um número inteiro: '))
print(decrescente(n))
'''

#Questão 12
'''
def fatorial_duplo(n):
    if n <= 0:
        return 1
    elif n % 2 == 0:
        return fatorial_duplo(n - 1)
    else:
        return n * fatorial_duplo(n - 2)


numero = int(input('Digite um número natural ímpar: '))
resultado = fatorial_duplo(numero)
print(f"O fatorial duplo de {numero} é: {resultado}")
'''

#Questão 13
'''
def multiplo(num1, num2):
    return num1 % num2 == 0

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor para verificar se este é mutiplo do valor anterior: '))
print(multiplo(num1,num2))
'''

#Questão 14
'''
def potencia(n):
    potencia = 1
    while potencia <= n:
        print(potencia)
        potencia *= 2

n = int(input("Digite um número: "))
print("Potências de 2 menores ou iguais a", n)
potencia(n)
'''

#Questão 15
'''
def fib(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

n = int(input("Digite o valor de n para a sequência de Fibonacci: "))
print(fib(n))
'''

#Questão 16
'''
def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
ano = int(input('Digite o ano para saber se é bissexto ou não: '))
print(bissexto(ano))
'''