# Imports
import pygame, os, sys, random, pytmx, math
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from src.settings import *
from src.spritesheet import SpriteSheet
from src.entities.Player import Player
from src.entities.Entity import Entity

class Game():
    def __init__(self):
        self.active = True
    def run(self):
        screen = pygame.display.get_surface()
        spriteimg = pygame.image.load(os.path.join('res','sprite.png')).convert_alpha()
        sprite = SpriteSheet(spriteimg)
        player = Player(sprite, 50, 50, 10, 64, 70, 2)
        desk = pygame.image.load(os.path.join('res','desk.png')).convert_alpha()
        rectdesk = desk.get_rect()
        deskobj = Entity(desk, 300, 200, 0, rectdesk.width, rectdesk.height, 1)
        while self.active:
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
            if(player.x > WIDTH-100):
                player.x = WIDTH-100
            if(player.y < 0):
                player.y = 0
            if(player.y > HEIGHT-140):
                player.y = HEIGHT-140

            pygame.draw.rect(screen, RED, (player.x, player.y, player.width * player.scale, player.height * player.scale), 3)   
            pygame.draw.rect(screen, (0, 100, 255), (deskobj.x, deskobj.y, deskobj.width, deskobj.height), 3) 

            if(player.isColliding(deskobj)):
                player.colisao = True
            else:
                player.colisao = False
            
            player.block()
            player.Move()    
            player.Draw(screen)
            deskobj.Draw(screen)
            pygame.display.flip()
            FPSCLOCK.tick(30)
