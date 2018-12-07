import pygame
import random
from constants import *


class Maze:
    # Define file use to create lvl structure
    def __init__(self, file):
        self.file = file
        self.structure = []

    # Parse file to create structure
    def structure_construction(self):
        with open(self.file, "r") as file:
            # Define total rows
            for row in file:
                row_structure = []
                # Append total number of case per row
                for case in row:
                    if case != "\n":
                        row_structure.append(case)
                # Create a table in two dimensions
                self.structure.append(row_structure)

    def display_lvl(self, window, wall_pic, end_pic, texture_pic):

        # Define where start picture's blit
        wall = pygame.image.load(wall_pic).convert_alpha()
        end = pygame.image.load(end_pic).convert_alpha()
        texture = pygame.image.load(texture_pic).convert_alpha()
        sprite = SPRITE_SIZE
        len_line = NB_SPRITE
        # Define where start picture's blit
        x = 0
        y = 0
        len_line = LEN_LINE

        for row in self.structure:
            for column in row:
                if column == "m":
                    window.blit(wall, [x, y])
                elif column == "a":
                    window.blit(end, [x, y])
                else:
                    window.blit(texture, [x, y])
                x += sprite
                # When the loop arrived at the end of line, reboot x position
                if x >= len_line:  # 15 is the number of sprite in a line of the maze
                    x = 0
                    y += sprite

    def test_next_position(self, next_position):
        if (
            next_position[0] < STRUCTURE_SIZE[0]
            and next_position[1] < STRUCTURE_SIZE[1]
        ):
            if next_position[0] >= 0 and next_position[1] >= 0:
                if self.structure[next_position[1]][next_position[0]] != "m":
                    return True

    def end_game(self, charac):
        if charac.position == [14, 14]:
            return False
        else:
            return True
    
    def response(self, charac, objects):
        print("dans end game ==>", objects.objects_collected)
        if charac.position == [14, 14] and objects.objects_collected == 3:
            print("GAGNÉ")
            return True
        elif charac.position == [14, 14] and objects.objects_collected != 3:
            print("PERDU")
            return False



# class Menu:
#     def __init__()


class Charac:
    def __init__(self, charac_pic, texture_pic, maze, window):
        self.position = [0, 0]
        self.charac = pygame.image.load(charac_pic).convert_alpha()
        self.texture = pygame.image.load(texture_pic).convert_alpha()
        self.maze = maze
        self.window = window

    def blit(self, past_position):
        # Determine pixel position for blit picture
        x_pix = self.position[0] * SPRITE_SIZE
        y_pix = self.position[1] * SPRITE_SIZE
        past_position = [i * SPRITE_SIZE for i in past_position]

        self.window.blit(self.texture, past_position)
        self.window.blit(self.charac, [x_pix, y_pix])
        pygame.display.update()

    def move(self, direction):
        self.x = self.position[0]
        self.y = self.position[1]
        maze = self.maze

        if direction == "right":
            next_position = [self.x + 1, self.y]
            if maze.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace blit by texture
                self.position = (
                    next_position
                )  # Determine new position to blit charac_pic
                self.blit(past_position)

        elif direction == "left":
            next_position = [self.x - 1, self.y]
            if maze.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace blit by texture
                self.position = (
                    next_position
                )  # Determine new position to blit charac_pic
                self.blit(past_position)

        elif direction == "up":
            next_position = [self.x, self.y - 1]
            if maze.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace blit by texture
                self.position = (
                    next_position
                )  # Determine new position to blit charac_pic
                self.blit(past_position)

        elif direction == "down":
            next_position = [self.x, self.y + 1]
            if maze.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace blit by texture
                self.position = (
                    next_position
                )  # Determine new position to blit charac_pic
                self.blit(past_position)


class Object:
    def __init__(self, syringe_pic, ether_pic, needle_pic, maze, window):
        self.syringe = pygame.image.load(syringe_pic).convert_alpha()
        self.ether = pygame.image.load(ether_pic).convert_alpha()
        self.needle = pygame.image.load(needle_pic).convert_alpha()
        self.i = 0
        self.j = 0
        self.k = 0
        self.objects_collected = 0
        self.maze = maze
        self.window = window

    def generate_random_position(self):
        searching = True
        self.x = 0
        self.y = 0
        self.inventory = {"ether": (), "syringe": (), "needle": ()}

        while searching:
            self.position = []
            self.x = random.randrange(0, 14, 1)
            self.y = random.randrange(0, 14, 1)

            print("X ===> ", self.x)
            print("Y ===> ", self.y)
            print("carac ===> ", self.maze.structure[self.x][self.y])

            if self.maze.structure[self.y][self.x] == "0":
                self.position.extend([self.x, self.y])
                searching = False
        print("random position ===>", self.position)
        return self.position

    def display_object(self):
        self.ether_position = []
        self.syringe_position = []
        self.needle_position = []

        while (
            self.ether_position == self.syringe_position
            or self.ether_position == self.needle_position
            or self.syringe_position == self.needle_position
        ):
            self.ether_position = self.generate_random_position()
            self.syringe_position = self.generate_random_position()
            self.needle_position = self.generate_random_position()

            print("ether position in method display_object ==> ", self.ether_position)
            print(
                "syringe position in method display_object ==> ", self.syringe_position
            )
            print("needle position in method display_object ==> ", self.needle_position)

            self.ether_position_pix = [i * SPRITE_SIZE for i in self.ether_position]
            self.syringe_position_pix = [i * SPRITE_SIZE for i in self.syringe_position]
            self.needle_position_pix = [i * SPRITE_SIZE for i in self.needle_position]

            self.window.blit(self.ether, self.ether_position_pix)
            self.window.blit(self.syringe, self.syringe_position_pix)
            self.window.blit(self.needle, self.needle_position_pix)

    def collecting_objects(self, charac):
        # Count number of objects collected
        if charac.position == self.ether_position:
            self.i = 1
        elif charac.position == self.syringe_position:
            self.j = 1
        elif charac.position == self.needle_position:
            self.k = 1

        self.objects_collected = self.i + self.j + self.k
        self.display_object_collected(self.objects_collected, ONE, TWO, THREE, WALL)

        print(self.objects_collected)
        return self.objects_collected

    def display_object_collected(
        self, objects_collected, one_pic, two_pic, three_pic, wall_pic
    ):
        one = pygame.image.load(one_pic).convert_alpha()
        two = pygame.image.load(two_pic).convert_alpha()
        three = pygame.image.load(three_pic).convert_alpha()
        wall = pygame.image.load(wall_pic).convert_alpha()
        position_objects_pix = [i * SPRITE_SIZE for i in [14, 0]]
        window = self.window

        if objects_collected == 1:
            window.blit(one, position_objects_pix)
        elif objects_collected == 2:
            window.blit(wall, position_objects_pix)
            window.blit(two, position_objects_pix)
        elif objects_collected == 3:
            window.blit(wall, position_objects_pix)
            window.blit(three, position_objects_pix)

# class Menu:
#     def __init__(self, menu_pic, window):
#         self.menu = pygame.image.load(menu_pic).convert_alpha()
#         self.window = window
#         self.window.blit(self.menu, ((0, 0)))

class Play:
    def __init__(self, window):
        self.window = window

    def init(self):
        self.maze = Maze(MAZE_STRUCTURE)
        self.mac_gyver = Charac(MAC_GYVER, TEXTURE, self.maze, self.window)
        self.mac_gyver.position = [0, 0]
        self.objects = Object(SYRINGE, ETHER, NEEDLE, self.maze, self.window)

        # INIT MAZE
        self.maze.structure_construction()
        self.maze.display_lvl(self.window, WALL, END, TEXTURE)

        # INIT CHARAC
        self.mac_gyver.blit(self.mac_gyver.position)

        # INIT OBJECTS
        self.objects.generate_random_position()
        self.objects.display_object()
        self.objects.objects_collected = 0

        #RUN PROGRAM
        self.run = True

    def menu(self, menu_pic):
        self.menu = pygame.image.load(menu_pic).convert_alpha()
        self.window.blit(self.menu, ((0, 0)))

        continuer = True
        while continuer:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continuer = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        continuer = False 
            
    def play(self):
        continuer = True
        while continuer:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continuer = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.mac_gyver.move("right")
                    elif event.key == pygame.K_LEFT:
                        self.mac_gyver.move("left")
                    elif event.key == pygame.K_UP:
                        self.mac_gyver.move("up")
                    elif event.key == pygame.K_DOWN:
                        self.mac_gyver.move("down")
                    self.objects.collecting_objects(self.mac_gyver)
                    continuer = self.maze.end_game(self.mac_gyver)
                    self.response = self.maze.response(self.mac_gyver, self.objects)
                    print('response ==>', self.response)
                    print(self.mac_gyver.position)
            pygame.display.flip()
        return self.response
        

    def end_game1(self, end_game1_pic):
        self.end_game1_pic = pygame.image.load(end_game1_pic).convert_alpha()
        self.window.blit(self.end_game1_pic, ((0, 0)))

        continuer = True
        while continuer:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continuer = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        continuer = False 
                        return True
    
    def end_game2(self, end_game2_pic):
        self.end_game2_pic = pygame.image.load(end_game2_pic).convert_alpha()
        self.window.blit(self.end_game2_pic, ((0, 0)))

        continuer = True
        while continuer:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continuer = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        continuer = False 
                        return True
