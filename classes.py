import pygame
import random
from constants import *

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

class Object():
    def __init__(self, syringe_pic, ether_pic, needle_pic, maze, window):
        self.syringe = pygame.image.load(syringe_pic).convert_alpha()
        self.ether = pygame.image.load(ether_pic).convert_alpha()
        self.needle = pygame.image.load(needle_pic).convert_alpha() 
        
    def generate_random_position(self):
        searching = True
        self.x = 0
        self.y = 0

        while searching:
            self.position = []
            self.x = random.randrange(0, 14, 1)
            self.y = random.randrange(0, 14, 1)

            print('X ===> ', self.x)
            print('Y ===> ', self.y)
            print('carac ===> ', maze.structure[self.x][self.y])
            
            if maze.structure[self.y][self.x] == '0' :
                self.position.extend([self.x, self.y])
                searching = False
        print('random position ===>', self.position)
        return self.position

    def display_object(self):
        self.ether_position = []
        self.syringe_position = []
        self.needle_position = []

        while self.ether_position == self.syringe_position or self.ether_position == self.needle_position \
        or self.syringe_position == self.needle_position:
            self.ether_position = self.generate_random_position()
            self.syringe_position = self.generate_random_position()
            self.needle_position = self.generate_random_position()

            print('ether position in method display_object ==> ', self.ether_position)
            print('syringe position in method display_object ==> ', self.syringe_position)
            print('needle position in method display_object ==> ', self.needle_position)

            self.ether_position_pix = [i*SPRITE_SIZE for i in self.ether_position]
            self.syringe_position_pix = [i*SPRITE_SIZE for i in self.syringe_position]
            self.needle_position_pix = [i*SPRITE_SIZE for i in self.needle_position]

            window.blit(self.ether, self.ether_position_pix)
            window.blit(self.syringe, self.syringe_position_pix)
            window.blit(self.needle, self.needle_position_pix)



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
objects.display_object()

continuer = True
while continuer:
    pygame.display.update()
    for event in pygame.event.get():
        #Waiting for events
        if event.type == pygame.QUIT:
            continuer = False
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