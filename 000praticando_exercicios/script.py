num = int(input('Digite um numero inteiro: '))
quantidades_digitos = 0
if num < 0:
    num = num * -1 
      
while num > 0:
    num = num // 10
    quantidades_digitos += 1
print(quantidades_digitos)