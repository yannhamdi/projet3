#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random

import sys

import pygame
from pygame.locals import *

pygame.init()
        
class Labyrinthe:
    WIDTH_CASE= 40
    SPRITE= 15
    def __init__ (self):
        "We initialize our labyrinthe"
        self.laby_area= {} #dictionnary that has all the coordinates of the labyrinthe
        self.mg=[] # mac gyver position
        self.free_cases =[]
        self.object_picked_up=[]
        self.wall= pygame.image.load("mur.gif").convert()
        self.pic_object1= pygame.image.load("bottle.gif").convert()
        self.pic_gyver= pygame.image.load("gyver.png").convert_alpha()
        self.bad_guy= pygame.image.load("bad.png").convert_alpha()
        self.pic_object2= pygame.image.load("box.gif").convert()
        self.pic_object3= pygame.image.load("coin.gif").convert()
        
        j=0
        with open("laby.txt", 'r') as f:# we open our labyrinthe file 
            for line in f:# for each line
                for i in range(len(line)):
                    if line[i] == "m": 
                        
                        self.laby_area[i,j]= "m"  # we create our dictionnary including coordinates of the wall
                    elif line[i] == "0":
                        
                        self.laby_area[i,j]= "0" # we have our coordinates of our pathway
                    elif line[i] == "E":
                        self.laby_area[i,j]= "E" # we have our coordinates'wayout
                        self.victory=(i,j)
                    elif line[i]== "G":
                        self.laby_area[i,j]= "G"

                        gyver=(i,j)
                        self.mg.append(gyver)

                j += 1
        self.draw_laby()
        self.placing_object()
        self.changing_character()

    
    def draw_laby(self, laby_area):
        "function that draws the labyrinthe in the console"

        for i in range(15):
            for j in range(15):
                sys.stdout.write(self.laby_area[i,j])

            sys.stdout.write("\n")    
        
    def placing_object(self):
        "function that places the 3 objects randomly"
        x=1 
        while x<=3:  
            i= random.randint(0,14)   #we pick up a random number between 0 and 14
            j= random.randint(0,14)
            if self.laby_area[i,j]== "0":
                self.laby_area[i,j]= str(x)
                x += 1
    
                
   
        
    def changing_character(self):
        "function that ask direction and place gyver to the new position"
        position=Position()
        while True:
            a, b = self.mg[0]
            event=input("veuillez entrer la direction") # we ask for the direction
            if event == "haut":
                new_x, new_y = (a - 1), b  # we are moving the coordinates towards the uppercase
                
            elif event == "bas":
                new_x, new_y = (a+ 1), b # we are moving the coordinates towards the bottom case
                
            elif event == "droite":
                new_x, new_y = a, (b + 1) # we are moving the coordinates toward the case on the right
               
                
            elif event == "gauche":
                new_x, new_y = a, (b - 1) # we are moving the coordinates towards the case on the left

            if new_x in range(15) and new_y in range(15):
                position.testing_position(self,a, b, new_x, new_y)
            else:
                print("sorry you are out of the layout")
            self.draw_laby()
            if self.mg[0]== self.victory:
                break
        if self.ending_game()== True:
            print("you have won")
        else:
            print("you have lost")

                
   
    def ending_game(self):
        "function that checks if Mac gyver has won the game or loose the game"
        if len(self.object_picked_up)==3:
            return True
        elif len(self.object_picked_up)<= 3:
            return False
    
    def moving_gyver(self, new_x, new_y):
        self.mg[0] = new_x, new_y
             

class Position():

    def checking_coordinates(self,labyrinthe, x,y):
        "function thats checks coordinates"
        return labyrinthe.laby_area[x,y] 
     
    def picking_up(self,labyrinthe, new_x, new_y):
        "function that picks up objects"
        if self.checking_coordinates(labyrinthe,new_x, new_y)== "1":
            labyrinthe.object_picked_up.append("object1")
            print("Great! You found object1")
        elif self.checking_coordinates(labyrinthe,new_x, new_y)== "2":
            labyrinthe.object_picked_up.append("object2")
            print("Great! You found object 2")
        elif self.checking_coordinates(labyrinthe,new_x, new_y)== "3":
            labyrinthe.object_picked_up.append("object3")
            print("Great! You found object 3")   
    
    def testing_position(self, labyrinthe, a, b, new_x, new_y):
        "function that tests the mouvement"
        if self.checking_coordinates(labyrinthe, new_x, new_y)== "m":  #we check if there is a wall
            labyrinthe.mg[0]= a, b
            print("sorry you cant walk through a wall")
        else:
            labyrinthe.moving_gyver(new_x, new_y)
            self.picking_up(labyrinthe,new_x,new_y)
            print(labyrinthe.object_picked_up)
            labyrinthe.laby_area[a, b]= "0"
            labyrinthe.laby_area[new_x, new_y]="G"
        

    
def main():
    
    
    pygame.init()
    fenetre= pygame.display.set_mode((Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE, Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE ))
    laby=Labyrinthe()
    macgyver=Character()
    fond= pygame.image.load("fond.jpg").convert()
    fenetre.blit(fond,(0,0))
    for i in range(15):
        for j in range(15):
            if laby.checking_coordinates(i,j)== "m":
                x= i*40
                y= j*40
                fenetre.blit(laby.wall, (x,y))
            elif laby.checking_coordinates(i,j)== "1":
                x= i*40
                y= j*40
                fenetre.blit(laby.pic_object1, (x,y))
            elif laby.checking_coordinates(i,j)== "G":
                x= i*40
                y= j*40
                fenetre.blit(laby.pic_gyver, (x,y))
            elif laby.checking_coordinates(i,j)== "2":
            	x= i*40
            	y= j*40
            	fenetre.blit(laby.pic_object2, (x, y))
            elif laby.checking_coordinates(i,j)== "E":
            	x= i* Labyrinthe.WIDTH_CASE
            	y= j * Labyrinthe.WIDTH_CASE
            	fenetre.blit(laby.bad_guy, (x,y))
            elif laby.checking_coordinates(i,j)== "3":
            	x= i* Labyrinthe.WIDTH_CASE
            	y= j* Labyrinthe.WIDTH_CASE
            	fenetre.blit(laby.pic_object3, (x,y))
            
        
    pygame.display.flip()
    continuer=1
    while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer = 0
            elif event.type== K_RIGHT:
                macgyver.move_right()
            elif event.type == K_LEFT:
                macgyver.move_left()
            elif event.type== K_UP:
                macgyver.move_up()
            elif event.type== K_DOWN:
                macgyver.move_down()

        continue
    

    laby.placing_object()
    position=Position()
    macgyver= Character()
    laby.changing_character()

    
main()
    
        
    
        

        

    
        

        

    
    
   

 
       
    













    

                              
    
   

                        
               

       

  
          
   

    

            
    

   



    






    

    







    

          
    

    

    
    

    










        



