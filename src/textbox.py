import pygame
from src.text import Text
from src.settings import *

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

class Textbox():
    def __init__(self, text):
        self.active = False
        self.screen = pygame.display.get_surface()
        self.width = WIDTH/2
        self.height = HEIGHT/3
        self.x = (WIDTH/2) - self.width/2
        self.y = 100
        self.arrow = pygame.image.load("res/arrow.png")
        self.arrow = pygame.transform.scale(self.arrow, (18, 20))
        self.esc = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = WHITE
        if(text == "level1"):
            self.message = "level1"
            self.options = ["Sim1", "Não1", "talvez"]
        else:
            self.message = "level22 2222222 2222222 22222222 222222 2222 a Testeaa aaaaa aaaaaa aaaaa aaaaaaaaa aaaaa"
            self.options = ["Sim2", "Não2", "talvez"]
        
    def run(self):
        while self.active:                    
            self.draw()

    def change_esc(self):
        if self.esc < 0:
            self.esc = len(self.options) - 1
        elif self.esc >= len(self.options):
            self.esc = 0 

    def events(self, event):
        pass
            
    def draw(self):
        line_color = RED
        line_width = 5
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.line(self.screen, line_color, (self.x, self.y), (self.x + self.width, self.y), line_width)
        pygame.draw.line(self.screen, line_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), line_width)
        pygame.draw.line(self.screen, line_color, (self.x, self.y), (self.x, self.y + self.height), line_width)
        pygame.draw.line(self.screen, line_color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), line_width)
        lines = dividir_string(self.message, self.width/12 - 8)
        for i, line in enumerate(lines):
            tx = Text(None, 40, line, BLACK, (self.x + 10, self.y + 15 + i * 25))
            tx.draw()
        for i, option in enumerate(self.options):
            tx = Text(None, 35, option, BLACK, (self.x + 20 + (i/(len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))
            tx.draw()
        self.screen.blit(self.arrow, (self.x + 5 + (self.esc / (len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))

