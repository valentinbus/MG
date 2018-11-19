import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((600, 600))

#Chargement et collage du fond
fond = pygame.image.load("./ressource/background.png").convert()
fenetre.blit(fond, (0, 0))

#Chargement et collage de MacGyver
macgyver = pygame.image.load("./ressource/MacGyver.png").convert_alpha() #Taille 32*43
position_macgyver = macgyver.get_rect()
fenetre.blit(macgyver, position_macgyver)

#Rafraîchissement de l'écran
pygame.display.flip()

#Define number of repeat when key stay press
pygame.key.set_repeat(400, 30)

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le macgyver
			    position_macgyver = position_macgyver.move(0,43)

			if event.key == K_UP:	
				#On monte le macgyver
				position_macgyver = position_macgyver.move(0,-43)

			if event.key == K_RIGHT:	
				#On descend le macgyver
				position_macgyver = position_macgyver.move(32,0)

			if event.key == K_LEFT:	#Si "flèche bas"
				#On descend le macgyver
				position_macgyver = position_macgyver.move(-32, 0)

            
	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(macgyver, position_macgyver)
	#Rafraichissement
	pygame.display.flip()
