import pygame
from pygame.locals import *
from src.settings import *
from src.text import Text

class inputName():
    def __init__(self):
        self.active = True
        self.input_text = ""
        self.size = 0
        self.title = Text(None, 40, "Escreva seu nome: ", WHITE, [(WIDTH/2), (HEIGHT/2) - 250])
        self.alpha = 255
    def run(self):
        screen = pygame.display.get_surface()

        while self.active:
            screen.fill(BLACK)
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                        if(self.size > 0):
                            self.size -= 1
                    elif event.key == K_RETURN:
                        #print(self.input_text)
                        with open ("playerName.txt", "w") as f:
                            f.write(self.input_text)
                        from src.menu import Menu
                        MUSIC.play(-1)
                        menu = Menu()
                        menu.run()
                        self.active = False
                    else:
                        if(self.size <= 15):
                            self.input_text += event.unicode
                            self.size += 1

            self.alpha -= 8
            if self.alpha < 0:
                self.alpha = 255
            line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            text = Text(None, 40, self.input_text, WHITE, [WIDTH/2, HEIGHT/2 - 5])
            text.draw_center()
            self.title.draw_center()
            pygame.draw.line(screen, WHITE, (WIDTH/3, HEIGHT/2 + 20), (WIDTH/3 + WIDTH/3, HEIGHT/2 + 20), 5)
            line_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            line_surface.set_alpha(self.alpha)
            pygame.draw.line(line_surface, (255, 255, 255, self.alpha), (WIDTH/2 + int(self.size*9.1), HEIGHT/2 + 10), (WIDTH/2 + int(self.size*9.1), HEIGHT/2 - 15), 3)
            screen.blit(line_surface, (0, 0))
            pygame.display.flip()
            FPSCLOCK.tick(30)