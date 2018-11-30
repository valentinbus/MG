import pygame
import test_maze
from constante import *

class Charac:
    def __init__(self, charac_pic, texture_pic, maze, window):
        self.position = [0, 0]
        self.charac = pygame.image.load(charac_pic).convert_alpha()
        self.texture = pygame.image.load(texture_pic).convert_alpha()
        self.maze = maze 

    def blit(self, past_position):
        #Determine pixel position for blit picture
        x_pix = self.position[0]*SPRITE_SIZE
        y_pix = self.position[1]*SPRITE_SIZE
        past_position = [i*SPRITE_SIZE for i in past_position]

        window.blit(self.texture, past_position)
        window.blit(self.charac, [x_pix, y_pix])
        pygame.display.update()

    def move(self, direction):
        self.x = self.position[0]
        self.y = self.position[1]

        if direction == 'right':
            next_position = [self.x + 1, self.y]
            if maze.test_next_position(next_position) == True:
                past_position = self.position #Determine previous position to replace blit by texture
                self.position = next_position #Determine new position to blit charac_pic
                self.blit(past_position)
        
        elif direction == 'left':
            next_position = [self.x - 1, self.y]
            if maze.test_next_position(next_position) == True:
                past_position = self.position #Determine previous position to replace blit by texture
                self.position = next_position #Determine new position to blit charac_pic
                self.blit(past_position)        

        elif direction == 'up':
            next_position = [self.x, self.y - 1]
            if maze.test_next_position(next_position) == True:
                past_position = self.position #Determine previous position to replace blit by texture
                self.position = next_position #Determine new position to blit charac_pic
                self.blit(past_position)

        elif direction == 'down':
            next_position = [self.x, self.y + 1]
            if maze.test_next_position(next_position) == True:
                past_position = self.position #Determine previous position to replace blit by texture
                self.position = next_position #Determine new position to blit charac_pic
                self.blit(past_position)

#########
#TESTING#
#########

#INIT MAZE
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
maze = test_maze.Maze(MAZE_STRUCTURE)
maze.structure_construction()
maze.display_lvl(window, WALL, END, TEXTURE)

#INIT CHARAC
mac_gyver = Charac(MAC_GYVER, TEXTURE, maze, window)
mac_gyver.blit(mac_gyver.position)


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
