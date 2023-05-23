import pygame
from src.text import Text
from src.settings import *

class UI():
    def __init__(self):
        self.screen = pygame.display.get_surface()

    def run(self, seconds, playerLife):
        text_timer = Text(None, 30, "Timer:", WHITE, [30, 30])
        text_surface = Text(None, 30, seconds, WHITE, [100, 30])
        player_life_text = Text(None, 30, "Vida:", WHITE, [30, HEIGHT - 50])
        player_life = Text(None, 30, str(playerLife), WHITE, [100, HEIGHT - 50])
        text_timer.draw()
        text_surface.draw()
        player_life_text.draw()
        player_life.draw()