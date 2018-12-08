import pygame
from constants import *
from classes import Charac, Maze, Object, Play

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    play = Play(window)

    menu = play.menu(MENU)
    continu = True
    run = True
    while run:
        play.init() 
        launch = play.play() 
        if launch == True:
            play.end_game1(END_GAME1)
        elif launch == False:
            play.end_game2(END_GAME2)
        else : 
            continu = False
        run = play.run

if __name__ == "__main__":
    main()