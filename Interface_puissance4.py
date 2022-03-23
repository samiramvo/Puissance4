#coding:utf-8

from tkinter import image_types
from webbrowser import BackgroundBrowser
import pygame
from pygame.locals import*
import pygame.freetype
pygame.init()
#Differentes couleurs utilisables pour mon jeu
blanc=(255,255,255)
Gris=(185,198,191)
violet=(100,14,50)
vert=(0,255,0)
bleu=(0,0,255)
noir=(0,0,0)
bleu_ciel=(153,217,234)

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




ecran_menu=pygame.display.set_mode((800,400))
  
aspect=pygame.font.SysFont('Helvetic',20)
pygame.display.set_caption("*************MENU DU JEU*************")  

def menu():
    ciel_etoile=pygame.image.load("C://Users//Samira//Pictures//ciel_etoile.jpg").convert()
                    ecran_menu.blit(ciel_etoile,(0,0))
                    rect1=pygame.draw.rect(ciel_etoile)

  
def jeu():
 



        # Initialisation d'ne surface à afficher
        screen = pygame.display.set_mode((taille))

        paint= pygame.image.load("C://Users//Samira//Pictures//pexels-frank-cone-3279307.jpg").convert()
        screen.blit(paint,(0,0))

        #Mise en place de ma plateforme de jeu  
        pygame.draw.rect(paint,bleu,(0,cases,nb_colonne*cases,(nb_ligne+1)*cases))

        for col in range (nb_colonne):
            for lig in range(nb_ligne):
                cercle=pygame.draw.circle(paint,bleu_ciel,((col*cases+cases/2),(lig*cases+cases/2+cases)),rayon)



        pygame.draw.rect(paint,noir,(900,cases,nb_col*cases2,(nb_lig+1)*cases))
        pygame.draw.rect(paint,Gris,(900,cases,nb_col*cases2,(nb_lig+1)*cases),5)
        pygame.draw.line(paint,Gris,(1100,100),(1100,700),4)

        for nb1 in range(nb_col)  :
            for nb2 in range(nb_lig):
                cercle2=pygame.draw.circle(paint,Gris,((nb_col*29+29/2),(nb_lig*29+29/2+29)),rayon2)

                
            pygame.display.update()
            
            #Mise en place d'une musique de fond
            pygame.mixer.init()
            pygame.mixer.music.load("C://Users//Samira//Music//Bramsito_-_Sale_mood_ft._Booba.mp3")
            
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
                        
                
                        if (event.type==pygame.MOUSEBUTTONDOWN in cercle  ):
                            posx=event.pos[0]
                            posy=event.pos[y]
                            for col in range (nb_colonne):
                             for lig in range(nb_ligne): 
                                cercle.fill(vert)
                                
                                pygame.display.flip()
                        
                    # Raffraichissement de l'ecran
                        pygame.display.flip()
                    
                    # Mise à jour du jeu et affichage
                        pygame.display.update()
                        if event.type == pygame.QUIT or (event.type ==KEYDOWN and (event.key==K_q or event.key==K_SPACE)):
                         run = False


  
  
  
continuer = True

while continuer==True:
    for event in pygame.event.get():
    
     if continuer==True:
         menu()
         if(event.type==QUIT or (event.type ==KEYDOWN and (event.key==K_q))):
          pygame .quit()
    
     if event.type==KEYDOWN and event.key==K_e:
        continuer==False
        if continuer==False:
             jeu()
         
             pygame.quit()
             quit()
    
