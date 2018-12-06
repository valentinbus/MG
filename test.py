import pygame
from constants import *

class Menu:
    def __init__():
        return

pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

continuer = True

while continuer:
    pygame.display.update()
    for event in pygame.event.get():
    # Waiting for events
        if event.type == pygame.QUIT:
            continuer = False

print(WINDOW_SIZE)