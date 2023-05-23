# Imports
import pygame, sys
from pygame.locals import *


class Timer():
    def __init__(self, x,y):
       self.x = x
       self.y = y
       self.time = 0
       self.font = pygame.font.Font(None, 36)
       self.screen = pygame.display.get_surface()

    def draw(self, seconds):
        self.time = int(seconds)
        text_content = str(self.time)
        # Render the text as an image surface
        text_surface = self.font.render(text_content, True, (255,255,255))
        # Get the rectangular bounds of the text surface
        text_rect = text_surface.get_rect()
        # Center the text on the screen
        text_rect.center = (self.x, self.y)
        # Blit the text surface onto the window
        self.screen.blit(text_surface, text_rect)