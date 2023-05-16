import pygame

class Entity():
    def __init__(self, sprite, x, y, speed, width, height, scale, textbox):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.scale = scale
        self.textbox = textbox
        self.hitbox = {"x":self.x, "y": self.y, "width":self.width, "height":self.height}

    def Draw(self, screen):
        screen.blit(self.sprite,(self.x, self.y))
        pygame.draw.rect(screen, (255,255,0), (self.hitbox["x"], self.hitbox["y"], self.hitbox["width"], self.hitbox["height"]),4)

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
    
    def checkHitBox(self, posx, posy):
        if self.hitbox["x"] <= posx <= self.hitbox["x"] + self.hitbox["width"] and self.hitbox["y"] <= posy <= self.hitbox["y"] + self.hitbox["height"]:
            return True
        else:
            print("fora do retangulo")