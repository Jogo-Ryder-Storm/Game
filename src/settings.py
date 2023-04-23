import pygame

pygame.mixer.init()
#Clock
FPSCLOCK = pygame.time.Clock()

# Tela
WIDTH = 1000
HEIGHT = 800 

# Cores
BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = [51, 51, 51]

MUSIC = pygame.mixer.Sound("res/music.mp3")