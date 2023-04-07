import pygame

class SpriteSheet():
    def __init__(self, img):
        self.sheet = img
    
    def get_image(self, x, y, width, height, scale, color):
        img = pygame.Surface((width, height)).convert_alpha()
        img.blit(self.sheet, (0, 0), ((x * width), (y * height), width, height))
        img = pygame.transform.scale(img, (width * scale, height * scale))
        img.set_colorkey(color)

        return img