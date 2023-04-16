import pygame
from src.entities.Entity import Entity

class Player(Entity):
    life = 3
    directions = ["left", "down", "right", "up"]
    actualDirection = directions[0]
    colisao = False
    walkSpriteFrame = [1, 3] #ESQUERDA DIREITA
    currentFrame = walkSpriteFrame[0]
    up = False
    down = False
    left = False
    right = False
    state = 0
    size = 0
    lastX = 0
    lastY = 0
    hitbox = {"width": 0, "height": 0}
    anim = []
    anim_steps = [9, 4, 9, 4]
    last_update = pygame.time.get_ticks()
    frame_tick = 120
    cur_frame = 0
    def __init__(self, sprite, x, y, speed, width, height):
        super().__init__(sprite, x, y, speed, width, height)
        self.size = width * height
        j = 0
        for animation in self.anim_steps:
            temp_list = []
            i = 0
            for _ in range(animation):
                temp_list.append(sprite.get_image(i, j, self.width, self.height, 2, (255,255,255)))
                i += 1
            j += 1
            self.anim.append(temp_list)
            self.hitbox["width"] = width*1.6
            self.hitbox["height"] = height*1.9

    def Move(self):
        self.lastX = self.x
        self.lastY = self.y
        if(self.up or self.down or self.left or self.right):
            self.state = self.currentFrame
            if(self.up):
                self.y -= self.speed
            elif(self.down):
                self.y += self.speed
            if(self.left):
                self.x -= self.speed
            elif(self.right):
                self.x += self.speed
        else:
            if(self.currentFrame == self.walkSpriteFrame[0]):
                self.state = 0
            else:
                self.state = 2

    def Draw(self, screen):
        cur_time = pygame.time.get_ticks()
        if cur_time - self.last_update >= self.frame_tick:
            self.cur_frame += 1
            self.last_update = cur_time
            if self.cur_frame == len(self.anim[self.state]):
                self.cur_frame = 0
        screen.blit(self.anim[self.state][self.cur_frame], (self.x, self.y))
    
    def block(self):
            self.x = self.lastX
            self.y = self.lastY
            self.colisao = False