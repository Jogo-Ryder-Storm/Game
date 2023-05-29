# Imports
import pygame, os, sys, random, pytmx, math
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from src.settings import *
from src.spritesheet import SpriteSheet
from src.entities.Player import Player
from src.entities.Npc import Npc
from src.entities.Entity import Entity
from src.UI import UI
from src.textbox import Textbox
from src.textfile import TextFile


class Game():
    def __init__(self):
        self.active = True
        self.life = 3
    def run(self):
        screen = pygame.display.get_surface()
        spriteimg = pygame.image.load(os.path.join('res','sprite.png')).convert_alpha()
        sprite = SpriteSheet(spriteimg)
        player = Player(sprite, 50, 50, 10, 64, 70, 1)
        player.life = self.life
        desk = pygame.image.load(os.path.join('res','desk.png')).convert_alpha()
        rectdesk = desk.get_rect()
        deskobj = Entity(desk, 300, 200, 0, rectdesk.width, rectdesk.height, 1, "level1")
        deskobj2 = Entity(desk, 800, 300, 0, rectdesk.width, rectdesk.height, 1, "level2")
        textbox = Textbox()
        spriteimgnpc = pygame.image.load(os.path.join('res','npc.png')).convert_alpha()
        spritenpc = SpriteSheet(spriteimgnpc)
        spriteimgnpc2 = pygame.image.load(os.path.join('res','npc2.png')).convert_alpha()
        spritenpc2 = SpriteSheet(spriteimgnpc2)
        npc = Npc(spritenpc, WIDTH/2, HEIGHT/2, 5, 32, 32, 1.7)
        npc2 = Npc(spritenpc2, WIDTH/2, HEIGHT/2, 5, 32, 32, 1.7)

        textFile = TextFile("ranking.txt")
        self.fase = 1
        self.resposta = ""
        start_ticks=pygame.time.get_ticks() #starter tick
        self.ended = False
        ui = UI()
        self.time = 0
        self.max_time = 10
        self.next_stage = False

        tmxdata = load_pygame('map/lvlone/Office2Official.tmx')
        
        
       


        while self.active:
            screen.fill(BLACK)




            imagenew = tmxdata.get_tile_image_by_gid
            for layer in tmxdata.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = imagenew(gid)
                        if tile:
                            calc_x = (math.sqrt(2) * tmxdata.width * x  - math.sqrt(2) * tmxdata.height * y ) / 0.885
                            calc_y =  (math.sqrt(2) * tmxdata.width * x  + math.sqrt(2) * tmxdata.height * y) / 1.77
                            # print(x, y)
                            if layer.name == "background":
                                screen.blit(tile, (calc_x+610, calc_y+80))
                            else:
                                screen.blit(tile, (calc_x+610, calc_y-20)) 

                

                #     image = tmxdata.get_tile_image
                #     screen.blit(image, (0, 0))
                #     cord_x += 1
                #     cord_y += 1

                #     pos_map_x += 1
                #     if(pos_map_x == tmxdata.width - 1):
                #         pos_map_x = 0
                
                # pos_map_y += 1
                # if(pos_map_y == tmxdata.height - 1):
                #     pos_map_y = 0

            

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
                        pos = player.getPlayerFront(screen)
                        if deskobj.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("mesa")
                            textbox.active = True
                        if deskobj2.checkHitBox(pos[0], pos[1]):
                            textbox.defineOption("escada")
                            textbox.active = True
                elif event.type == KEYDOWN and textbox.active == True:
                    player.left = False
                    player.right = False
                    player.up = False
                    player.down = False
                    if event.key == K_g:
                       self.resposta = textbox.getChoice()
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
            
  
            if textbox.choiceMade == True:
                if self.fase == 1:
                    if self.resposta == "Sim":
                        textbox.defineOption("fase-1-correto")
                        textbox.active = True
                        player.time = text_content
                        self.ended = True
                        self.next_stage = True
                        textbox.choiceMade = False
                    
            if (self.time > 9 and self.next_stage == False):
                self.life -= 1
                self.run()
            else:
                 seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        
            if self.life <= 0:
                from src.gameover import Gameover
                gameouver = Gameover()
                gameouver.run()

            player.Draw(screen)
            npc.Draw(screen)
            npc2.Draw(screen)
            deskobj.Draw(screen)
            deskobj2.Draw(screen)
            if(textbox.active == True):
                textbox.draw()
            else:      
                player.block()
                player.Move()    
            npc.Move()
            npc2.Move()
            if self.ended == True:
                textFile.copyFileToTemp()
                textFile.readFile("Player", str(player.time), str(player.life))
                
                self.ended = False

            self.time = int(seconds)
            text_content = str(self.max_time - self.time)
            ui.run(text_content, str(player.life))

            # print(player.time)
            pygame.display.flip()
            FPSCLOCK.tick(30)
