import pygame
from src.text import Text
from src.settings import *

class Textbox():
    def __init__(self, text):
        self.active = False
        if(text == "level1"):
            message = "level1"
        else:
            message = "level2"
        self.width = WIDTH/3
        self.height = 100
        self.x = (WIDTH/2) - self.width/2
        self.y = 100
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = WHITE
        self.text_position = [(self.x), (self.y)]
        self.render_text = Text(None, 40, message, BLACK, self.text_position)
        self.esc1 = Text(None, 40, "Sim", BLACK, (self.x + 10, self.y + self.height - 40))
        self.esc2 = Text(None, 40, "Não", BLACK, (self.x + self.width - 60, self.y + self.height - 40))
        
    def run(self):
        while self.active:
            self.draw()

    def events(self, event):
        pass
            
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.line(self.screen, GREEN, (self.x, self.y), (self.x + self.width, self.y), 5)
        pygame.draw.line(self.screen, GREEN, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 5)
        pygame.draw.line(self.screen, GREEN, (self.x, self.y), (self.x, self.y + self.height), 5)
        pygame.draw.line(self.screen, GREEN, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 5)
        self.render_text.draw()
        self.esc1.draw()
        self.esc2.draw()