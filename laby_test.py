#!/usr/bin/python3
# -*- coding: Utf-8 -*
from tkinter import *

class Labyrinthe:
    WIDTH_CASE= 25
    ZONE_MUR= []
    ZONE_LIBRE= []
    EXIT=[]

    def __init__(self, longueur, largeur):
	    self.longueur= longueur
	    self.largeur= largeur
        

    def initialize_laby(self):
        fen = Tk()
        can = Canvas(fen, width= Labyrinthe.WIDTH_CASE * self.longueur, height= Labyrinthe.WIDTH_CASE * self.largeur, background="white")
        ton_image = PhotoImage(file="mur.gif")   
        j=0
        with open("laby.txt", 'r') as f:# tu vas lire le fichier ligne par ligne
            for line in f:# tu as ta ligne => line
                for i in range(len(line)):# tu as le nombre de lettre de ta ligne len(line)
                    if line[i] == "m":  # tu as la lettre
                        can.create_image(i * Labyrinthe.WIDTH_CASE, j * Labyrinthe.WIDTH_CASE, anchor=NW, image= ton_image) 
                        mur=(i, j)
                        self.ZONE_MUR.append(mur)   
                    elif line[i] == "0":
                        vide=(i,j)
                        self.ZONE_LIBRE.append(vide)
                    elif line[i] == "E":
                        sortie=(i,j)
                        self.EXIT.append(sortie)
                j += 1
        can.pack(padx=5, pady=5)
        fen.mainloop()

def main():
    laby= Labyrinthe(15,15)
    laby.initialize_laby()

main()


