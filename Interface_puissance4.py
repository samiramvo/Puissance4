#------------------
#BRAVO A TOI SAMIRA
#------------------

import os
from tkinter import image_types
from webbrowser import BackgroundBrowser
import pygame
from pygame.locals import*
import pygame.freetype
pygame.init()
import numpy as np
from numpy import zeros


nb_colonne=7
nb_ligne=6
cases=100
cases2=200
rayon= (cases/2)-15
rayon2= (cases/2)-30
largeur = (nb_colonne* cases)+600;
hauteur = (nb_ligne+1) * cases;
taille = (largeur, hauteur);
nb_col=2;
nb_lig=21;

tab=zeros((6,7), int)
def create_board():
    
    print(np.flip(tab,0))

def mouvement_pion(tab,nb_colonne):
    if tab[nb_ligne-1][nb_colonne]==0:
      return True
    else:
     return False

class IA :
    """On attribue a l'objet IAJERRY des attributs"""
    def __init__(self):
        """On definit la representation de l'objet IAJERRY"""
        self.representation=1
        
class Player :
    """On attribue a l'objet IAJERRY des attributs"""
    def __init__(self):
        """On definit la representation de l'objet IAJERRY"""
        self.representation=2
joueur1=IA()
joueur2=Player() 




     
#Differentes couleurs utilisables pour mon jeu
blanc=(255,255,255)
Gris=(185,198,191)
violet=(100,14,50)
vert=(0,255,0)
bleu=(0,0,255)
noir=(0,0,0)
bleu_ciel=(153,217,234)
rouge=(255,255,0)
jaune=(237,28,36)

nb_colonne=7
nb_ligne=6
cases=100
cases2=200
rayon= (cases/2)-15

largeur = (nb_colonne* cases)+600;
hauteur = (nb_ligne+1) * cases;
taille = (largeur, hauteur);
nb_col=2;
nb_lig=5;
# Initialisation d'une surface à afficher
screen = pygame.display.set_mode((taille))

paint= pygame.image.load("./assets/ciel_etoile.jpg").convert()
screen.blit(paint,(0,0))

def dessiner_plateau(tab):
#Mise en place de ma plateforme de jeu  
        pygame.draw.rect(paint,bleu,(0,cases,nb_colonne*cases,(nb_ligne+1)*cases))

        for col in range (nb_colonne):
                    for lig in range(nb_ligne):
                        cercle=pygame.draw.circle(paint,noir,((col*cases+cases/2),(lig*cases+cases/2+cases)),rayon)



        pygame.draw.rect(paint,violet,(900,cases,nb_col*cases2,(nb_lig)*cases))
        pygame.draw.rect(paint,noir,(900,cases,nb_col*cases2,(nb_lig)*cases),5)
        pygame.draw.line(paint,noir,(900,300),(1300,300),4)
        pygame.draw.line(paint,noir,(1100,100),(1100,600),4)
        
        
        imgIA= pygame.image.load("./assets/image Joueur.jpg").convert()
        paint.blit(imgIA,(900,100))
        imgJoueur= pygame.image.load("./assets/image IA.jpg").convert()
        paint.blit(imgJoueur,(1100,100))
        cercle1=pygame.draw.circle(paint,blanc,(1000,400),60)
        cercle2=pygame.draw.circle(paint,noir,(1200,400 ),60)
        
        
        for col in range (nb_colonne):
             for lig in range(nb_ligne):
                        
                if tab[lig][col] == 1:   
                        pygame.draw.circle(paint,rouge,((col*cases+cases/2),hauteur-(lig*cases+cases/2)),rayon)
                        
                if tab[lig][col] == 2: 
                        pygame.draw.circle(paint,jaune,((col*cases+cases/2),hauteur-(lig*cases+cases/2)),rayon)
pygame.display.flip()

tab[0][1]=1
tab[1][3]=2
tab[0][2]=1
tab[2][3]=2


dessiner_plateau(tab)  
# Mise à jour du jeu et affichage
pygame.display.update()                 
#Mise en place d'une musique de fond
pygame.mixer.init()
pygame.mixer.music.load("./assets/Bramsito_-_Sale_mood_ft._Booba.mp3")
            
pygame.mixer.music.play()
        

#Personnalisation du curseur de la souris

souris=pygame.mouse.set_cursor(*pygame.cursors.tri_left)


        #Donner un titre à mon jeu
pygame.display.set_caption("PUISSANCE 4")
pygame.key.get_pressed()
pygame.event.wait()
pygame.mouse.get_pressed()

        
#Deplacements de la souris

x=0
y=0
screen.blit(paint, (x,y))

run = True
while run:
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                       posx=event.pos[0] 
                        
                    
                    if event.type == pygame.QUIT or (event.type ==KEYDOWN and (event.key==K_q or event.key==K_SPACE)):
                       run = False
                         
                    # Raffraichissement de l'ecran
                    pygame.display.flip()
                    
pygame.time.wait(3000)
pygame.quit()
quit()

 
