from tkinter import *
from animations import *
from interfaceTK import jouer


def menu_tk(choix_de_partie):
    # On met le choix à Quitter pour pouvoir fermer la fenêtre
    choix_de_partie[0] = "Quitter"
    
    # Création de la fenêtre
    menu = Tk()
    menu.geometry("406x648")
    
    # Chargement des images
    # Arrière plan
    bg = PhotoImage(file = "images_menu/game_bg.png")
    bg_canvas = Canvas( menu, width = 406, height = 648, bd=0) 
    bg_canvas.pack()
    bg_canvas.create_image( 0, 0, image = bg, anchor = "nw")
    # Menu
    img = PhotoImage(file = 'images_menu/menu_image.png')
    menu_image=bg_canvas.create_image(-406,0,anchor=NW,image=img)
    # Choix de Niveau
    img_n = PhotoImage(file = 'images_menu/niveaux_image.png')
    niveau_image=bg_canvas.create_image(407,0,anchor=NW,image=img_n)

    
    def choix_boutton_menu(event):
        """ La fonction choix_boutton_menu est liée à la détection d'un click sur le bouton gauche de la souris dans le menu
                  - elle prend pour paramètre un évènement souris
                  - elle appuie sur le boutton correspondant
                  - et effectue les actions qui leurs sont associées
        """
        x = event.x  # abscisse
        y = event.y  # ordonnée
        # Détecte si l'on clique sur un boutton
        if 143 <= x and x <= 270:
            if 330 <= y and y <= 371: # Bouton Jouer
                # Lance les animations
                menu.after(0, animation_menu_fin, menu, bg_canvas, menu_image, 0)
                menu.after(0, animation_niveau_debut, menu, bg_canvas, niveau_image, 0)
                # Redéfinie la fonction liée à la détection d'un click sur le bouton gauche de la souris pour le menu de choix de niveau
                menu.bind("<Button-1>", choix_boutton_niveau)
            elif 401 <= y and y <= 442: # Bouton Credit
                credit = Toplevel(menu)
                texte = Label(credit, text="### Projet NSI ###\n --- Allan & Guillaume ---")
                texte.pack()
            elif 473 <= y and y <= 516: # Bouton Quitter
                # Ferme la fen^tre
                menu.destroy()
        
    def choix_boutton_niveau(event):
        """ La fonction choix_boutton_menu est liée à la détection d'un click sur le bouton gauche de la souris dans le menu de choix de niveau
                  - elle prend pour paramètre un évènement souris
                  - elle appuie sur le boutton correspondant
                  - et effectue les actions qui leurs sont associées
    """
        x = event.x  # abscisse
        y = event.y  # ordonnée
        # Détecte si l'on clique sur un boutton
        if 143 <= x and x <= 270:
            if 225 <= y and y <= 269: # Bouton Débutant
                menu.destroy() # Ferme la fenêtre
                # Met à jour les paramètres 'choix_de_partie' pour 'Debutant'
                choix_de_partie[1] = 'Debutant'
                # Lance le jeu
                jouer(choix_de_partie)
            elif 345 <= y and y <= 388: # Bouton Intermediaire
                menu.destroy() # Ferme la fenêtre
                # Met à jour les paramètres 'choix_de_partie' pour 'Intermediaire'
                choix_de_partie[1] = 'Intermediaire'
                # Lance le jeu
                jouer(choix_de_partie)
            elif 454 <= y and y <= 497: # Bouton Expert
                menu.destroy() # Ferme la fenêtre
                # Met à jour les paramètres 'choix_de_partie' pour 'Expert'
                choix_de_partie[1] = 'Expert'
                # Lance le jeu
                jouer(choix_de_partie)

    
    # Lance l'animations du menu
    menu.after(0, animation_menu_debut, menu, bg_canvas, menu_image, 0)
    
    # Pour détecter un click sur le bouton gauche de la souris, on va relier (bind en anglais) cet évenement (<Button-1>) à une fonction
    menu.bind("<Button-1>", choix_boutton_menu)
    menu.mainloop()
