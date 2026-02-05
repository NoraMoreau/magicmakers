import pygame, sys
from pygame.locals import QUIT
import random
import os

pygame.init()
pygame.mixer.init()

largeur, hauteur = 800, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('NOKIA 3210')

# Définition des couleurs
# (la fenêtre, le serpent)
bleu = "#3B60CD"
orange = "#F9F8F7"

# Dimensions des cellules et nombre de cellules
cellule = 20
nb_cellule_x = largeur // cellule
nb_cellule_y = hauteur // cellule

# Horloge pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

# Définir les déplacements
haut = (0, -1)
bas = (0, 1)
gauche = (-1, 0)
droite = (1, 0)

# Chargemet des sons
son_jeu = pygame.mixer.Sound(os.path.join('0097.wav'))
mange_pion = pygame.mixer.Sound(os.path.join('2580.wav'))

# Méthode pour déplacer le serpent en début de jeu
def depart_serpent():
    # Jouer le son
    son_jeu.play()
    # Initialiser le serpent avec trois segments
    snake = [(9, 5), (8, 5), (7, 5)]
    # Initiaiser la direction du serpent
    direction = droite
    # Initialiser la position du pion à manger
    pion = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))
    # Initailiser la couleur des pions
    couleur_pion = random.choice(["#DE1919", "#D57132", "#D176B1"])

    while True:
        #print("Tête = ", snake[0], "Corps = ", snake[1], "Queue = ", snake[2])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != bas:
                    direction = haut
                elif event.key == pygame.K_DOWN and direction != haut:
                    direction = bas
                elif event.key == pygame.K_LEFT and direction != droite:
                    direction = gauche
                elif event.key == pygame.K_RIGHT and direction != gauche:
                    direction = droite

        # Position actuelle de la tete du serpent
        deplacement = snake[0]
        # Calculer les nouvelles coordonnées de la tête en ajoutant sa direction 
        # au x et y où se trouve la tête de base
        x, y = deplacement[0] + direction[0], deplacement[1] + direction[1]
        # Insère les nouvelles données du déplacement au début du tableau snake[]
        snake.insert(0, (x,y))

        # Gestion des collisions sur les bords
        if (x < 0 or x >= nb_cellule_x) or (y < 0 or y >= nb_cellule_y) or (snake.count((x, y)) > 1):
            depart_serpent()
        
        # Vérifier si le serpent a mangé le pion, donc si il est à la même position que le pion
        if (x, y) == pion:
            # Générer une nouvelle position pour le pion
            pion = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))
            couleur_pion = random.choice(["#DE1919", "#D57132", "#D176B1"])
            mange_pion.play()
        else:
            # Si le serpent n'a pas mangé le pion, on enlève le dernier segment du serpent
            # (ca gardera la même taille du serpent, sinon il grandira à chaque déplacement)
            snake.pop()

        fenetre.fill(bleu)

        # Dessiner le serpent, 
        for segment in snake:
            pygame.draw.rect(fenetre, orange, (segment[0] * cellule, segment[1] * cellule, cellule, cellule))
            #print("x = ", segment[0] * cellule, " y = ", segment[1] * cellule, "   width = ", cellule, " height = ", cellule)
        # Dessiner le pion à manger
        pygame.draw.rect(fenetre, couleur_pion, (pion[0] * cellule, pion[1] * cellule, cellule, cellule))

        # Contrôler la vitesse du jeu
        horloge.tick(5)

        pygame.display.update()

depart_serpent()
