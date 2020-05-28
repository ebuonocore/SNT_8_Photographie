# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:53:43 2020

@author: admin
"""
from tkinter import *
import matplotlib.image as mpimg
import numpy as np
from tkinter import *

def dessine(tableau, cote):
    # Création du widget principal ("maître") :
    fenetre = Tk()
    d = 10 # Marges autour de l'image
    # création des widgets "esclaves" :
    hauteur_canevas = (len(tableau)+1)*cote+d*2
    largeur_canevas = (len(tableau[0])+1)*cote+d*2
    can = Canvas(fenetre,bg='white',height=hauteur_canevas,width=largeur_canevas)
    for ligne in range(len(tableau)):
        for colonne in range(len(tableau[0])):
            R,V,B = codeGris_pixel(tableau,colonne,ligne)
            colorval = "#%02x%02x%02x" % (R*17, V*17, B*17)
            #print('colorval:',colorval)
            can.create_rectangle(colonne*cote+d,ligne*cote+d,(colonne+1)*cote+d, (ligne+1)*cote+d, fill = colorval, width =0) 
    can.pack()
    fenetre.mainloop()
    
def codeGris_pixel(tableau,x,y):
    niveau = tableau[y][x]
    if type(niveau)!=int:
        niveau = 0
    if niveau <0:
        niveau = 0
    if niveau >9:
        niveau = 9
    R = niveau*15//9
    return R,R,R
                
     