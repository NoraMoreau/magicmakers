import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mon Memory Game")

# les couleurs utilisées pour la fenetre
bleu = (0, 0, 255)
blanc = (255, 255, 255)

# Ajout des variables de configuration des cartes
carte_largeur = 100
carte_hauteur = 100
espacement_des_cartes = 10
nb_lignes = 4
nb_colonnes = 4

# Creation du chemin de simages
images = ["image1.png", 
          "image2.png", 
          "image3.png", 
          "image4.png", 
          "image5.png", 
          "image6.png", 
          "image7.png", 
          "image8.png"]

# Calculer le nombre de paires nécessaires
nombre_de_paires = (nb_lignes * nb_colonnes) // 2
# Générer une liste de nombre sous forme de chaînes de caractères
nombres =  []
for nombre in range(nombre_de_paires):
    nombres.append(str(nombre))

# Dupliquer chaque nombre pour créer des paires
paires = nombres * 2
# Mélanger les paires aléatoirement
random.shuffle(paires)
# Afficher en concole les paires mélangées
print(paires)

# Chargement des images et redimensionnement
liste_images = []
for image in images:
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (carte_largeur, carte_hauteur))
    liste_images.append(image)

# Création de la grille de cartes
cartes = []
# Parcourir chaque ligne de la grille
for ligne in range(nb_lignes):
    # Parcourir chaque colonne de la grille
    for colonne in range(nb_colonnes):
        # Calculer la position x et y de chaque carte
        x = colonne * (carte_largeur + espacement_des_cartes) + (largeur - (carte_largeur + espacement_des_cartes) * nb_colonnes) // 2
        y = ligne * (carte_hauteur + espacement_des_cartes) + (hauteur - (carte_hauteur + espacement_des_cartes) * nb_lignes) // 2
        # Créer un dictionnaire pour chaque carte avec ses propriétés
        carte = {
            'valeur_carte': paires.pop(),
            'dessin_carte': pygame.Rect(x, y, carte_largeur, carte_hauteur),
            'carte_retournee': False,
            'carte_identique': False
        }
        # Ajouter la carte à la liste des cartes
        cartes.append(carte)

# Variables du jeu
cartes_retournees = []
paires_trouvees = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    fenetre.fill(bleu)

    # Dessiner l'emplacement des cartes = un carré blanc
    for carte in cartes:
        pygame.draw.rect(fenetre, blanc, carte['dessin_carte'])

    # On écoute les événements de la souris; si un clic est détecté et qu'on n'a pas encore trouvé toutes les paires on entre dans le if
    if event.type == pygame.MOUSEBUTTONDOWN and paires_trouvees < nombre_de_paires:
        # On récupère la position de la souris
        position_souris = pygame.mouse.get_pos()
        # Parcourt toutes les cartes pour vérifier quelle carte a été cliquée dans notre liste de cartes
        for carte in cartes:
            # Vérifie si la carte n'est pas déjà identifiée comme paire 
            # et si la souris est bien sur la carte
            if not carte['carte_identique'] and carte['dessin_carte'].collidepoint(position_souris):
                # Si la carte n'est pas encore retournée (pour éviter de retourner une carte déjà face visible dans le cas où on retourne notre deuxième carte)
                if not carte['carte_retournee']:
                    # On retourne la carte
                    carte['carte_retournee'] = True
                    # On ajoute la carte à la liste des cartes retournées
                    cartes_retournees.append(carte)
                    # Si deux cartes sont retournées, on vérifie si elles sont identiques; sinon on attend le prochain clic
                    if len(cartes_retournees) == 2:
                        # Si les valeurs des deux cartes sont identiques
                        if cartes_retournees[0]['valeur_carte'] == cartes_retournees[1]['valeur_carte']:
                            # On marque les cartes comme identiques
                            cartes_retournees[0]['carte_identique'] = True
                            cartes_retournees[1]['carte_identique'] = True
                            # On incrémente le nombre de paires trouvées
                            paires_trouvees += 1
                        else:
                            # Retourne les cartes face cachée si elles ne sont pas identiques
                            cartes_retournees[0]['carte_retournee'] = False
                            cartes_retournees[1]['carte_retournee'] = False
                        # On réinitialise la liste des cartes retournées
                        cartes_retournees = []

    # Dessiner les cartes
    for carte in cartes:
        if carte["carte_retournee"]:
            fenetre.blit(liste_images[int(carte["valeur_carte"])], carte["dessin_carte"])
        else:
            # On dessine la carte face cachée
            pygame.draw.rect(fenetre, blanc, carte["dessin_carte"])
    
    pygame.display.update()

