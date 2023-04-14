import pygame
from entities.Entity import Entity

class Player(Entity):
    life = 3
    direcoes = ["left", "down", "right", "up"]
    colisao = False
    direcao = direcoes[0]
    directions = [1, 3] #ESQUERDA DIREITA
    direction = directions[0]
    up = False
    down = False
    left = False
    right = False
    state = 0
    size = 0
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
            
    
    def Move(self):
        if(self.up or self.down or self.left or self.right):
            self.state = self.direction
            if(self.up):
                self.y -= self.speed
            elif(self.down):
                self.y += self.speed
            elif(self.left):
                self.x -= self.speed
            elif(self.right):
                self.x += self.speed
        else:
            if(self.direction == self.directions[0]):
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
            if(self.direcao == self.direcoes[3]):
                self.y += self.speed*2
            elif(self.direcao == self.direcoes[1]):
                self.y -= self.speed*2
            elif(self.direcao == self.direcoes[0]):
                self.x += self.speed*2
            elif(self.direcao == self.direcoes[2]):
                self.x -= self.speed*2
            self.colisao = False