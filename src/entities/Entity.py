import pygame

class Entity():
    def __init__(self, sprite, x, y, speed, width, height, scale):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.scale = scale

    def Draw(self, screen):
        screen.blit(self.sprite,(self.x, self.y))
    
    def isColliding(self, entity2):
        other_rect = pygame.Rect(entity2.x, entity2.y, entity2.width * entity2.scale, entity2.height * entity2.scale)
        x1 = self.x
        y1 = self.y
        my_rect = pygame.Rect(x1, y1, self.width * self.scale, self.height * self.scale)
        if(my_rect.colliderect(other_rect)):
            return True
        x1 = self.x - 1
        y1 = self.y 
        if(my_rect.colliderect(other_rect)):
            return True
        x1 = self.x
        y1 = self.y - 1
        if(my_rect.colliderect(other_rect)):
            return True
        x1 = self.x -1
        y1 = self.y - 1
        if(my_rect.colliderect(other_rect)):
            return True
        return False