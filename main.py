import pygame
from constants import *
from classes import *

pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
maze = Maze(MAZE_STRUCTURE)
mac_gyver = Charac(MAC_GYVER, TEXTURE, maze, window)
objects = Object(SYRINGE, ETHER, NEEDLE, maze, window)

def init():
    # INIT MAZE
    maze.structure_construction()
    maze.display_lvl(window, WALL, END, TEXTURE)

    # INIT CHARAC
    mac_gyver.blit(mac_gyver.position)

    # INIT OBJECTS

    objects.generate_random_position()
    objects.display_object()

    return maze, mac_gyver, objects

def launch_game():
    init()
    continuer = True
    while continuer:
        pygame.display.update()
        for event in pygame.event.get():
            # Waiting for events
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mac_gyver.move("right")
                elif event.key == pygame.K_LEFT:
                    mac_gyver.move("left")
                elif event.key == pygame.K_UP:
                    mac_gyver.move("up")
                elif event.key == pygame.K_DOWN:
                    mac_gyver.move("down")
                objects.collecting_objects(mac_gyver)
                continuer = maze.end_game(mac_gyver)
                response = maze.response(mac_gyver, objects)
                print(mac_gyver.position)
        pygame.display.flip()
    return response 


def end_game1():
    menu = Menu(MENU, window)

    continuer = True        
    while continuer:
        pygame.display.update()
        for event in pygame.event.get():
            # Waiting for events
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    response = launch_game()

def end_game2():
    menu = Menu(MENU, window)

    continuer = True        
    while continuer:
        pygame.display.update()
        for event in pygame.event.get():
            # Waiting for events
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    response = launch_game()         

def menu():
    menu = Menu(MENU, window)

    continuer = True        
    while continuer:
        pygame.display.update()
        for event in pygame.event.get():
            # Waiting for events
            if event.type == pygame.QUIT:
                continuer = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    response = launch_game()
                    if response == True:
                        end_game1()
                    elif response == False:
                        end_game2()

menu()