#!/usr/bin/python3
# -*- coding: Utf-8 -*
from tkinter import *

def main():
    tableau = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
           [1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    fen = Tk()
    can = Canvas(fen, width=250, height=250, background="white")
    ############################"#########" 
    ton_image = PhotoImage(file="mur.png") #il faut la creer comme ca
    #######################################
    longueur_case = 250 / len(tableau) 
    for i in range(10):
        for j in range(10):
            if(tableau[i][j] == 1):
                can.create_image(i * longueur_case, j *
                                 longueur_case, anchor=NW, image=ton_image)# tu avais cree ton image comme un rectangle
            # else:
                #   can.create_rectangle(i*longueur_case,j*longueur_case,(i+1)*longueur_case,(j+1)*longueur_case, fill="black", outline="white")
    can.pack()
    fen.mainloop()

if __name__ == '__main__':
    main()