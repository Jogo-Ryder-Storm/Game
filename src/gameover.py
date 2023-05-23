# Imports
import pygame, sys
from pygame.locals import *

# Modulos
from src.settings import *
from src.text import Text
from src.button import Button

class Gameover():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.active = True
        self.title = Text(None, 60, "GAMEOVER", WHITE, [(WIDTH/2) - 125, (HEIGHT/2) - 150])
        self.btn_menu = Button("white", (WIDTH/2) - 125, 480, "Menu", self.next_scene)
        self.btn_quit = Button("white", (WIDTH/2) - 125, 560, "Sair", self.quit_game)

    def next_scene(self):
        from src.menu import Menu
        menu = Menu()
        menu.run()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.active:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.quit_game()

                self.btn_menu.events(event)
                self.btn_quit.events(event)

            self.screen.fill(BLACK)
            self.title.drawFade()
            self.btn_menu.draw()
            self.btn_quit.draw()

            pygame.display.flip()
            FPSCLOCK.tick(30)