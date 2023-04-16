import pygame

class Text:
    def __init__(self, font, size, text, color, pos):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color).convert_alpha()
        self.position = pos
        self.text_alpha = 255
        self.alpha_speed = 7
    
    def draw(self):
        self.screen.blit(self.text, self.position)
    
    def drawFade(self):
        if(self.text_alpha > 0):
            self.text_alpha -= self.alpha_speed
        else:
            self.text_alpha = 255
        self.text.set_alpha(self.text_alpha)
        self.screen.blit(self.text, self.position)