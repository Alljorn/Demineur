from random import *


def placer_mines(grille, nb_mines):
    """place à des positions aléatoires un nombre de mines défini
       arguments:
         grille: la grille de jeu, de type list
         nb_mines: le nombre de mines à placer, de type int
    """
    while nb_mines != 0: # Tant qu'il reste des mines à placer
        # Choix d'une position aléatoire
        ligne = randint(0, len(grille)-1)
        largeur = randint(0, len(grille[0])-1)
        if grille[ligne][largeur]["valeur"] != -1: # Si il n'y a pas déjà de mines à cette position
            # On place la mine et on enlève une mine au nombre de mines à placer
            grille[ligne][largeur]["valeur"] = -1
            nb_mines -= 1
            
            
def valeur_case(grille, l, c):
    """renvoie la valeur d'une case défini
       arguments:
        grille: la grille de jeu, de type list
        l: le numéro de ligne, de type int
        c: le numéro de colonne, de type int
        renvoie le nombre de mines entourant la case ciblée, un integer
    """
    # Si il y a une mine sur la case, sa valeur est -1
    if grille[l][c]["valeur"] == -1:
        return -1
    
    nb_mine = 0 # Creer une variable nb_mine qui représente la valeur d'une case (compteur)
    for ligne in range(l-1, l+1 +1): # Pour les lignes entourant et comprenant la case  
        for colone in range(c-1, c+1 +1): # Pour les colonnes entourant et comprenant la case  
            # Vérifie que la case ciblé par la boucle ne soit pas en dehors de la grille de jeu
            if ligne>=0 and ligne<len(grille) and colone>=0 and colone<len(grille[0]):
                # Et si il y a une mine sur cette case
                if grille[ligne][colone]["valeur"] == -1:
                    nb_mine +=1 # On incrémente le compteur
    return nb_mine
    


def generer_grille_jeu(hauteur, largeur, nb_mines):
    """genere une grille de jeu
       arguments:
         hauteur: hauteur de la grille de jeu, de type int
         largeur: largeur de la grille de jeu, de type int
         nb_mines: nombre de mines à placer, de type int
        renvoie une liste
    """
    # Creez une grille de jeu par compréhension (chaque case de valeur et d'etat nul), de largeur et hauteur voulu
    grille = [[{"valeur": 0, "etat": 0} for j in range(largeur)] for i in range(hauteur)]
    placer_mines(grille, nb_mines) # Place le nombre de mine voulu dans la grille de jeu
    # Pour chaque case de la grille de jeu
    for l in range(hauteur):
        for c in range(largeur):
            # Donne une valeur à chaque case de la grille
            grille[l][c]["valeur"] = valeur_case(grille, l, c)
    return grille
    

def marquer(grille,l,c):
    """met un drapeau sur une case ciblé si il n'y en a pas et l'enlève sinon
       arguments:
         grille: la grille de jeu,  de type list
         l: le numéro de ligne, de type int
         c: le numéro de colonne, de type int
    """
    # Si la case n'est pas ouverte 
    if grille[l][c]["etat"] != 1:
        if grille[l][c]["etat"] == 0: # Si la case n'est pas marquée
            # On met un drapeau
            grille[l][c]["etat"] = 2
        elif grille[l][c]["etat"] == 2: # Si la case est marquée
            # On enlève le drapeau
            grille[l][c]["etat"] = 0
            
"""
def ouvrir(grille, l, c):
    \"""Ouvre la case désigné
       arguments:
         grille: la grille de jeu, de type list
         l: le numéro de ligne, de type int
         c: le numéro de colonne, de type int
    \"""
    # Si la case n'est pas marqué d'un drapeau
    if grille[l][c]["etat"] != 2:
        grille[l][c]["etat"] = 1 # On l'ouvre
"""

def ouvrir(grille, l, c):
    """Ouvre la case désigné et se propage (fonction récursive)
       arguments:
         grille: la grille de jeu, de type list
         l: le numéro de ligne, de type int
         c: le numéro de colonne, de type int
    """
    # Il y a plusieurs état trivial
    # Si la case ciblé est en dehors de la grille de jeu
    if l>=len(grille) or l<0 or c>=len(grille[0]) or c<0:
        return
    # Si la case est ouverte ou marqué d'un drapeau
    elif grille[l][c]["etat"] != 0:
        return
    # Si la case contient une valeur (une mine ou une indication sur le nombre de mines alentours)
    elif grille[l][c]["valeur"] != 0:
        # On l'ouvre
        # Par propagation une case qui contient une mine ne sera pas ouverte car elle est forcment
        # entouré de case contenant une indication sur le nombre de mines alentours
        # Elle sera ouverte seulement si l'utilisateur clique directement dessus
        grille[l][c]["etat"] = 1
        return
    
    # On ouvre la case
    grille[l][c]["etat"] = 1
    
    ouvrir(grille, l+1, c) # Ouvrir bas
    ouvrir(grille, l, c+1) # Ouvrir droite
    ouvrir(grille, l-1, c) # Ouvrir haut
    ouvrir(grille, l, c-1) # Ouvrir gauche
    # Ouvrir angles
    ouvrir(grille, l+1, c+1) # bas droite
    ouvrir(grille, l+1, c-1) # bas gauche
    ouvrir(grille, l-1, c+1) # haut droite
    ouvrir(grille, l-1, c-1) # haut gauche
    
    # On conduit bien vers une des conditions d'arret car même si il n'y a aucune mine et (donc) aucune indication
    # sur les mines alantours, la propagation atteindra une case ouverte ou marqué d'un drapeau et au final, les bord
    # de la grille de jeu


def a_gagner(grille):
    """
    Test si le joueur a gagné
    Paramètres:
        - grille: une grille de jeu, de type list
    Renvoie 1 si le joueur a gagné, 0 si le joueur n'a pas encore gagné et -1 si le joueur a ouvert une case comportant une mine
    """
    valeur = 1 # La variable qui dit l'état du joueur
    # Pour chaque case de la grille de jeu
    for ligne in grille:
        for colonne in ligne:
            # Si une case qui comporte une mine est ouverte
            if colonne['valeur'] == -1 and colonne['etat'] == 1: 
                return -1 # Le joueur a perdu
            elif colonne['valeur'] >= 0 and colonne['etat'] != 1: # Si une case sans mine n'est pas ouverte
                valeur = 0 # le joueur peut continuer de jouer
    return valeur

def nombre_drapeau(grille):
    """
    Compte le nombre de drapeau sur la grille de jeu
    Paramètres:
        - grille: une grille de jeu de type list
    Renvoie le nombre de drapeau sur la grille de jeu
    """
    nbr_drapeau = 0 # Compteur du nombre de drapeau posé
    # Pour chaque case de la grille de jeu
    for ligne in grille:
        for colonne in ligne:
            # Si il y a un drapeau sur la case
            if colonne['etat'] == 2:
                nbr_drapeau += 1 # On incrémente le compteur
    return nbr_drapeau

