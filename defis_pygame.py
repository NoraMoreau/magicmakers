import pygame, sys
from pygame.locals import QUIT
import time

def dessiner():
    fenetre.fill("#D15D15")
    #visage
    pygame.draw.rect(fenetre, "grey", (50, 10, 200, 250))
    #yeux
    pygame.draw.circle(fenetre, "black", (100, 60), 40)
    pygame.draw.circle(fenetre, "white", (100, 60), 15)
    pygame.draw.circle(fenetre, "black", (200, 60), 40)
    pygame.draw.circle(fenetre, "white", (180, 55), 10)
    #bouche
    pygame.draw.ellipse(fenetre, "red", (60, 130, 180, 80), 4)
    pygame.draw.rect(fenetre, "grey", (60, 130, 180, 40))
    #nez
    pygame.draw.line(fenetre, "black", (130, 120), (170, 120), 4)
    pygame.draw.line(fenetre, "black", (130, 120), (150, 150), 4)
    pygame.draw.line(fenetre, "black", (170, 120), (150, 150), 4)
    #noeud
    pygame.draw.circle(fenetre, "#CD7292", (240, 20), 10)
    pygame.draw.line(fenetre, "#CD7292", (210, 0), (240, 15), 4)
    pygame.draw.line(fenetre, "#CD7292", (200, 20), (240, 15), 4)
    pygame.draw.line(fenetre, "#CD7292", (210, 0), (200, 20), 4)
    pygame.draw.line(fenetre, "#CD7292", (250, 17), (280, 15), 4)
    pygame.draw.line(fenetre, "#CD7292", (250, 17), (275, 40), 4)
    pygame.draw.line(fenetre, "#CD7292", (280, 15), (275, 40), 4)
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
