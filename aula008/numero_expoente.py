# Faça um programa que peça dois números, base e expoente, calcule e 
# mostre o primeiro número elevado ao segundo número. Não utilize a função 
# de potência da linguagem ou o operador de exponenciação

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

while expoente > 0:
    resultado *= base
    expoente -= 1

print(f"Resultado é: {resultado}")
