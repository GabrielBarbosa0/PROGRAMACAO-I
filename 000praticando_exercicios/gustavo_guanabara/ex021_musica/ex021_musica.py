import pygame
import os

# Definindo o diretório atual como diretório de trabalho
os.chdir(os.path.dirname(__file__))

pygame.init()

# Carregando e reproduzindo a música
pygame.mixer.music.load('./ex021.mp3')
pygame.mixer.music.play()

# Aguardando até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Adicionando uma pausa de 2 segundos após o término da música
pygame.time.delay(2000)

# Finalizando o pygame
pygame.quit()


