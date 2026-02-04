import pygame, sys
from pygame.locals import QUIT

pygame.init()

largeur, hauteur = 800, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('NOKIA 3210')

# Définition des couleurs
# (la fenêtre, le serpent et le pion à manger)
bleu = '#D1FFFB'
orange = '#FFC980'
rose = '#EB68EF'

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

# Méthode pour déplacer le serpent en début de jeu
def depart_serpent():
    # Initialiser le serpent avec trois segments
    snake = [(9, 5), (8, 5), (7, 5)]
    # Initiaiser la direction du serpent
    direction = droite

    while True:
        print("Tête = ", snake[0])
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
        # Insère les nouvelles données dans snake[0] et déplace la tête du serpent vers la nouvelle position
        snake.insert(0, (x,y))

        fenetre.fill(bleu)

        for segment in snake:
            pygame.draw.rect(fenetre, orange, (segment[0] * cellule, segment[1] * cellule, cellule, cellule))

        # Contrôler la vitesse du jeu
        horloge.tick(5)

        pygame.display.update()

depart_serpent()