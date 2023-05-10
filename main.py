import pygame
from src.settings import *
from src.menu import Menu

# Inicia a pygame engine
pygame.init()
pygame.font.init()
pygame.display.set_caption('Ryder Storm')
screen = pygame.display.set_mode([WIDTH, HEIGHT])

MUSIC.play(-1)

# Printa que o jogo iniciou
print("System UP!")

if __name__ == "__main__":
    menu = Menu()
    menu.run()