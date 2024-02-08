# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordena os números em ordem crescente
crescente = [num1, num2, num3]
crescente.sort()

# Ordena os números em ordem decrescente
decrescente = sorted(crescente, reverse=True)

# Imprime os números em ordem crescente e decrescente
print("Em ordem crescente:", crescente)
print("Em ordem decrescente:", decrescente)
