import math


# https://easings.net/
# Les courbes d'accélérations (easing functions) décrivent la vitesse à laquelle un paramètre change en fonction du temps
def easeOutBack(x):
    """
    https://easings.net/#easeOutBack
    Paramètre:
        - x: représente la progression de l'animation dans une plage variant de 0 (début de l'animation) à 1 (fin de l'animation)
    Renvoie le résultat du calcul 'ease out back' en fonction de x
    """
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(x - 1, 3) + c1 * math.pow(x - 1, 2)

def linear(x):
    """
    Renvoie simplement le paramètre passé, pour animation linéaire
    Paramètre:
        - x: représente la progression de l'animation dans une plage variant de 0 (début de l'animation) à 1 (fin de l'animation)
    Renvoie le résultat du calcul 'linear' en fonction de x
    """
    return x


def animation_menu_debut(menu, bg_canvas, menu_image, pr):
    """
    Première animation (début) de l'image du menu dans menuTK.py
    Paramètres:
        - menu: la fenêtre du menu
        - bg_canvas: le canvas du menu
        - menu_image: l'image du menu
        - pr: la progression de l'animation (0 à 1)
    """
    x_b = bg_canvas.coords(menu_image)[0] # Récupère les coordonées en x de l'image
    x_depart, x_arrivee = -406, 0 # Définitions des points en x de départ et d'arriver
    # Calcule de l'animation celon sa progression
    x = round( easeOutBack(pr) * (x_arrivee-x_depart) + x_depart )
    # Fait bouger l'image à sa nouvelle position
    bg_canvas.move(menu_image, x-x_b, 0)
    if pr < 1: # Tant que l'animation n'est pas fini en recommence environ 1/60 de seconde plus tard
        pr += 1/60
        # Si la progression a dépassé sa terminaison on la rectifie
        if pr > 1: pr = 1
        menu.after(int(1000/60), animation_menu_debut, menu, bg_canvas, menu_image, pr)
        
def animation_menu_fin(menu, bg_canvas, menu_image, pr):
    """
    Deuxième animation (fin) de l'image du menu dans menuTK.py
    Paramètres:
        - menu: la fenêtre du menu
        - bg_canvas: le canvas du menu
        - menu_image: l'image du menu
        - pr: la progression de l'animation (0 à 1)
    """
    x_b = bg_canvas.coords(menu_image)[0] # Récupère les coordonées en x de l'image
    x_depart, x_arrivee = 0, -406 # Définitions des points en x de départ et d'arriver
    # Calcule de l'animation celon sa progression
    x = round( linear(pr) * (x_arrivee-x_depart) + x_depart )
    # Fait bouger l'image à sa nouvelle position
    bg_canvas.move(menu_image, x-x_b, 0)
    if pr < 1: # Tant que l'animation n'est pas fini en recommence environ 1/60 de seconde plus tard
        pr += 1/60
        # Si la progression a dépassé sa terminaison on la rectifie
        if pr > 1: pr = 1
        menu.after(int(1000/60), animation_menu_fin, menu, bg_canvas, menu_image, pr)
            
def animation_niveau_debut(menu, bg_canvas, niveaux_image, pr):
    """
    Animation de l'image du menu de choix de niveau dans menuTK.py
    Paramètres:
        - menu: la fenêtre du menu
        - bg_canvas: le canvas du menu
        - menu_image: l'image du menu de choix de niveau
        - pr: la progression de l'animation (0 à 1)
    """
    x_b = bg_canvas.coords(niveaux_image)[0] # Récupère les coordonées en x de l'image
    x_depart, x_arrivee = 407, -5 # Définitions des points en x de départ et d'arriver
    # Calcule de l'animation celon sa progression
    x = round( linear(pr) * (x_arrivee-x_depart) + x_depart )
    # Fait bouger l'image à sa nouvelle position
    bg_canvas.move(niveaux_image, x-x_b, 0)
    if pr < 1: # Tant que l'animation n'est pas fini en recommence environ 1/60 de seconde plus tard
        pr += 1/60
        # Si la progression a dépassé sa terminaison on la rectifie
        if pr > 1: pr = 1
        menu.after(int(1000/60), animation_niveau_debut, menu, bg_canvas, niveaux_image, pr)
