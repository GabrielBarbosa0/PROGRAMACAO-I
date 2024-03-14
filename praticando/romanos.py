def int_para_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    resultado = ''
    i = 0

    while numero > 0:
        for _ in range(numero // valores[i]):
            resultado += romanos[i]
            numero -= valores[i]
        i += 1

    return resultado

# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para converter e imprime o resultado
print("O número romano correspondente é:", int_para_romano(numero))