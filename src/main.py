# Imports
import pygame
import os
import sys
import random
import pytmx

from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from Sprite.spritesheet import SpriteSheet
from entities.player.Player import Player

# Inicia a pygame engine
pygame.init()
FPSCLOCK = pygame.time.Clock()
 
# Cores
BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tela
height = 800
width = 600
size = [height, width]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ryder Storm')

#Player
spriteimg = pygame.image.load(os.path.join('res','sprite.png')).convert_alpha()
sprite = SpriteSheet(spriteimg)
player = Player(sprite, 50, 50, 10, 64, 70)


# Printa que o jogo iniciou
print("System UP!")

#Game loop
while True:
    screen.fill(BLACK)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()
            exit()

        #Key event Player
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.direction = player.directions[0]
                player.left = True
                player.cur_frame = 0
            if event.key == K_RIGHT:
                player.direction = player.directions[1]
                player.right = True
                player.cur_frame = 0
            if event.key == K_UP:
                player.up = True
                player.cur_frame = 0
            if event.key == K_DOWN:
                player.down = True
                player.cur_frame = 0
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.left = False
                player.cur_frame = 0
            if event.key == K_RIGHT:
                player.right = False
                player.cur_frame = 0
            if event.key == K_UP:
                player.up = False
                player.cur_frame = 0
            if event.key == K_DOWN:
                player.down = False
                player.cur_frame = 0

    player.Move()
    player.Draw(screen)

    pygame.display.flip()
    FPSCLOCK.tick(30)