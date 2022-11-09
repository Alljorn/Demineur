from menuTK import menu_tk
from interfaceTK import jouer


choix_de_partie = ['Quitter', 'Debutant'] # On utilise la propriété des listes qui sont modifiées quand on les donne à une fonction qui la modifie
menu_tk(choix_de_partie) # On lance le menu avec la liste de paramèrtres 'choix_de_partie'
# Ce lance après que l'utilisateur est quitté le menu et/ou sélectionné un choix à la fin d'une partie 
# Tant que l'on ne souhaite pas quitter
while choix_de_partie[0] != 'Quitter':
    if choix_de_partie[0] == 'Menu': # Si l'utilisateur veut retourner au menu 
        menu_tk(choix_de_partie)
    else: # Si l'utilisateur veux rejouer
        jouer(choix_de_partie)