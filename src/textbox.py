import pygame
from src.text import Text
from src.settings import *

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
            self.message = "level2"
            self.options = ["Sim2", "Não2", "talvez"]
        self.text_position = [(self.x), (self.y)]
        self.render_text = Text(None, 40, self.message, BLACK, self.text_position)
        
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
        self.render_text.draw()
        for i, option in enumerate(self.options):
            tx = Text(None, 35, option, BLACK, (self.x + 20 + (i/(len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))
            tx.draw()
        self.screen.blit(self.arrow, (self.x + 5 + (self.esc / (len(self.options) - 1))*(self.width - 100), self.y + self.height - 40))