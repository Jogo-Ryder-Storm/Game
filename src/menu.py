# Imports
import pygame
from pygame.locals import *

# Modulos
from src.settings import *
from src.text import Text
from src.game import Game

class Menu():
    def __init__(self):
        self.active = True
        self.title = Text(None, 60, "Ryder Storm", WHITE, [(WIDTH/2) - 120, (HEIGHT/2) - 100])
        self.sub = Text(None, 31, "Pressione ENTER para jogar", WHITE, [(WIDTH/2) - 150, HEIGHT - 200])
    def run(self):
        screen = pygame.display.get_surface()
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