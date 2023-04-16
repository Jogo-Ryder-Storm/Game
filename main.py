# Imports
import pygame, os, sys, random, pytmx, math
from pygame.locals import *
from pytmx.util_pygame import load_pygame

# Modulos
from src.settings import *
from src.spritesheet import SpriteSheet
from src.entities.Player import Player
from src.text import Text

# Inicia a pygame engine
pygame.init()
FPSCLOCK = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Ryder Storm')
# Printa que o jogo iniciou
print("System UP!")
class Game():
    def __init__(self):
        self.active = True
    def run(self):
        spriteimg = pygame.image.load(os.path.join('res','sprite.png')).convert_alpha()
        sprite = SpriteSheet(spriteimg)
        player = Player(sprite, 50, 50, 10, 64, 70)
        deskWidth = 150
        deskHeight = 100
        desk = pygame.image.load(os.path.join('res','desk.png')).convert_alpha()
        desk = pygame.transform.scale(desk, (deskWidth,deskHeight))
        rect1 = desk.get_rect()
        rect1.x = 300
        rect1.y = 200
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

            screen.blit(desk, rect1)
            #pygame.draw.rect(screen, RED, (player.x, player.y, player.hitbox["width"], player.hitbox["height"]), 3) 
            #pygame.draw.rect(screen, (0, 100, 255), (player.x, player.y, player.width, player.height), 3)  
            #pygame.draw.rect(screen, (0, 100, 255), (rect1.x, rect1.y,deskWidth, deskHeight), 3) 

            while(player.colisao == True):
                player.block()

            #Checa colisão
            player_rect = pygame.Rect(player.x, player.y, player.hitbox["width"], player.hitbox["height"])
            if player_rect.colliderect(rect1):
                player.colisao = True
            else:
                player.colisao = False
                player.Move()
                
            player.Draw(screen)
            pygame.display.flip()
            FPSCLOCK.tick(30)

class Menu():
    def __init__(self):
        self.active = True
        self.title = Text(None, 60, "Ryder Storm", WHITE, [(WIDTH/2) - 120, (HEIGHT/2) - 100])
        self.sub = Text(None, 31, "Pressione ENTER para jogar", WHITE, [(WIDTH/2) - 150, HEIGHT - 200])
    def run(self):
        while self.active:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        game.run()
                        self.active = False

            screen.fill(BLACK)
            self.title.draw()
            self.sub.drawFade()
            pygame.display.flip()
            FPSCLOCK.tick(30)

if __name__ == "__main__":
    menu = Menu()
    menu.run()