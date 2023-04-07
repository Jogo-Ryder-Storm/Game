from entities.Entity import Entity

class Player(Entity):
    def __init__(self, img, velocidade):
        super().__init__(img)
        self.velocidade = velocidade