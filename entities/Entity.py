class Entity():
    def __init__(self, img):
        self.img = img

    def Draw(self, screen):
        screen.blit(self.img,(0,0))