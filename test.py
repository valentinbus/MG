import pygame

screen = pygame.display.set_mode([800, 800], 0, 32)
#initiates screen

image1 = pygame.image.load('./ressource/background.png').convert_alpha()
#testimage0.jpg is loaded into the variable image1

image2 = pygame.image.load('./ressource/aiguille.png').convert_alpha()
#testimage.png is loaded into the variable image2

while True:
    screen.fill([0, 0, 0])
    #screen is filled with a black background

    screen.blit(image1, [200, 200]) 
    #here image1 is blitted onto screen at the coordinates (200,200)

    image1.blit(image2, [0, 0])
    #here image2 is blitted onto image1 at the coordinates (0,0) which starts at the upper left of image1

    pygame.display.update()
    #updates display, which you can just ignore