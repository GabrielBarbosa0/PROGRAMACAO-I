# Solicita uma string ao usuário
entrada = input("Digite uma string: ")

# Inicializa uma string vazia para construir a escada
escada = ""

# Percorre cada caractere na string de entrada de forma reversa
for caractere in reversed(entrada):
    # Adiciona o caractere à escada
    escada = caractere + escada
    # Imprime a escada atual
    print(escada)
