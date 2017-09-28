#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random

import sys

import pygame
from pygame.locals import *

import position

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
        self.changing()

    
    def draw_laby(self):
        "function that draws the labyrinthe in the console"
        fenetre= pygame.display.set_mode((Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE, Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE ))
        self.wall= pygame.image.load("mur.gif").convert()
        self.pic_object1= pygame.image.load("bottle.gif").convert()
        self.pic_gyver= pygame.image.load("gyver.png").convert_alpha()
        self.bad_guy= pygame.image.load("bad.png").convert_alpha()
        self.pic_object2= pygame.image.load("box.gif").convert()
        self.pic_object3= pygame.image.load("coin.gif").convert()
        pygame.init()
        position = Position()
        fond= pygame.image.load("fond.jpg").convert()
        fenetre.blit(fond,(0,0))
        for i in range(15):
            for j in range(15):
                if position.checking_coordinates(self,i,j)== "m":
                    x= i* Labyrinthe.WIDTH_CASE
                    y= j* Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.wall, (x,y))
                elif position.checking_coordinates(self,i,j)== "1":
                    x = i * Labyrinthe.WIDTH_CASE
                    y= j * Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.pic_object1, (x,y))
                elif position.checking_coordinates(self,i,j)== "G":
                    x= i * Labyrinthe.WIDTH_CASE
                    y= j * Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.pic_gyver, (x,y))
                elif position.checking_coordinates(self,i,j)== "2":
                    x= i * Labyrinthe.WIDTH_CASE
                    y= j * Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.pic_object2, (x, y))
                elif position.checking_coordinates(self,i,j)== "E":
                    x= i* Labyrinthe.WIDTH_CASE
                    y= j * Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.bad_guy, (x,y))
                elif position.checking_coordinates(self,i,j)== "3":
                    x= i* Labyrinthe.WIDTH_CASE
                    y= j* Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.pic_object3, (x,y))
        pygame.display.flip()
    
    def placing_object(self):
        "function that places the 3 objects randomly"
        x=1 
        while x<=3:  
            i= random.randint(0,14)   #we pick up a random number between 0 and 14 in order to pick up a random column
            j= random.randint(0,14)   # random line
            if self.laby_area[i,j]== "0":   # if the coordinate picked up is free
                self.laby_area[i,j]= str(x) # we save our object
                x += 1
    
    def changing(self):
        position=Position()
        while True:
            a, b = self.mg[0]  # we save a and b as the actual coordinate of macgyver
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # if the player presses echap we stop the game
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        break
                    # if the player presses the keydown we call the function to test the position at the bottom case    
                    elif event.key == K_DOWN:
                         new_x, new_y = a, (b + 1)
                        
                    # if the player presses the keyup we will be trying the coordinates at the upper case
                    elif event.key == K_UP:
                        new_x, new_y = a, (b - 1)
                        
                    # if the player presses the keyleft 
                    elif event.key == K_LEFT:
                        
                        new_x, new_y = (a - 1), b 
                    # if the player presses the keyright
                    elif event.key == K_RIGHT:
                        new_x, new_y = (a+ 1), b
                    # we check if the movement is inside the labyrinth   
                    if new_x in range(15) and new_y in range(15):
                        # if it is then we call our method which test the mouvement
                        position.testing_position(self,a, b, new_x, new_y)
                    else:
                        print("sorry you are out of the layout")
                    self.draw_laby() # we call up the method to upddate our labyrinthe
            # if macgyver arrives at the exit then we stop the loop and test if we won or loose
            if self.mg[0]== self.victory:
                break
        if self.ending_game()== True:
            print("you have won")
        else:
            print("you have lost")

                
   
    def ending_game(self):
        "function that checks if Mac gyver has won the game or loose the game"
        # mac gyver has arrived at the exit we check if he has the 3 objects
        if len(self.object_picked_up)==3:
            return True
        # we check if he hasnt got the 3 objects and then he has lost
        elif len(self.object_picked_up)<= 3:
            return False
    
    def moving_gyver(self, new_x, new_y):
        "function that gives the new coordinates of macgyver"
        self.mg[0] = new_x, new_y
             

class Position():

    def checking_coordinates(self,labyrinthe, x,y):
        "function thats checks coordinates"
        # we return what has the coordinates provided
        return labyrinthe.laby_area[x,y] 
     
    def picking_up(self,labyrinthe, new_x, new_y):
        "function that picks up objects"
        if self.checking_coordinates(labyrinthe,new_x, new_y)== "1":
            # we add to the list object 1
            labyrinthe.object_picked_up.append("object1")
            print("Great! You found object1")
        elif self.checking_coordinates(labyrinthe,new_x, new_y)== "2":
            # we add to the list object 2
            labyrinthe.object_picked_up.append("object2")
            print("Great! You found object 2")
        elif self.checking_coordinates(labyrinthe,new_x, new_y)== "3":
            # we add to the list object 3
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
            labyrinthe.draw_laby()




if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()