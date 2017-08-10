#!/usr/bin/python3
# -*- coding: Utf-8 -*
from tkinter import *
import random

class Labyrinthe:
    WIDTH_CASE= 25
        
    
    def __init__ (self):
        self.zone_mur=[]
        self.zone_libre=[]
        self.depart=[]
        self.victoire=[]
        j=0
        with open("laby.txt", 'r') as f:# tu vas lire le fichier ligne par ligne
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
        self.zone_objet()
        


    def zone_objet(self):
        self.objet_1= self.zone_libre.pop(random.randint(0, len(self.zone_libre)-1))
        self.objet_2= self.zone_libre.pop(random.randint(0, len(self.zone_libre)-1))
        self.objet_3= self.zone_libre.pop(random.randint(0, len(self.zone_libre)-1))

    def draw_laby(self,frame):
        self.width_case= 25
        self.sprite= 15
        self.pic_wall= PhotoImage(file="mur.gif")
        self.pic_object1= PhotoImage(file="box.gif")
        self.pic_object2= PhotoImage(file="bottle.gif")
        self.pic_object3= PhotoImage(file="coin.gif")
        self.can= Canvas(frame,width= self.width_case * self.sprite, height= self.width_case * self.sprite, background= "white")
        for z in self.zone_mur:
            (x,y)= z
            self.can.create_image(x * self.width_case, y * self.width_case, anchor= NW, image= self.pic_wall)
            self.can.pack()
        (x,y)=self.objet_1
        self.can.create_image(x * self.width_case, y * self.width_case, anchor= NW, image= self.pic_object1)
        (x,y)=self.objet_2
        self.can.create_image(x * self.width_case, y * self.width_case, anchor= NW, image= self.pic_object2)
        (x,y)=self.objet_3
        self.can.create_image(x * self.width_case, y * self.width_case, anchor= NW, image= self.pic_object3)


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
            elif (x,y) in self.objet_1:
                print("objet 1")
            elif (x,y) in self.objet_2:
                print("objet 2")
            elif (x,y) in self.objet_3:
                print("Objet 3")
            else:
                print ("ya rien")
def main():
    laby=Labyrinthe()
    fenetre= Tk()
    laby.draw_laby(fenetre)
    fenetre.mainloop()
    

    

main()

