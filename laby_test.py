#!/usr/bin/python3
# -*- coding: Utf-8 -*
from tkinter import *

class Labyrinthe:
    WIDTH_CASE= 25
        
    
    def __init__ (self):
        self.zone_mur=[]
        self.zone_libre=[]
        self.depart=[]
        self.victoire=[]
        j=0
        with open("laby_test.txt", 'r') as f:# tu vas lire le fichier ligne par ligne
            for line in f:# tu as ta ligne => line
                for i in range(len(line)):# tu as le nombre de lettre de ta ligne len(line)
                    if line[i] == "m":  # tu as la lettre
                        mur=(i,j)  
                        self.zone_mur.append(mur) 
                    elif line[i] == "0":
                        vide=(i,j)
                        self.zone_libre.append(vide)
                    elif line[i] == "E":
                        sortie=(i,j)
                        self.victoire.append(sortie)
                    elif line[i]== "G":
                        start=(i,j)
                        self.depart.append(start)
                j += 1
        
    def zone(self):
        x=int(input("veuillez entrer x"))
        y=int(input("veuillez entrer y"))
        if (x,y) in self.victoire:
            print("c'est la sortie")
        elif (x,y) in self.zone_mur:
            print("c'est un mur")
        elif (x,y) in self.zone_libre:
            print("c'est libre")
        elif (x,y) in self.depart:
            print("c'est le depart")
        else:
            print ("ya rien")
def main():
    laby=Labyrinthe()
    laby.zone()
main()

