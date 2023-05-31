import pygame
from src.settings import *
from src.inputname import inputName

# Inicia a pygame engine
pygame.init()
pygame.font.init()
pygame.display.set_caption('Ryder Storm')
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Printa que o jogo iniciou
print("System UP!")

if __name__ == "__main__":
    name = inputName()
    #from src.gameover import Gameover
    #name = Gameover()
    name.run()