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
# Define as coordenadas iniciais das imagens
rect1.x = 300
rect1.y = 100



# Define as coordenadas do canto superior esquerdo do retângulo
rect_x = 500
rect_y = 500

# Define o tamanho do retângulo
rect_width = 200
rect_height = 100

###

#Game loop
while True:
    screen.fill(BLACK)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()
            exit()
        print(player.direcao)
        #Key event Player
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.direcao = player.direcoes[0]
                player.direction = player.directions[0]
                player.left = True
                player.cur_frame = 0
            if event.key == K_RIGHT:
                player.direcao = player.direcoes[2]
                player.direction = player.directions[1]
                player.right = True
                player.cur_frame = 0
            if event.key == K_UP:
                player.direcao = player.direcoes[3]
                player.up = True
                player.cur_frame = 0
            if event.key == K_DOWN:
                player.direcao = player.direcoes[1]
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

    if(player.x < -20 ):
        player.x = -20
    if(player.x > width-100):
        player.x = width-100
    if(player.y < 0):
        player.y = 0
    if(player.y > height-140):
        player.y = height-140

    screen.blit(desk, rect1)
    # Desenha o retângulo na superfície da janela
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    #distance = math.sqrt((circle_center[0] - (player.x + player.size // 2))**2 + (circle_center[1] - (player.y + player.size // 2))**2)
    #if distance <= circle_radius + player.size // 2:
      # Se o papa bolinhas encostar no círculo vermelho o círculo vermelho é reiniciado
    # CB: Círculo Branco    CV: Círculo Vermelho 
    #        y + altura CB          y CV                    y CB                y + altura CV            x + largura CB           x CV                x CB                 x CV
    #if (player.y + 20 >= circle_y - 10  and player.y - 20 <= circle_y + 10) and (player.x +20  >= circle_x - 10 and player.x - 20 <= circle_x + 20): 
        #print("Colisão entre o quadrado e o círculo!")
    
    
    pygame.draw.rect(screen, (0, 100, 255), (player.x, player.y, player.width, player.height), 3)  # width = 3
    pygame.draw.rect(screen, (0, 100, 255), (rect1.x, rect1.y,200, 200), 3)  # width = 3


    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    if player_rect.colliderect(rect1):
        player.colisao = True
    else:
        player.colisao = False
        player.Move()
        
    while(player.colisao == True):
        player.block()
    
    player.Draw(screen)

    pygame.display.flip()
    FPSCLOCK.tick(30)