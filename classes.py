import pygame

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


    def display_lvl(self, window):
        wall = pygame.image.load('./ressource/structures.png').convert_alpha()
        start = pygame.image.load('./ressource/personnages.png')
        end = pygame.image.load('./ressource/Gardien.png').convert_alpha()

        #Define where start picture's blit
        sprite = wall.get_size()[0]
        x=0
        y=0
        len_line = 15*32 
        for row in self.structure:
            for column in row:
                if column == 'm':
                    window.blit(wall, [x, y])
                elif column == 'a':
                    window.blit(end, [x, y])
                x+=sprite

                #When the loop arrived at the end of line, reboot x position
                if x >= len_line: #15 is the number of sprite in a line of the maze
                    x=0
                    y+=sprite

            
class Character:
    #Character initialisation
    def __init__(self, file, maze):
        self.file = file
        self.position = [0, 0]

    def init_in_maze(self, window):
        self.charac = pygame.image.load(self.file).convert_alpha()
        window.blit(self.charac, self.position)

    def move(self, move):
        '''if move == 'up':
            #Define the position of charac
            self.position = [0, self.position[1]+1]
            
            #print(maze.structure[self.position[1]][self.position[0]])
            if maze.structure[self.position[1]][self.position[0]] != 'm':
                window.blit(self.charac, [self.position[0]*32], self.position[1]*32)
            else:
                self.position = [0, self.position[1]-1]
            print(self.position)
        elif move == 'down':
            self.position = [0, self.position[1]-1]

            if maze.structure[self.position[1]][self.position[0]] != 'm':
                window.blit(self.charac, [self.position[0]*32], self.position[1]*32)
            else:
                self.position = [0, self.position[1]+1]
            print(self.position)'''
        if move == 'down':
            self.position = [self.position[0], self.position[1]+1]
            print(self.position)
            window.blit(self.charac, [self.position[0]*32, self.position[1]*32])

        '''elif move == 'up':
            self.position = [self.position[0], self.position[1]-1]
            print(self.position)
            window.blit(self.charac, [self.position[0]*32, self.position[1]*32])'''




#### Zone de debug ###

#Initialisation of the maze
pygame.init()

maze = Maze('./ressource/maze_structure')
maze.structure_construction()
window = pygame.display.set_mode((15*32, 15*32))
background = pygame.image.load('./ressource/background.jpeg')
window.blit(background, [0, 0])
maze.display_lvl(window)

#Initialisation charac personnage:
mc_gyver = Character('./ressource/mc_gyver.png', maze)
mc_gyver.init_in_maze(window)

#Starting Game Loop
continuer = 1
while continuer:
    pygame.display.update()
    for event in pygame.event.get():	#Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0
        elif event.type == pygame.KEYUP:
            mc_gyver.move('up')
        elif event.type == pygame.KEYDOWN:
            mc_gyver.move('down')
    pygame.display.flip()