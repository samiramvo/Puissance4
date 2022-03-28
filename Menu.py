
import pygame
import sys
import os
from tkinter import image_types
from webbrowser import BackgroundBrowser
from pygame.locals import*
import pygame.freetype
pygame.init()
import numpy as np
from numpy import zeros


#Differentes couleurs utilisables pour mon jeu
blanc=(255,255,255)
gris=(103,103,103)
violet=(64,15,97)
vert=(0,255,0)
bleu_fonce=(17,10,50)
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



def dessiner_plateau(tab):

    # Initialisation d'une surface à afficher
    screen = pygame.display.set_mode((taille))

    paint= pygame.image.load("assets/ciel_etoile.jpg").convert()
    screen.blit(paint,(0,0))
    
    #Mise en place de ma plateforme de jeu  
    pygame.draw.rect(paint,bleu,(0,cases,nb_colonne*cases,(nb_ligne+1)*cases))

    for col in range (nb_colonne):
         for lig in range(nb_ligne):
            cercle=pygame.draw.circle(paint,noir,((col*cases+cases/2),(lig*cases+cases/2+cases)),rayon)



  
    pygame.draw.rect(paint,gris,(740,cases,nb_col*cases2+160,(nb_lig)*cases),5)
    pygame.draw.line(paint,gris,(740,300),(1300,300),4)
    pygame.draw.line(paint,gris,(1015,100),(1015,600),4)
        
        
    imgIA= pygame.image.load("assets/image Joueur.jpg").convert()
    paint.blit(imgIA,(750,115))
    imgJoueur= pygame.image.load("assets/image IA.jpg").convert()
    paint.blit(imgJoueur,(1020,120))
    cercle1=pygame.draw.circle(paint,bleu_fonce,(880,450),60)
    cercle2=pygame.draw.circle(paint,blanc,(1150,450 ),60)
        

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


                 
                # Mise à jour du jeu et affichage
                pygame.display.update()                 
                #Mise en place d'une musique de fond
    pygame.mixer.init()
    pygame.mixer.music.load("assets/Bramsito_-_Sale_mood_ft._Booba.mp3")
                            
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
                                    pygame.quit()
                                        
                                # Raffraichissement de l'ecran
                            pygame.display.flip()
                                                                
        
    pygame.quit()
    quit()

                



#Creation d'un objet de surface d'affichage menu
X=1300
Y=700



ecran1=pygame.display.set_mode((X,Y))

pygame.display.set_caption('MENU DU JEU')

ecran1.fill(noir)

pygame.draw.rect(ecran1,bleu,(450,350,400,50),3)
pygame.draw.rect(ecran1,bleu,(450,550,400,50),3)

font = pygame.font.SysFont('Wide Latin',32)

pygame.display.flip()

#**************************************************#
pygame.draw.rect(ecran1,violet,(0,0,1300,50))
pygame.draw.line(ecran1,violet,(500,0),(420,100),5)
pygame.draw.line(ecran1,violet,(0,100),(420,100),5)

menu= font.render('MAIN MENU',True,blanc)
ecran1.blit(menu,(10,60))


#Dessin de l'ellipse contenant puissance4
pygame.draw.ellipse(ecran1,bleu, (410,120,500,100))
titre_jeu= font.render('PUISSANCE 4',True,violet,blanc)
ecran1.blit(titre_jeu,(460,155))

#Dessin de l'ellipse contenant start
pygame.draw.ellipse(ecran1,bleu, (450,350,400,50))
text1=font.render('START',True,violet,blanc)

ecran1.blit(text1,(550,360))


#Dessin de l'ellipse contenant quit
pygame.draw.ellipse(ecran1,bleu, (450,550,400,50))
text2= font.render('EXIT',True,violet,blanc)
ecran1.blit(text2,(580,560))

#Comment entrer dans le jeu et comment quitter
information1=font.render("Press 's' to start",True,violet)
ecran1.blit(information1,(450,280))
information2=font.render("Press 'q' to quit",True,violet)
ecran1.blit(information2,(450,480))


#Mise à jour et affichage
pygame.display.flip()



begin=True
while begin:
    
    for event in pygame.event.get():
     if event.type==KEYDOWN and event.key ==K_s:
        
         pygame.quit()
         
         dessiner_plateau(tab)
         
         
     if (event.type==pygame.QUIT) or (event.type==KEYDOWN and event.key==K_q):
       
        pygame.quit()
        quit()
    pygame.display.update()
            