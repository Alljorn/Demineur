from demineur import *
from tkinter import *
from PIL import Image, ImageTk


# Dictionnaire constant permettant de définir les règles pour chaque niveaux
NIVEAUX = {"Debutant": {"NB_LIGNES": 10, "NB_COLONNES": 7, "NOMBRE_MINES": 10},
           "Intermediaire": {"NB_LIGNES": 16, "NB_COLONNES": 16, "NOMBRE_MINES": 40},
           "Expert": {"NB_LIGNES": 16, "NB_COLONNES": 31, "NOMBRE_MINES": 99},
           }

def jouer(choix_de_partie):
    # On met le choix à Quitter pour pouvoir fermer la fenêtre
    choix_de_partie[0] = "Quitter"
    niveau = choix_de_partie[1] # Récupére le choix du niveau
    
    ### image_demineur.py ###
    # Si on import le fichier (image_demineur.py) ça va créer une fenêtre lors de l'importation de ce fichier (interfaceTK.py) dans menuTK.py
    
    # Création de la fenêtre et chargement des images
    fen = Tk()

    COTE_CASE =40
    

    cache = Image.open('images/case_cache.png')
    cache= cache.resize((COTE_CASE, COTE_CASE))
    cache = ImageTk.PhotoImage(cache, master=fen)

    mine = Image.open('images/case_bombe.png')
    mine= mine.resize((COTE_CASE, COTE_CASE))
    mine = ImageTk.PhotoImage(mine, master=fen)

    zero = Image.open('images/case_0.png')
    zero= zero.resize((COTE_CASE, COTE_CASE))
    zero = ImageTk.PhotoImage(zero, master=fen)

    un= Image.open('images/case_1.png')
    un= un.resize((COTE_CASE, COTE_CASE))
    un = ImageTk.PhotoImage(un, master=fen)


    deux = Image.open('images/case_2.png')
    deux = deux .resize((COTE_CASE, COTE_CASE))
    deux  = ImageTk.PhotoImage(deux , master=fen)

    trois = Image.open('images/case_3.png')
    trois= trois.resize((COTE_CASE, COTE_CASE))
    trois = ImageTk.PhotoImage(trois, master=fen)

    quatre= Image.open('images/case_4.png')
    quatre= quatre.resize((COTE_CASE, COTE_CASE))
    quatre = ImageTk.PhotoImage(quatre, master=fen)

    cinq = Image.open('images/case_5.png')
    cinq= cinq.resize((COTE_CASE, COTE_CASE))
    cinq = ImageTk.PhotoImage(cinq, master=fen)

    six = Image.open('images/case_6.png')
    six = six .resize((COTE_CASE, COTE_CASE))
    six  = ImageTk.PhotoImage(six , master=fen)

    sept = Image.open('images/case_7.png')
    sept= sept.resize((COTE_CASE, COTE_CASE))
    sept = ImageTk.PhotoImage(sept, master=fen)

    huit = Image.open('images/case_8.png')
    huit= huit.resize((COTE_CASE, COTE_CASE))
    huit = ImageTk.PhotoImage(huit, master=fen)

    drapeau= Image.open('images/case_drapeau.png')
    drapeau= drapeau.resize((COTE_CASE, COTE_CASE))
    drapeau = ImageTk.PhotoImage(drapeau, master=fen)
    ### ----- ###

    
    # Récupère le nombre de ligne et de colonne correspondant au niveau via le dictionnaire NIVEAUX
    NB_LIGNES = NIVEAUX[niveau]["NB_LIGNES"]
    NB_COLONNES=NIVEAUX[niveau]["NB_COLONNES"]
    
    # Calcule des dimmentions du plateau
    HAUTEUR_PLATEAU_JEU = NB_LIGNES*COTE_CASE
    LARGEUR_PLATEAU_JEU = NB_COLONNES*COTE_CASE


    # Récupére le nombre de mines correspondant au niveau via le dictionnaire NIVEAUX
    NOMBRE_MINES = NIVEAUX[niveau]["NOMBRE_MINES"]


    # Ajout d'une zone d'affichage pour un chronomètre et un compteur de nombre de mines restantes
    can_top = Canvas(fen, width=LARGEUR_PLATEAU_JEU)
    
    # Séparation de la zone d'affichage en deux parties
    # Partie chronomètre
    can_chrono = Canvas(can_top)
    # Variable qui, si passe à False, stop le chronomètre définitivement
    chrono_continue = [True] # Liste pour pouvoir être modifié dans d'autre fonction
    # Affichage texte
    wd_chrono_text = Label(can_chrono, text="Temps écoulé:")
    wd_chrono_valeur = Label(can_chrono, text="0")
    # Fonction incrémente le chronomètre toute les une seconde
    def getTime():
        wd_chrono_valeur['text'] = (str(int(wd_chrono_valeur['text'])+1))
        if chrono_continue[0]: fen.after(1000, getTime)
    
    # Partie nombre de mines restantes
    can_nombre_mines = Canvas(can_top)
    # Affichage texte
    wd_nombre_mines_text = Label(can_nombre_mines, text="Nombre de mines restantes:")
    wd_nombre_mines_restantes = Label(can_nombre_mines, text=NOMBRE_MINES) # Affiche le nombre total de mines par défaut
    
    
    # Affichage des composant
    wd_chrono_text.pack(padx= LARGEUR_PLATEAU_JEU/10)
    wd_chrono_valeur.pack()
    can_chrono.grid(row=0, column=0)

    wd_nombre_mines_text.pack(padx= LARGEUR_PLATEAU_JEU/10)
    wd_nombre_mines_restantes.pack()
    can_nombre_mines.grid(row=0, column=1)

    can_top.pack()

    ####################################### Définition du canevas #####################################################################################
    # Le canevas représente une surface pour dessiner.
    # Avec Tkinter, on ne peut pas dessiner ni insérer d'images en dehors d'un canevas.

    can = Canvas(fen, bg="light gray", height=HAUTEUR_PLATEAU_JEU, width=LARGEUR_PLATEAU_JEU)
    can.pack() 
    # pack va ajuster notre fenêtre à la taille du canevas.


    ####################################### Création de la grille de jeu ##############################################################################
    grille_jeu=generer_grille_jeu(NB_LIGNES,NB_COLONNES,NOMBRE_MINES)


    ###################################### Création et affichage du plateau de jeu  associé à la grille de jeu #########################################
    # On crée une grille d'images: liste de listes de même taille que la grille de jeu . Au départ, chaque case contient l'image "cache".
    # L'affichage du plateau sera mis à jour à chaque action à l'aide de la fonction affichage
    plateau_jeu=[] # on stocke les images de chaque case dans une liste de listes pour pouvoir modifier leur couleur
    for i in range(NB_LIGNES):
        ligne=[]
        for j in range(NB_COLONNES):
            ligne.append(can.create_image(COTE_CASE*j,COTE_CASE*i, anchor = NW, image = cache))
        plateau_jeu.append(ligne)




    def affichage(grille,plateau):
        """ La fonction affichage
            - prend pour paramètres une grille de jeu (liste de listes) et un plateau de jeu (liste de listes)
            - met à jour l'affichage du plateau de jeu avec les informations contenues dans la grille de jeu en fonction de l'état et de la valeur de chaque case        
        """
        for i in range(NB_LIGNES):
            for j in range(NB_COLONNES):
                case=grille[i][j] 
                if case['etat']==0: # cas où la case est cachée : on affiche l'image "cache"
                    can.itemconfigure(plateau[i][j], image=cache)  
                elif case['etat']==1: # cas où la case est découverte : on affiche l'image en fonction de sa valeur
                    if case['valeur']==-1:
                        can.itemconfigure(plateau[i][j], image=mine)
                    elif case['valeur']==0:
                        can.itemconfigure(plateau[i][j], image=zero)
                    elif case['valeur']==1:
                        can.itemconfigure(plateau[i][j], image=un)
                    elif case['valeur']==2:
                        can.itemconfigure(plateau[i][j], image=deux)
                    elif case['valeur']==3:
                        can.itemconfigure(plateau[i][j], image=trois)
                    elif case['valeur']==4:
                        can.itemconfigure(plateau[i][j], image=quatre)
                    elif case['valeur']==5:
                        can.itemconfigure(plateau[i][j], image=cinq)
                    elif case['valeur']==6:
                        can.itemconfigure(plateau[i][j], image=six)
                    elif case['valeur']==7:
                        can.itemconfigure(plateau[i][j], image=sept)
                    elif case['valeur']==8:
                        can.itemconfigure(plateau[i][j], image=huit)
                elif case['etat']==2: # cas où la case comporte un drapeau : on affiche l'image "drapeau"
                    can.itemconfigure(plateau[i][j], image=drapeau)

    ################################## fonctions liées à la détection d'un évènement souris (clic gauche ou clic droit) #############################################
                    
    def choix_case(event):
        """ La fonction choix_case :
                 - prend pour paramètre un évènement souris
                 - renvoie la ligne et la colonne liées à cet évènement dans la grille de jeu
        """
        # On récupère la position de la souris
        x = event.x  # abscisse
        y = event.y  # ordonnée
        ligne=y//COTE_CASE # on calcule la ligne correspondante dans la grille de jeu
        colonne=x//COTE_CASE # on calcule la colonne correspondante dans la grille de jeu    
        return ligne,colonne



    peut_cliquer = [True] # Liste pour pouvoir être modifié dans d'autre fonction              
    def clic_gauche(event):
        """ La fonction clic_gauche est liée à la détection d'un click sur le bouton gauche de la souris  
                  - elle prend pour paramètre un évènement souris
                  - elle "découvre" la case correspondante 
                  - et met à jour l'affichage du plateau de jeu
        """
        if not peut_cliquer[0]: return # Si on ne peut pas cliquer on sort de la fonction
        
        ligne,colonne=choix_case(event)
        ouvrir(grille_jeu,ligne,colonne)
        affichage(grille_jeu,plateau_jeu)
        
        # Test si le joueur a gagné
        gagner = a_gagner(grille_jeu)
        if gagner == 1:
            # Stop le chronomètre et la possibilité de cliquer
            chrono_continue[0] = False
            peut_cliquer[0] = False
            
            # Affichage d'une fenêtre de victoire
            fen_gagner = Toplevel(fen)
            fen_gagner.geometry(f'400x{int(HAUTEUR_PLATEAU_JEU/2)}')
            message = Label(fen_gagner, text=f"C'est gagné !\nTemps écoulé: {int(wd_chrono_valeur['text'])+1} seconde") # Affiche le temps écoulé
            
            # Fonctions permettant de faire un choix et de fermer la fenêtre de jeu
            def rejouer():
                choix_de_partie[0] = 'Rejouer'
                fen.destroy()
            def menu():
                choix_de_partie[0] = 'Menu'
                fen.destroy()
            def quitter():
                choix_de_partie[0] = 'Quitter'
                fen.destroy()
            # Création des boutons associés à leurs fonctions (voir ci dessus)
            bouton_rejouer = Button (fen_gagner, text = "Rejouer", command=rejouer)
            bouton_menu = Button (fen_gagner, text = "Retour au menu", command=menu)
            bouton_quitter = Button(fen_gagner, text="Quitter", command=quitter)
            
            # Affichage des composants
            message.pack()
            bouton_rejouer.pack()
            bouton_menu.pack()
            bouton_quitter.pack()
            
        
        elif gagner == -1:
            # Stop le chronomètre et la possibilité de cliquer
            chrono_continue[0] = False
            peut_cliquer[0] = False
            
            # Affichage d'une fenêtre de défaite
            fen_perdu= Toplevel(fen)
            fen_perdu.geometry(f'400x{int(HAUTEUR_PLATEAU_JEU/2)}')
            message = Label(fen_perdu, text=f"C'est perdu !\nTemps écoulé: {int(wd_chrono_valeur['text'])+1} seconde") # Affiche le temps écoulé
            
            # Fonctions permettant de faire un choix et de fermer la fenêtre de jeu
            def rejouer():
                choix_de_partie[0] = 'Rejouer'
                fen.destroy()
            def menu():
                choix_de_partie[0] = 'Menu'
                fen.destroy()
            def quitter():
                choix_de_partie[0] = 'Quitter'
                fen.destroy()
            # Création des boutons associés à leurs fonctions (voir ci dessus)
            bouton_rejouer = Button(fen_perdu, text="Rejouer", command=rejouer)
            bouton_menu = Button(fen_perdu, text="Retour au menu", command=menu)
            bouton_quitter = Button(fen_perdu, text="Quitter", command=quitter)
            
            # Affichage des composants
            message.pack()
            bouton_rejouer.pack()
            bouton_menu.pack()
            bouton_quitter.pack()        


    def clic_droit(event): # fonction liée à la détection d'un click sur le bouton droit de la souris
        if not peut_cliquer[0]: return # Si on ne peut pas cliquer on sort de la fonction
        
        ligne,colonne=choix_case(event)
        marquer(grille_jeu,ligne,colonne)
        affichage(grille_jeu,plateau_jeu)
        
        # Met à jour le compteur de mines restantes
        # On compte en fait le nombre de drapeau posé soustrait au nombre de mines total et non le
        # nombre de mines trouvé soustrait au nombre de mines total pour éviter que l'on puisse tricher en
        # posant un drapeau et vérifier si le compteur c'est abaissé
        wd_nombre_mines_restantes['text'] = NOMBRE_MINES - nombre_drapeau(grille_jeu)
        
        
    # Pour détecter un click sur le bouton gauche de la souris, on va relier (bind en anglais) cet évenement (<Button-1>) à une fonction   
    can.bind("<Button-1>", clic_gauche)
     
    # Pour détecter un click sur le bouton droit de la souris, on va relier cet évenement (<Button-3>) à une fonction 
    can.bind("<Button-3>", clic_droit)

    fen.after(1000, getTime) # Lancement du chronomètre
    fen.mainloop()



    # A partir de cette instruction, Tkinter est en alerte et réceptionne plusieurs fois par secondes les événements clavier et souris,
    # il regarde tout ce qui se passe et vous avertit lorsqu'il détecte un des événements que vous lui aurez demandé de surveiller
    # C'est pourquoi on met cette instruction en dernier: on démarre la surveillance une fois que tous les objets ont étés correctement placés.
