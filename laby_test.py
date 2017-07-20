#!/usr/bin/python3
# -*- coding: Utf-8 -*
from tkinter import *



fen = Tk()
can = Canvas(fen, width=25*15, height=25*15, background="white")
############################"#########" 
ton_image = PhotoImage(file="mur.gif") 

longueur_case = 25
j=0# sera le num de ligne
with open("laby.txt", 'r') as f:# tu vas lire le fichier ligne par ligne
   for line in f:# tu as ta ligne => line
        for i in range(len(line)):# tu as le nombre de lettre de ta ligne len(line)
            
            if line[i] == "m":  # tu as la lettre
                can.create_image(i * longueur_case, j * longueur_case, anchor=NW, image= ton_image)   
        j += 1

can.pack(padx=5, pady=5)
fen.mainloop()

