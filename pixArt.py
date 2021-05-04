# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:53:43 2020

@author: admin
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dessine_scatter(nom, taille):
    #plt.figure(num=None, figsize=(6,6), dpi=10, facecolor='w', edgecolor='k')
    tab_couleurs = [(i/9,i/9,i/9) for i in range(10)]
    largeur = len(nom[0])
    hauteur = len(nom)
    plt.rcParams["figure.figsize"] = (largeur*taille/40,hauteur*taille/40)
    plt.rcParams["figure.dpi"] = 40.
    point_x = []
    point_y = []
    point_couleur = []
    for y in range(hauteur):
        for x in range(largeur):
            for ty in range(taille):
                for tx in range(taille):
                    point_x.append(x*taille+tx)
                    point_y.append(-y*taille-ty)
                    point_couleur.append(tab_couleurs[nom[y][x]])
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.grid(False)
    plt.scatter(point_x,point_y,c=point_couleur,s=1, marker='x')
    plt.show()
    
def dessine_rect(nom, taille):
    largeur = len(nom[0])
    hauteur = len(nom)
    plt.rcParams["figure.figsize"] = (largeur,hauteur)
    plt.rcParams["figure.dpi"] = taille
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.grid(False)
    tab_couleurs = [(i/9,i/9,0) for i in range(10)]
    rect = []
    dX = 1 / largeur
    dY = 1 / hauteur
    for y in range(hauteur):
        for x in range(largeur):
            coul=tab_couleurs[nom[y][x]]
            X = x / largeur
            Y = (hauteur - y) / hauteur
            rect.append(patches.Rectangle((X-dX,Y-dY),dX,dY,linewidth=1,facecolor=coul))
    for r in rect:
        ax.add_patch(r)
    plt.show()
    
def dessine(nom,taille):
    if taille <8:
        dessine_scatter(nom,taille)
    else:
        dessine_rect(nom,taille)
