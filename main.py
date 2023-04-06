import pygame
import random

# Initialize the game engine
pygame.init()
FPSCLOCK = pygame.time.Clock()
 
# Define the colors we will use in RGB format
BLACK = (  0,  0,  0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
# Set the height and width of the screen
height = 800
width = 600
size = [height, width]
screen = pygame.display.set_mode(size)

screen.fill(WHITE)
while True:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit()

    pygame.display.flip()
    FPSCLOCK.tick(30)

