
from email.mime import image
from msilib.schema import Font
from selectors import EVENT_READ
from turtle import _Screen, update
from winreg import KEY_ALL_ACCESS
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
import math
import random
import time






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

#Creation d'un tableau d'entier
tab=zeros((6,7), int)

def create_board(tab):
     tab = np.zeros((nb_ligne,nb_colonne))

def afficher_tableau(tab):
    
    print(np.flip(tab,0))
    print("\n\n")
    if coup_gagnant(tab,1):
        print("L'IA a gagné")
        run=False
        
    if  coup_gagnant(tab,2):
        print("Le joueur a gagné")
        run=False
    if partie_nulle(tab):
        print("Partie nulle!!")
        run=False
    

def emplacement_valide(tab,colonne):
    if tab[nb_ligne-1][colonne]==0:
      return True
    else:
     return False

def trouver_Ligne_Vide(tab,colonne):
 for r in range(nb_ligne):
  if tab[r][colonne]==0:
   return r

def lacher_jeton(tab, ligne, colonne,X):
    tab[ligne][colonne] = X

def coup_gagnant(tab,X):
    #Possibilités de gagner horizontalement
    for col in range (nb_colonne-3):
     for lig in range (nb_lig):
       if tab[lig][col]==X and tab[lig][col+1]==X and tab[lig][col+2]==X and tab[lig][col+3]==X:
         return True

    #Possibilites de gagner verticalement
    for col in range (nb_colonne):
     for lig in range (nb_ligne-3):
      if tab[lig][col]==X and tab[lig+1][col]==X and tab[lig+2][col]==X and tab[lig+3][col]==X:
        return True

    #Possibilites de gagner diagonalement vers la droite
    for col in range (nb_colonne-3):
     for lig in range (nb_ligne-3):
        if tab[lig][col]== X and tab[lig+1][col+1]== X and tab[lig+2][col+2]== X and tab[lig+3][col+3]== X:
          return True
    
    #Possibilites de gagner diagonalement vers la gauche
    for col in range (nb_colonne-3):
     for lig in range (3,nb_ligne):
      if tab[lig][col]==X and tab[lig-1][col+1]==X and tab[lig-2][col+2]==X and tab[lig-3][col+3]== X:
         return True

def partie_nulle(tab):
     for col in range (nb_colonne):
       for lig in range(nb_ligne): 
          if tab[lig][col] == 0:
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

font = pygame.font.SysFont('Wide Latin',52)
               

#================================================================================================#

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
    cercle1=pygame.draw.circle(paint,bleu_fonce,(880,450),70)
    cercle2=pygame.draw.circle(paint,blanc,(1150,450 ),70)
    nb_pions1=font.render("21", True, blanc)
    nb_pions2=font.render("21", True, bleu_fonce)
    paint.blit(nb_pions1, [830,430])
    paint.blit(nb_pions2, [1100, 430])
  

                                      
      

    create_board(tab)

                 
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
    clock=pygame.time.Clock()

                        
                #Deplacements de la souris

    x=0
    y=0
    screen.blit(paint, (x,y))
     

    tour=0
    run = True
    while run:
        for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                                
                                
                                screen_black=pygame.draw.rect(paint,noir,(0,0,largeur-600,(cases))) 
                                posx = event.pos[0]
                                if tour==0:
                                  if posx<650:
                                  
                                   colonne = int (math.floor(posx/(cases)))       
                                   
                                   if emplacement_valide(tab,colonne):
                                      ligne = trouver_Ligne_Vide(tab,colonne)
                                    
                                      lacher_jeton(tab, ligne, colonne,2)
                                      if tab[ligne][colonne] == 2: 
                                                
                                                        pygame.draw.circle(screen,blanc,((colonne*cases+cases/2),hauteur- (ligne*cases+cases/2)),rayon)
                                      
                                
                                      counteur=21
                                      text="21"
                                      b=1
                                      if tab[ligne][colonne]==2:
                                            
                                                
                                                        cercle1=pygame.draw.circle(paint,bleu_fonce,(880,450),70)
                                                        counteur=counteur-b      
                                                        text=str(counteur)
                                                    
                                                    
                                                        nb_pions1=font.render(text, True, blanc)
                                                            
                                                        screen.blit(nb_pions1, [830,430])
                                                        
                                                
                                      b=b+1
                                      pygame.display.flip()
                                                
                                    
                                      
                                      create_board(tab)
                                      afficher_tableau(tab)
                                   if coup_gagnant(tab,2):
                                        pygame.draw.circle(screen,blanc,(50,50),rayon)
                                        texte_image = font.render("Le joueur a gagné", True, blanc)
                                        screen.blit(texte_image, [100, 30])
                                      
                                        run=False 
                                        
                                      
                                                            
                                
                                
                                  
                                tour==1
                                
                                if emplacement_valide(tab,col):
                                         
                                          ligne2 = trouver_Ligne_Vide(tab,col)
                                          
                                          lacher_jeton(tab, ligne2, col,1)
                                           
                                         
                                          counteur1=21
                                          text1="21"
                                          a=1
                                       
                                          if tab[ligne2][col] == 1 :
                                                        
                                                      pygame.draw.circle(screen,bleu_fonce,((col*cases+cases/2),hauteur-(ligne2*cases+cases/2)),rayon)
                                                
                                                      cercle2=pygame.draw.circle(paint,blanc,(1150,450 ),70)
                                                    
                                                      counteur1=counteur1-a       
                                                      text1=str(counteur1)
                                                        
                                                        
                                                      nb_pions2=font.render(text1, True, bleu_fonce)
                                                                    
                                                    
                                                      screen.blit(nb_pions2, [1100,430])
                                          a=a+1
                                                    
                                                
                                          pygame.display.flip()
                                             
                                          
                                          create_board(tab)
                                          afficher_tableau(tab) 
                                if coup_gagnant(tab,1):
                                            
                                            pygame.draw.circle(screen,bleu_fonce,(50,50),rayon)
                                            texte_image = font.render("L'IA a gagné", True, bleu_fonce)
                                            screen.blit(texte_image, [100, 30])
                                            
                                            run=False
                                if partie_nulle(tab):
                                     pygame.draw.circle(screen,bleu_ciel,(50,50),rayon)
                                     texte_image = font.render("PARTIE NULLE!!", True, bleu_ciel)
                                     screen.blit(texte_image, [100, 30])
                                     run=False
                                    
                                           
                                            
                                                                                              
                                                                        
                pygame.display.flip()
                                
                                      
                if event.type == pygame.MOUSEMOTION:
                                 screen_black=pygame.draw.rect(screen,noir,(0,0,largeur-600,cases)) 
                                 posx = event.pos[0]
                                
                                 if tour==0:
                                     if posx<650:
                                      pygame.draw.circle(screen,blanc,(posx,(cases/2)),rayon)
                                 if coup_gagnant(tab,1) :
                                          pygame.draw.circle(screen,blanc,(50,50),rayon)
                                          texte_image = font.render("Le joueur a gagné", True, blanc)
                                          screen.blit(texte_image, [100, 30])
                                          
                                          
                                 if coup_gagnant(tab,2):
                                         pygame.draw.circle(screen,bleu_fonce,(50,50),rayon)
                                         texte_image = font.render("L'IA a gagné", True, bleu_fonce)
                                         screen.blit(texte_image, [100, 30])
                                         
                                
                                         pygame.display.update()
               
                                    
                if event.type == pygame.QUIT or (event.type ==KEYDOWN and (event.key==K_q or event.key==K_SPACE)):
                                    pygame.quit()
                                        
                                # Raffraichissement de l'ecran
    pygame.display.flip()
                                                                
        
    pygame.quit()
    quit()
#################################################################################################""
def dessiner_plateau2(tab):
       
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
    cercle1=pygame.draw.circle(paint,bleu_fonce,(880,450),70)
    cercle2=pygame.draw.circle(paint,blanc,(1150,450 ),70)
    nb_pions1=font.render("21", True, blanc)
    nb_pions2=font.render("21", True, bleu_fonce)
    paint.blit(nb_pions1, [830,430])
    paint.blit(nb_pions2, [1100, 430])
  

                                      
      

    create_board(tab)

                 
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
    clock=pygame.time.Clock()

                        
                #Deplacements de la souris

    x=0
    y=0
    screen.blit(paint, (x,y))
     

    tour=0
    run = True
    while run:
        for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                                
                           
                                screen_black=pygame.draw.rect(paint,noir,(0,0,largeur-600,(cases))) 
                                posx = event.pos[0]
                               
                                
                                
                                    
                                if tour==0:
                                  if posx<650:
                                      
                                
                                   colonne = int (math.floor(posx/(cases)))       
                                   
                                   if emplacement_valide(tab,colonne):
                                      ligne = trouver_Ligne_Vide(tab,colonne)
                                    
                                      lacher_jeton(tab, ligne, colonne,2)
                                      if tab[ligne][colonne] == 2: 
                                                
                                                        pygame.draw.circle(screen,blanc,((colonne*cases+cases/2),hauteur- (ligne*cases+cases/2)),rayon)
                                      
                                
                                      counteur=21
                                      text="21"
                                      b=1
                                      if tab[ligne][colonne]==2:
                                            
                                                
                                                        cercle1=pygame.draw.circle(paint,bleu_fonce,(880,450),70)
                                                        counteur=counteur-b      
                                                        text=str(counteur)
                                                    
                                                    
                                                        nb_pions1=font.render(text, True, blanc)
                                                            
                                                        screen.blit(nb_pions1, [830,430])
                                                        
                                                
                                      b=b+1
                                      pygame.display.flip()
                                                
                                    
                                      
                                      create_board(tab)
                                      afficher_tableau(tab)
                                   if coup_gagnant(tab,2):
                                        pygame.draw.circle(screen,blanc,(50,50),rayon)
                                        texte_image = font.render("Le joueur1 a gagné", True, blanc)
                                        screen.blit(texte_image, [100, 30])
                                      
                                        run=False 
                                        
                                      
                                                            
                                
                                
                                  
                                   tour=1
                                   if tour==1:
                                      if posx<650:
                                        colonne = int (math.floor(posx/(cases)))  
                                        
                                        if emplacement_valide(tab,colonne):
                                                
                                                ligne2 = trouver_Ligne_Vide(tab,colonne)
                                                
                                                lacher_jeton(tab, ligne2, colonne,1)
                                                
                                                
                                                counteur1=21
                                                text1="21"
                                                a=1
                                            
                                                if tab[ligne2][colonne] == 1 :
                                                                
                                                            pygame.draw.circle(screen,bleu_fonce,((colonne*cases+cases/2),hauteur-(ligne2*cases+cases/2)),rayon)
                                                        
                                                            cercle2=pygame.draw.circle(paint,blanc,(1150,450 ),70)
                                                            
                                                            counteur1=counteur1-a       
                                                            text1=str(counteur1)
                                                                
                                                                
                                                            nb_pions2=font.render(text1, True, bleu_fonce)
                                                                            
                                                            
                                                            screen.blit(nb_pions2, [1100,430])
                                                a=a+1
                                                            
                                                        
                                                pygame.display.flip()
                                                    
                                                
                                                create_board(tab)
                                                afficher_tableau(tab) 
                                        if coup_gagnant(tab,1):
                                                    
                                                    pygame.draw.circle(screen,bleu_fonce,(50,50),rayon)
                                                    texte_image = font.render("Le joueur2 a gagné", True, bleu_fonce)
                                                    screen.blit(texte_image, [100, 30])
                                                    
                                                    run=False
                                        if partie_nulle(tab):
                                            pygame.draw.circle(screen,bleu_ciel,(50,50),rayon)
                                            texte_image = font.render("PARTIE NULLE!!", True, bleu_ciel)
                                            screen.blit(texte_image, [100, 30])
                                            run=False
                                        
                                            
                                                
                                                                                                
                                                                        
                pygame.display.flip()
                                
                                
                if event.type == pygame.MOUSEMOTION:
                                 screen_black=pygame.draw.rect(screen,noir,(0,0,largeur-600,cases)) 
                                 posx = event.pos[0]
                                 if posx<650:
                                      
                                     if tour==0:
                                       
                                         pygame.draw.circle(screen,blanc,(posx,(cases/2)),rayon)
                                         
                                     
                                     
                                     if tour==1:
                                        
                                            pygame.draw.circle(screen,bleu_fonce,(posx,(cases/2)),rayon)
                                          
                                 
                                 if coup_gagnant(tab,1) :
                                          pygame.draw.circle(screen,blanc,(50,50),rayon)
                                          texte_image = font.render("Le joueur2 a gagné", True, blanc)
                                          screen.blit(texte_image, [100, 30])
                                          
                                          
                                 if coup_gagnant(tab,2):
                                         pygame.draw.circle(screen,bleu_fonce,(50,50),rayon)
                                         texte_image = font.render("Le joueur1 a gagné", True, bleu_fonce)
                                         screen.blit(texte_image, [100, 30])
                                         
                                
                                         pygame.display.update()
               
                                    
                if event.type == pygame.QUIT or (event.type ==KEYDOWN and (event.key==K_q or event.key==K_SPACE)):
                                    pygame.quit()
                                        
                                # Raffraichissement de l'ecran
    pygame.display.flip()
                                                                
        
    pygame.quit()
    quit()




##################################################################################################

def options():
    #Creation de l'option jeu
                     
                
                     ecran2=pygame.display.set_mode((1300,700))
                     
                     pygame.display.set_caption('OPTIONS DE JEU')
                     ecran2.fill(noir)

                     pygame.draw.rect(ecran2,bleu,(410,350,450,100),3)
                     pygame.draw.rect(ecran2,bleu,(410,550,450,100),3)

                     font = pygame.font.SysFont('Wide Latin',22)
                     myfont = pygame.font.SysFont('Wide Latin',32)


                     pygame.display.flip()

                    #**************************************************#
                     pygame.draw.rect(ecran2,violet,(0,0,1300,50))
                     
                     pygame.draw.line(ecran2,violet,(500,0),(420,100),5)
                     pygame.draw.line(ecran2,violet,(0,100),(420,100),5)


                     option= myfont.render('OPTIONS',True,blanc)
                     ecran2.blit(option,(10,60))


                    #Dessin de l'ellipse contenant jeu
                     pygame.draw.ellipse(ecran2,bleu, (410,120,500,100))
                     jeu= myfont.render('JEU',True,violet,blanc)
                     ecran2.blit(jeu,(600,155))

                    #Dessin de l'ellipse contenant joueur VS IA
                     pygame.draw.ellipse(ecran2,bleu, (410,350,450,100))
                     text1=font.render('JoueurVSIA',True,violet,blanc)

                     ecran2.blit(text1,(530,390))


                    #Dessin de l'ellipse contenant joueur VS joueur
                     pygame.draw.ellipse(ecran2,bleu, (410,550,450,100))
                     text2= font.render('JoueurVSJoueur',True,violet,blanc)
                     ecran2.blit(text2,(480,590))

                    #Comment entrer dans le jeu et comment quitter
                     information1=font.render("Press 1:",True,violet)
                     ecran2.blit(information1,(450,280))
                     information2=font.render("Press 2:",True,violet)
                     ecran2.blit(information2,(450,480))
                     while True:
                         for event in pygame.event.get():
                             if event.type==KEYDOWN and event.key==K_1:
                                 #Mise à jour et affichage
                                

                            
                                 dessiner_plateau(tab)
                             pygame.display.flip()
                             if event.type==KEYDOWN and event.key==K_2:
                                
                                dessiner_plateau2(tab)
                             pygame.display.flip()
                             if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_SPACE):
                                 pygame.quit()
                                 quit()    

#==========================================================================================#
def menu():
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
        information2=font.render("Press 'e' to quit",True,violet)
        ecran1.blit(information2,(450,480))


        #Mise à jour et affichage
        pygame.display.flip()



        begin=True
        while begin:
            
            for event in pygame.event.get():
             if event.type==pygame.MOUSEBUTTONDOWN:
                 x1=event.pos[0]
                 y1=event.pos[1]
                 if 450<=x1<=850 and 350<=y1<=400:
                     pygame.display.quit()
                     
                     options()

                    
             if event.type==pygame.MOUSEMOTION:
                     x1=event.pos[0]
                     y1=event.pos[1]
                     if 450<=x1<=850 and 350<=y1<=400:
                         text1=font.render('START',True,violet,vert)

                         ecran1.blit(text1,(550,360))
                         pygame.display.update()
                     else:    
                         text1=font.render('START',True,violet,blanc)

                         ecran1.blit(text1,(550,360))
                         pygame.display.update()
                         
             if event.type==pygame.MOUSEBUTTONDOWN:
                     x1=event.pos[0]
                     y1=event.pos[1]
                     if 450<=x1<=850 and 550<=y1<=600:
                        pygame.quit()
                        quit()
                    
                     
             if event.type==pygame.MOUSEMOTION:
                     x1=event.pos[0]
                     y1=event.pos[1]
                     if 450<=x1<=850 and 550<=y1<=600:
                         text2= font.render('EXIT',True,violet,jaune)
                         ecran1.blit(text2,(580,560))
                         pygame.display.update()
                     else:    
                         text2= font.render('EXIT',True,violet,blanc)
                         ecran1.blit(text2,(580,560))
                         pygame.display.update()                        
             if event.type==KEYDOWN and event.key ==K_s:
                    
                pygame.display.quit()
                
                dessiner_plateau(tab)
                
                
             if (event.type==pygame.QUIT) or (event.type==KEYDOWN and event.key==K_e):
                    
                        pygame.quit()
                        quit()
             pygame.display.flip()

             
            
            
                        

#===========================================================================================#
pygame.key.get_pressed()
pygame.mouse.get_pressed()
pygame.event.wait()

souris=pygame.mouse.set_cursor(*pygame.cursors.tri_left)


animation=pygame.display.set_mode((1300,700))

pygame.display.set_caption("Animations")
paint= pygame.image.load("assets/ciel_etoile.jpg").convert()
animation.blit(paint,(0,0))

paint1= pygame.image.load("assets/puissance4.jpg").convert()
animation.blit(paint1,(100,100))

pygame.draw.ellipse(animation,noir, (450,450,400,150))

font = pygame.font.SysFont('Wide Latin',52)

text2= font.render('JOUER',True,violet,noir)
animation.blit(text2,(480,500))


pygame.display.flip()
while True:
 for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==KEYDOWN and event.key==K_q):
           pygame.quit()
        
        if event.type==pygame.MOUSEMOTION:
            x=event.pos[0]
            y=event.pos[1]
            if 450<=x<=850 and 450<=y<=600:  
           
                text2= font.render('JOUER',True,vert,noir)
                animation.blit(text2,(480,500)) 
                pygame.display.update()
                
            else:
                text2= font.render('JOUER',True,violet,noir)
                animation.blit(text2,(480,500)) 
                pygame.display.update()
        
        
        
        if event.type==pygame.MOUSEBUTTONDOWN:
         
            x=event.pos[0]
            y=event.pos[1]
            if 450<=x<=850 and 450<=y<=600:
                time.sleep(0.5)
                menu()  
                pygame.display.flip() 
        

        
                    

        if event.type==KEYDOWN and event.key==K_SPACE:
            menu()  
            pygame.display.flip() 


