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
        
        Character()
        Position()
        j=0
        with open("laby.txt", 'r') as f:# we open our labyrinthe file 
            for line in f:# for each line
                for i in range(len(line)):
                    if line[i] == "m": 
                        self.laby_area[i,j]= "m"  # we create our dictionnary including coordinates of the wall
                    elif line[i] == "0":
                        self.laby_area[i,j]= "0" # we have our coordinates of our pathway
                        possible_object= (i,j)
                        self.free_cases.append(possible_object)
                    elif line[i] == "E":
                        self.laby_area[i,j]= "E" # we have our coordinates'wayout
                        self.victory=(i,j)
                    elif line[i]== "G":
                        self.laby_area[i,j]= "G"
                        gyver=(i,j)
                        self.mg.append(gyver) #we are saving Mac gyver first position
                j += 1
        self.draw_laby() # we print on the consol the labyrinthe           
        self.placing_object()
    def draw_laby(self, **laby_area):
        "function that draws the labyrinthe in the console"
        for i in range(15):
            for j in range(15):
                sys.stdout.write(self.laby_area[i,j]) # we draw the labyrinth in the consol
            sys.stdout.write("\n")  

        
    def placing_object(self):
        "function that places the 3 objects"
        self.object1= self.free_cases.pop(random.randint(0, len(self.free_cases)-1))
        self.object2= self.free_cases.pop(random.randint(0, len(self.free_cases)-1))
        self.object3= self.free_cases.pop(random.randint(0, len(self.free_cases)-1))
        a,b =self.object1
        c,d= self.object2
        e,f= self.object3
        self.laby_area[a,b]= "1"
        self.laby_area[c,d]= "2"
        self.laby_area[e,f]= "3"
        print("\n")
        self.draw_laby()
                
    def changing_character(self):
        "function that ask direction and place gyver to the new position"
        while self.ending_game()== False: #while the game is not terminated
            a,b=self.mg[0]
            event=input("veuillez entrer la direction") # we ask for the direction
            if event == "haut":
                Character.move_up(self) # we call the up moving method
                new_x, new_y= self.mg[0] #new coordinates of gyver under the condition no wall
            elif event == "bas":
                Character.move_down(self) # we call the up moving method
                new_x, new_y= self.mg[0]
            elif event == "droite":
                Character.move_right(self) # we call the up moving method
                new_x, new_y= self.mg[0]
            elif event == "gauche":
                Character.move_left(self) # we call the up moving method
                new_x, new_y= self.mg[0]
            Position.testing_position(self,a,b,new_x,new_y) # we test the movement
                
            if self.mg[0]== self.victory and len(self.object_picked_up)<3: # line that defines if we loose the game
                break
        if self.ending_game()== True:
            print("you have won")
        else:
            print("you have lost")                      
        
    def checking_coordinates(self,x, y):
        "function that checks coordinates"
        return self.laby_area[x,y]  # it returns what's in coordinates x,y 

    def picking_up(self,new_x, new_y):
        "function that picks up objects"
        if self.checking_coordinates(new_x, new_y)== "1":
            self.object_picked_up.append("object1")
            print("Great! You found object1")
        elif self.checking_coordinates(new_x, new_y)== "2":
             self.object_picked_up.append("object2")
             print("Great! You found object 2")
        elif self.checking_coordinates(new_x, new_y)== "3":
             self.object_picked_up.append("object3")
             print("Great! You found object 3")
   
    def ending_game(self):
        "function that checks if Mac gyver has won the game"
        if self.mg[0]== self.victory and len(self.object_picked_up)==3:   # gyver is at the exit and he has found the 3 objects
            return True # the function returns True
        else:
            return False # otherwise the function returns false
    
class Character():

    
    def __init(self):
        
        self.x=x
        self.y=y
        
    def move_right(self):  
        "function that move gyver to the right and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=x<=14 and 0<=(y+1)<=14: # we check if the movement stays in the layout
            self.mg[0]= x, (y+1) 
        else:
            print("you are out of the layout")    
        
    def move_left(self):
        "function that move gyver to the left and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=x<=14 and 0<=(y-1)<=14:
            self.mg[0]= x, (y-1)  
        else:
            print("you are out of the layout")  
        
    def move_up(self):
        "function that move up gyver and check if the movement is in the layout"
        x,y=self.mg[0]
        if 0<=(x-1)<=14 and 0<=y<=14:
            self.mg[0]= (x-1), y
        else:
            print("you are out of the layout")              
    
    def move_down(self):
        "function that move down gyver and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=(x+1)<=14 and 0<=y<=14:
            self.mg[0]= ((x+1), y)
        else:
            print("you are out of the layout")      
    
     
class Position():
    def __init__(self):
        Character()
        
    def testing_position(self, first_x, first_y, new_x, new_y):
        "we change coordinates if possible"
        if self.checking_coordinates(new_x,new_y)=="m":   # we check if there is a wall at the new possible position for Mac Gyver
            self.mg[0]= first_x, first_y
            print("Sorry, you can't walk through a wall")
        else:
            self.mg[0]= new_x, new_y
            self.laby_area[first_x, first_y]= "0"
            Labyrinthe.picking_up(self,new_x, new_y)
            self.laby_area[new_x, new_y]="G"
            self.draw_laby()
            self.ending_game()  # we test if the player finishes the game  

    
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
    
        
    
        

        

    
        

        

    
    
   

  
   

    

                              
    
   

                        
               

       

  
          
   

    

            
    

   



    






    

    







    

          
    

    

    
    

    










        



