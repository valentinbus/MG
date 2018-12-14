import pygame
from constants import NB_SPRITE, SPRITE_SIZE, LEN_LINE, WINDOW_SIZE, STRUCTURE_SIZE, MENU, END_GAME1, END_GAME2, ONE, TWO, THREE, START, END, WALL, TEXTURE, BACKGROUND, MAC_GYVER, ETHER, SYRINGE, NEEDLE, MAZE_STRUCTURE
from classes import Charac, Maze, Object, Play

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    play = Play(window)

    play.menu(MENU)
    run = True
    while run:
        play.init() 
        launch = play.play() 
        if launch == True:
            play.end_game1(END_GAME1)
        elif launch == False:
            play.end_game2(END_GAME2)
        run = play.run

if __name__ == "__main__":
    main()