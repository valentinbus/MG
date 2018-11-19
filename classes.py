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
        end = pygame.image.load('./ressource/Gardien.png').convert_alpha()
        #Define where start picture's blit
        x=0
        y=0
        #window_size = window.
        for row in self.structure:
            for column in row:
                if column == 'm':
                    window.blit(wall, [x, y])
                x+=32
                #if x >= 600:
                if x >= window.get_size()[0]:
                    x=0
                    y+=32
            


#### Zone de debug ###

pygame.init()
window = pygame.display.set_mode((600, 600))

maze = Maze('./ressource/maze_structure')
maze.structure_construction()
maze.display_lvl(window)

#BOUCLE INFINIE
continuer = 1
while continuer:
    pygame.display.update()
    for event in pygame.event.get():	#Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0