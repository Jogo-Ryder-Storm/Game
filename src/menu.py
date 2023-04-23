# Imports
import pygame, sys
from pygame.locals import *

# Modulos
from src.settings import *
from src.text import Text
from src.game import Game
from src.button import Button

class Menu():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.active = True
        self.state = 1
        self.fullscreen = False
        self.music = True
        self.title = Text(None, 60, "Ryder Storm", WHITE, [(WIDTH/2) - 125, (HEIGHT/2) - 250])
        self.sub = Text(None, 31, "Pressione ENTER para jogar", WHITE, [(WIDTH/2) - 140, HEIGHT - 200])
        self.btn_play = Button("white", (WIDTH/2) - 125, 480, "Jogar", self.next_scene)
        self.btn_options = Button("white", (WIDTH/2) - 125, 560, "Opções", self.scene_options)
        self.btn_quit = Button("white", (WIDTH/2) - 125, 640, "Sair", self.quit_game)
        self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela cheia", self.screen_change)
        self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Mutar", self.mute)
        self.btn_back = Button("white", (WIDTH/2) - 125, 640, "Voltar", self.back)

    def mute(self):
        if(self.music):
            MUSIC.stop()
            self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Desmutar", self.mute)
            self.music = False
        else:
            MUSIC.play(-1)
            self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Mutar", self.mute)
            self.music = True

    def back(self):
        if(self.state >= 3):
            self.state -= 1 

    def screen_change(self):
        if(self.fullscreen == False):
            self.fullscreen = True
            self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela normal", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.fullscreen = False
            self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela cheia", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    def scene_options(self):
        self.state = 3

    def next_scene(self):
        game = Game()
        game.run()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.active:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if self.state == 1:
                        if event.key == pygame.K_RETURN:
                            self.state = 2
                if self.state == 2:
                    self.btn_play.events(event)
                    self.btn_options.events(event)
                    self.btn_quit.events(event)
                elif self.state == 3:
                    self.btn_screen.events(event)
                    self.btn_back.events(event)
                    self.btn_mute.events(event)

            self.screen.fill(BLACK)
            self.title.draw()
            if self.state == 1:
                self.sub.drawFade()
            elif self.state == 2:
                self.btn_play.draw() 
                self.btn_play.draw()         
                self.btn_options.draw()         
                self.btn_quit.draw()
            elif self.state == 3:
                self.btn_screen.draw()
                self.btn_mute.draw()
                self.btn_back.draw()
            pygame.display.flip()
            FPSCLOCK.tick(30)