# Imports
import pygame, os, sys, random, pytmx, math
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from src.settings import *
from src.spritesheet import SpriteSheet
from src.entities.Player import Player
from src.entities.Entity import Entity
from src.textbox import Textbox

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
        deskobj2 = Entity(desk, 800, 300, 0, rectdesk.width, rectdesk.height, 1)


        textbox = Textbox("level3")
        while self.active:
            screen.fill(BLACK)
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    exit()

                #Key event Player
                if event.type == KEYDOWN and textbox.active == False:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
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
                    if event.key == K_g:
                        #textbox.active = True
                        deskobj.checkHitBox(player.x, player.y)
                        deskobj2.checkHitBox(player.x, player.y)
                elif event.type == KEYDOWN and textbox.active == True:
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    if event.key == K_g:
                        textbox.active = False
                        textbox.esc = 0
                    if event.key == K_LEFT:
                        textbox.esc -= 1
                        textbox.change_esc()
                    if event.key == K_RIGHT:
                        textbox.esc += 1
                        textbox.change_esc()
                if event.type == KEYUP and textbox.active == False:
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

            #pygame.draw.rect(screen, RED, (player.x, player.y, player.width * player.scale, player.height * player.scale), 3)   
            #pygame.draw.rect(screen, (0, 100, 255), (deskobj.x, deskobj.y, deskobj.width, deskobj.height), 3) 

            if(player.isColliding(deskobj) or player.isColliding(deskobj2)):
                player.colisao = True
            else:
                player.colisao = False
            
            player.Draw(screen)
            deskobj.Draw(screen)
            deskobj2.Draw(screen)
            if(textbox.active == True):
                textbox.draw()
            else:      
                player.block()
                player.Move()    


            pygame.display.flip()
            FPSCLOCK.tick(30)
