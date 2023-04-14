# Imports
import pygame
import os
import sys
import random
import pytmx
import math

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
width = 1000
size = [width, height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ryder Storm')

#Player
spriteimg = pygame.image.load(os.path.join('res','sprite.png')).convert_alpha()
sprite = SpriteSheet(spriteimg)
player = Player(sprite, 50, 50, 10, 64, 70)

# Define as coordenadas do centro do círculo
circle_x = width // 4 
circle_y = height // 4
# Define o raio do círculo
circle_radius = 50

# Printa que o jogo iniciou
print("System UP!")


###
desk = pygame.image.load(os.path.join('res','desk.png')).convert_alpha()
desk = pygame.transform.scale(desk, (200,200))
rect1 = desk.get_rect()
rect1.x = 300
rect1.y = 100




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
                player.actualDirection = player.directions[0]
                player.currentFrame = player.walkSpriteFrame[0]
                player.left = True
                player.cur_frame = 0
            if event.key == K_RIGHT:
                player.actualDirection = player.directions[2]
                player.currentFrame = player.walkSpriteFrame[1]
                player.right = True
                player.cur_frame = 0
            if event.key == K_UP:
                player.actualDirection = player.directions[3]
                player.up = True
                player.cur_frame = 0
            if event.key == K_DOWN:
                player.actualDirection = player.directions[1]
                player.down = True
                player.cur_frame = 0
        if event.type == KEYUP:
            if event.key == K_LEFT:
                player.left = False
                player.cur_frame = 0
            elif event.key == K_RIGHT:
                player.right = False
                player.cur_frame = 0
            elif event.key == K_UP:
                player.up = False
                player.cur_frame = 0
            elif event.key == K_DOWN:
                player.down = False
                player.cur_frame = 0

    if(player.x < -20 ):
        player.x = -20
    if(player.x > width-100):
        player.x = width-100
    if(player.y < 0):
        player.y = 0
    if(player.y > height-140):
        player.y = height-140

    screen.blit(desk, rect1)
    
    pygame.draw.rect(screen, (0, 100, 255), (player.x, player.y, player.width, player.height), 3)  # width = 3
    pygame.draw.rect(screen, (0, 100, 255), (rect1.x, rect1.y,200, 200), 3)  # width = 3

    while(player.colisao == True):
        player.block()

    #Checa colisão
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    if player_rect.colliderect(rect1):
        player.colisao = True
    else:
        player.colisao = False
        player.Move()
        
        
    player.Draw(screen)

    pygame.display.flip()
    FPSCLOCK.tick(30)