import pygame

from classes import Charac, Maze, Object, Play
from constants import (BACKGROUND, END, END_GAME1, END_GAME2, ETHER, LEN_LINE,
                       MAC_GYVER, MAZE_STRUCTURE, MENU, NB_SPRITE, NEEDLE, ONE,
                       SPRITE_SIZE, START, STRUCTURE_SIZE, SYRINGE, TEXTURE,
                       THREE, TWO, WALL, WINDOW_SIZE)


def main():
    '''Run game'''
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    play = Play(window)

    play.menu(MENU)
    run = True
    while run:
        play.init()
        launch = play.play()
        if launch:
            play.end_game1(END_GAME1)
        else:
            play.end_game2(END_GAME2)
        run = play.run


if __name__ == "__main__":
    main()
