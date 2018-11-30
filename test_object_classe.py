import pygame
from constants import *
from classes import Maze, Charac
import random

class Object():
    def __init__(self, syringe_pic, ether_pic, needle_pic, maze, window):
        self.syringe = pygame.image.load(syringe_pic).convert_alpha()
        self.ether = pygame.image.load(ether_pic).convert_alpha()
        self.needle = pygame.image.load(needle_pic).convert_alpha() 
        self.position = []
        
    def generate_random_position(self):
        searching = True
        self.x = 0
        self.y = 0

        while searching:
            self.x = random.randrange(0, 14, 1)
            self.y = random.randrange(0, 14, 1)

            print('X ===> ', self.x)
            print('Y ===> ', self.y)
            print('carac ===> ', maze.structure[self.x][self.y])
            
            if maze.structure[self.x][self.y] == '0' :
                self.position.extend([self.x, self.y])
                searching = False
        print('random position ===>', self.position)

    def display_object(self):
        self.ether_position = self.generate_random_position()
        ether_position_pix = [i*SPRITE_SIZE for i in self.ether_position]
        window.blit(self.ether, ether_position_pix)



#########
#TESTING#
#########

#INIT MAZE
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
maze = Maze(MAZE_STRUCTURE)
maze.structure_construction()
maze.display_lvl(window, WALL, END, TEXTURE)

#INIT CHARAC
mac_gyver = Charac(MAC_GYVER, TEXTURE, maze, window)
mac_gyver.blit(mac_gyver.position)

#INIT OBJECTS 
objects = Object(SYRINGE, ETHER, NEEDLE, maze, window)
objects.generate_random_position()
#objects.display_object()


continuer = 1
while continuer:
    pygame.display.update()
    for event in pygame.event.get():
        #Waiting for events
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mac_gyver.move('right')  
            elif event.key == pygame.K_LEFT:
                mac_gyver.move('left')
            elif event.key == pygame.K_UP:
                mac_gyver.move('up')
            elif event.key == pygame.K_DOWN:
                mac_gyver.move('down')
            print(event.key)
            print(mac_gyver.position)
    pygame.display.flip()