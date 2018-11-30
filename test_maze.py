import pygame
from constante import *

class Maze:
    #Define file use to create lvl structure
    def __init__(self, file):
        self.file = file
        self.structure = []

    #Parse file to create structure
    def structure_construction(self):
        with open(self.file, 'r') as file:
            #Define total rows
            for row in file:
                row_structure = []
                #Append total number of case per row
                for case in row:
                    if case != '\n':
                        row_structure.append(case)
                #Create a table in two dimensions 
                self.structure.append(row_structure)


    def display_lvl(self, window, wall_pic, end_pic, texture_pic):

        #Define where start picture's blit
        wall = pygame.image.load(wall_pic).convert_alpha()
        end = pygame.image.load(end_pic).convert_alpha()
        texture = pygame.image.load(texture_pic).convert_alpha()
        sprite = SPRITE_SIZE
        len_line = NB_SPRITE
        #Define where start picture's blit
        x=0
        y=0
        len_line = LEN_LINE

        for row in self.structure:
            for column in row:
                if column == 'm':
                    window.blit(wall, [x, y])
                elif column == 'a':
                    window.blit(end, [x, y])
                else :
                    window.blit(texture, [x, y])
                x+=sprite
                #When the loop arrived at the end of line, reboot x position
                if x >= len_line: #15 is the number of sprite in a line of the maze
                    x=0
                    y+=sprite

    def test_next_position(self, next_position):
        if next_position[0] < STRUCTURE_SIZE[0] and next_position[1] < STRUCTURE_SIZE[1]:
            if next_position[0] >= 0 and next_position[1] >= 0:
                #print(self.structure[next_position[1]][next_position[0]])
                if self.structure[next_position[1]][next_position[0]] != 'm':
                    return True

#########
#TESTING#
#########

#INIT
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
maze = Maze(MAZE_STRUCTURE)
maze.structure_construction()
maze.display_lvl(window, WALL, END, TEXTURE)

#TEST
continuer = 1
while continuer:
    pygame.display.update()
    for event in pygame.event.get():	#Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0