# Imports
import pygame, sys
from pygame.locals import *

# Modulos
from src.settings import *
from src.text import Text
from src.button import Button

def dividir_string(string, largura_maxima):
        palavras = string.split()
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            if len(linha_atual) + len(palavra) + 1 <= largura_maxima:
                linha_atual += " " + palavra if linha_atual else palavra
            else:
                linhas.append(linha_atual)
                linha_atual = palavra
        
        if linha_atual:
            linhas.append(linha_atual)
        return linhas

class Menu():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.active = True
        self.state = 1
        self.fullscreen = False
        self.music = True
        self.title = Text(None, 60, "Ryder Storm", WHITE, [(WIDTH/2) - 125, (HEIGHT/2) - 250])
        self.sub = Text(None, 31, "Pressione ENTER para jogar", WHITE, [(WIDTH/2) - 140, HEIGHT - 200])
        self.btn_play = Button("white", (WIDTH/2) - 125, 400, "Jogar", self.next_scene)
        self.btn_options = Button("white", (WIDTH/2) - 125, 480, "Opções", self.scene_options)
        self.btn_comandos = Button("white", (WIDTH/2) - 125, 560, "Sobre", self.comandos)
        self.btn_quit = Button("white", (WIDTH/2) - 125, 640, "Sair", self.quit_game)
        self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela cheia: OFF", self.screen_change)
        self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Musica: ON", self.mute)
        self.btn_back = Button("white", (WIDTH/2) - 125, 640, "Voltar", self.back)

    def mute(self):
        if(self.music):
            MUSIC.stop()
            self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Musica: OFF", self.mute)
            self.music = False
        else:
            MUSIC.play(-1)
            self.btn_mute = Button("white", (WIDTH/2) - 125, 560, "Musica: ON", self.mute)
            self.music = True

    def back(self):
        self.state = 2

    def screen_change(self):
        if(self.fullscreen == False):
            self.fullscreen = True
            self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela cheia: ON", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.fullscreen = False
            self.btn_screen = Button("white", (WIDTH/2) - 125, 480, "Tela cheia: OFF", self.screen_change)
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    def scene_options(self):
        self.state = 3
    
    def comandos(self):
        self.state = 4

    def next_scene(self):
        from src.game import Game
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
                    self.btn_comandos.events(event)
                    self.btn_quit.events(event)
                elif self.state == 3:
                    self.btn_screen.events(event)
                    self.btn_back.events(event)
                    self.btn_mute.events(event)
                elif self.state == 4:
                    self.btn_back.events(event)

            self.screen.fill(BLACK)
            self.title.draw()
            if self.state == 1:
                self.sub.drawFade()
            elif self.state == 2:
                self.btn_play.draw() 
                self.btn_comandos.draw()         
                self.btn_options.draw()         
                self.btn_quit.draw()
            elif self.state == 3:
                self.btn_screen.draw()
                self.btn_mute.draw()
                self.btn_back.draw()
            elif self.state == 4:
                bx = WIDTH/5
                by = HEIGHT/3
                bwd = WIDTH/2 + 150
                bht = HEIGHT/2
                pygame.draw.rect(self.screen, WHITE, pygame.Rect(bx, by, bwd, bht))
                titulo = "Comandos:"
                sobre = "Sobre:"
                texto = "Para movimentar o jogador precione os direcionais (setas) do teclado."
                texto2 = "Para interragir com objetos pressione a tecla 'G' proximo a um objeto."
                desc = "Ryder Storm é um jogo onde o jogador precissa realizar escolhas ao se encontrar em um desastre natural. O jogador ganha pontos baseado em seu tempo e resposta."
                tx = Text(None, 40, titulo, BLACK, (bx + bwd/2 - 80, by + 15))
                tx.draw()
                tx = Text(None, 30, texto, BLACK, (bx + 10, by + 80))
                tx.draw()
                tx = Text(None, 30, texto2, BLACK, (bx + 10, by + 110))
                tx.draw()
                tx = Text(None, 40, sobre, BLACK, (bx + bwd/2 - 50, by + 140))
                tx.draw()
                lines = dividir_string(desc, bwd/12 - 1)
                for i, line in enumerate(lines):
                    tx = Text(None, 35, line, BLACK, (bx + 10, by + 200 + i * 25))
                    tx.draw()
                self.btn_back.draw()
            pygame.display.flip()
            FPSCLOCK.tick(30)