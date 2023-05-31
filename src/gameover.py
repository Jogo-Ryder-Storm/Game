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
        self.title = Text(None, 60, "GAMEOVER", WHITE, [(WIDTH/2) - 125, (HEIGHT/2) - 270])
        self.btn_menu = Button("white", (WIDTH/2) - 250, HEIGHT - 100, "Menu", self.next_scene)
        self.btn_quit = Button("white", (WIDTH/2) + 50, HEIGHT - 100, "Sair", self.quit_game)
        self.btn_next = Button("white", (WIDTH/2) + 100, HEIGHT - 250, "->", self.next_page)
        self.btn_back = Button("white", (WIDTH/2) - 380, HEIGHT - 250, "<-", self.back_page)
        self.allscores = ""
        self.page = 0
        self.maxppage = 7
        with open('ranking.txt') as f:
            contents = f.read()
            self.allscores = contents.split("\n")
    def next_scene(self):
        from src.menu import Menu
        menu = Menu()
        menu.run()
        self.active = False

    def next_page(self):
        if(self.maxppage * (self.page+1) < len(self.allscores)):
            self.page += 1
            print(self.page)
            print(self.maxppage * (self.page+1))
            print(len(self.allscores))

    def back_page(self):
        if(self.page >= 1):
            self.page -= 1

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while self.active:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.quit_game()

                self.btn_next.events(event)
                self.btn_back.events(event)
                self.btn_menu.events(event)
                self.btn_quit.events(event)

            self.screen.fill(BLACK)
            self.title.drawFade()
            bx = WIDTH/5
            by = HEIGHT/4
            bwd = WIDTH/2 + 100
            bht = HEIGHT/2
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(bx, by, bwd, bht))
            titulo = "Score:"
            tx = Text(None, 40, titulo, BLACK, (bx + bwd/2, by + 20))
            tx.draw_center()
            strout = "Voce ficou em {} Lugar !!!".format("X")
            tx = Text(None, 35, strout, BLACK, (bx + bx/2 + 100, by + 45))
            tx.draw()
            for i in range(self.maxppage):
                try:
                    text = self.allscores[i+self.maxppage*self.page].split(";")
                    strout = "{}° {} | Tempo: {}s | Vida: {}".format(i+self.maxppage*self.page + 1, text[0], text[1], text[2])
                    tx = Text(None, 30, strout, BLACK, (bx + bwd/2, by + 100 + 25*i))
                    tx.draw_center()
                except:
                    break

            self.btn_back.draw()
            self.btn_next.draw()
            self.btn_menu.draw()
            self.btn_quit.draw()

            pygame.display.flip()
            FPSCLOCK.tick(30)