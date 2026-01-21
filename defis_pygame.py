import pygame, sys
from pygame.locals import QUIT
import time

def dessiner():
    fenetre.fill("#D15D15")
    pygame.draw.rect(fenetre, "grey", (50,10, 200, 250))
    pygame.draw.circle(fenetre, "black", (200, 60), 40)
    pygame.draw.circle(fenetre, "black", (100, 60), 40)
    pygame.draw.line(fenetre, "red", (150, 120), (150, 150), 4)
    pygame.draw.ellipse(fenetre, "#7C15D1", (60, 170, 180, 80))
    #tick est appellé à chaque maj de l'affichage
    pygame.display.update()

pygame.init()
fenetre = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Robot!')
horloge = pygame.time.Clock()

while True:
    #permet de mettre à jour l'horloge relative au jeu
    #= le nombre d'images par secondes
    horloge.tick(60)
    temps = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    dessiner()
    #print("Afficher la durée d'éxecution du jeu ", time.time() - temps)
