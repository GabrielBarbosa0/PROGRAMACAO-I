# texto_original = str(input('Digite uma frase: '))
# deslocamento = int(input('Digite a chave de deslocamento: '))

# texto_cifrado = ''
# for caractere in texto_original:
#     if caractere.isalpha():  # verifica se o caractere é uma letra
#         if caractere.islower():  # verifica se o caractere é minúsculo
#             novo_caractere = chr(((ord(caractere) - ord('a') + deslocamento) % 26) + ord('a'))
#         else:
#             novo_caractere = chr(((ord(caractere) - ord('A') + deslocamento) % 26) + ord('A'))
#     else:
#         novo_caractere = caractere
#     texto_cifrado += novo_caractere

# print("Texto cifrado:", texto_cifrado)


# Teste cifra de cesar

texto_original = str(input('Digite uma frase: '))
deslocamento = int(input('Digite o valor do deslocamento: '))

texto_cifrado = ""
for caractere in texto_original:
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if caractere in alfabeto_minusculo:
        indice = (alfabeto_minusculo.index(caractere) + deslocamento) % 26
        novo_caractere = alfabeto_minusculo[indice]
    elif caractere in alfabeto_maiusculo:
        indice = (alfabeto_maiusculo.index(caractere) + deslocamento) % 26
        novo_caractere = alfabeto_maiusculo[indice]
    else:
        novo_caractere = caractere
    texto_cifrado += novo_caractere

print("Texto cifrado:", texto_cifrado)


# Descriptografar mensagem

mensagem_cifrada = input("Digite a mensagem cifrada: ")
deslocamento = int(input("Digite o valor do deslocamento: "))

mensagem_descriptografada = ""
for caractere in mensagem_cifrada:
    alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if caractere in alfabeto_minusculo:
        indice = (alfabeto_minusculo.index(caractere) - deslocamento) % 26
        novo_caractere = alfabeto_minusculo[indice]
    elif caractere in alfabeto_maiusculo:
        indice = (alfabeto_maiusculo.index(caractere) - deslocamento) % 26
        novo_caractere = alfabeto_maiusculo[indice]
    else:
        novo_caractere = caractere
    mensagem_descriptografada += novo_caractere

print("Mensagem descriptografada:", mensagem_descriptografada)





