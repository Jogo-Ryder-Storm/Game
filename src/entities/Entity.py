class Entity():
    def __init__(self, sprite, x, y, speed, width, height):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def Draw(self, screen):
        screen.blit(self.sprite,(self.x, self.y))