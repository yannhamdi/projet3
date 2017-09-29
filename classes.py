#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random


import pygame

from pygame.locals import *


class Labyrinthe:
    "the class that manages our labyrinthe"
    # the size of our case
    WIDTH_CASE= 40
    # the number of sprite
    SPRITE= 15
    def __init__ (self):
        "We initialize our labyrinthe"
        self.laby_area= {} #dictionnary that has all the coordinates of the labyrinthe
        self.mg=[] # mac gyver position
        # the bag that contains the object picked up
        self.object_picked_up=[]
       
        
        j=0
        with open("laby.txt", 'r') as file_laby:# we open our labyrinthe file 
            for line in file_laby:# for each line
                for i in range(len(line)):
                    if line[i] == "m": 
                        
                        self.laby_area[i, j]= "m"  # we create our dictionnary including coordinates of the wall
                    elif line[i] == "0":
                        
                        self.laby_area[i, j]= "0" # we have our coordinates of our pathway
                    elif line[i] == "E":
                        self.laby_area[i, j]= "E" # we have our coordinates'wayout
                        self.victory=(i, j)
                    elif line[i]== "G":
                        self.laby_area[i, j]= "G"

                        gyver=(i, j)
                        self.mg.append(gyver)

                j += 1
        # we call up our method placing object to place the 3 objects
        self.placing_object()
        # we draw the labyrinthe
        self.draw_laby()
        # we call up the loop to start the game
        self.changing()

    def draw_laby(self):
        "function that draws the labyrinthe in the console"
        # we create the labyrinthe frame
        fenetre= pygame.display.set_mode((Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE, Labyrinthe.WIDTH_CASE* Labyrinthe.SPRITE ))
        # we initialize our pictures for the game
        self.wall= pygame.image.load("mur.gif").convert()
        self.pic_object1= pygame.image.load("bottle.gif").convert()
        self.pic_gyver= pygame.image.load("gyver.png").convert_alpha()
        self.bad_guy= pygame.image.load("bad.png").convert_alpha()
        self.pic_object2= pygame.image.load("box.gif").convert()
        self.pic_object3= pygame.image.load("coin.gif").convert()
        pygame.init()
        position = Position()
        # we put the background picture
        fond= pygame.image.load("fond.jpg").convert()
        fenetre.blit(fond,(0,0))
        # for each lines
        for i in range(15):
            # for each columns
            for j in range(15):
                # if we find a wall
                if position.checking_coordinates(self, i, j)== "m":
                    # we save our wall coordinates and multiply by the size of the cases
                    location_x = i* Labyrinthe.WIDTH_CASE
                    location_y = j* Labyrinthe.WIDTH_CASE
                    # we place the picture at the appropiated coordinated
                    fenetre.blit(self.wall, (location_x, location_y))
                # if we find object 1       
                elif position.checking_coordinates(self, i, j)== "1":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place the object1
                    fenetre.blit(self.pic_object1, (location_x, location_y))
                # if we find a "G" it means we have our macgyver character
                elif position.checking_coordinates(self, i, j)== "G":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place macgyver picture
                    fenetre.blit(self.pic_gyver, (location_x, location_y))
                #for the object 2
                elif position.checking_coordinates(self, i, j)== "2":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    #we place the picture of object 2
                    fenetre.blit(self.pic_object2, (location_x, location_y))
                # this is the exit and where he is located the bad guy
                elif position.checking_coordinates(self, i, j)== "E":
                    location_x = i* Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place the picture of the bad guy
                    fenetre.blit(self.bad_guy, (location_x, location_y))
                # object 3
                elif position.checking_coordinates(self, i, j)== "3":
                    location_x = i* Labyrinthe.WIDTH_CASE
                    location_y = j* Labyrinthe.WIDTH_CASE
                    fenetre.blit(self.pic_object3, (location_x, location_y))
        # we update the frame   
        pygame.display.flip()
    
    def placing_object(self):
        "function that places the 3 objects randomly"
        x = 1 
        while x <= 3:  
            i = random.randint(0,14)   #we pick up a random number between 0 and 14 in order to pick up a random column
            j = random.randint(0,14)   # random line
            if self.laby_area[i,j] == "0":   # if the coordinate picked up is free
                self.laby_area[i,j] = str(x) # we save our object
                x += 1
    
    def changing(self):
        "function that catches event"
        position=Position()
        #while macgyver has not arrived at the exit we have the loop
        while self.mg[0] != self.victory:
            position_x, position_y = self.mg[0]  # we save a and b as the actual coordinate of macgyver
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # if the player presses the keydown we call the function to test the position at the bottom case    
                    if event.key == K_DOWN:
                         new_x, new_y = position_x, (position_y + 1)
                    # if the player presses the keyup we will be trying the coordinates at the upper case
                    elif event.key == K_UP:
                        new_x, new_y = position_x, (position_y - 1)
                    # if the player presses the keyleft 
                    elif event.key == K_LEFT:
                        new_x, new_y = (position_x - 1), position_y 
                    # if the player presses the keyright
                    elif event.key == K_RIGHT:
                        new_x, new_y = (position_x + 1), position_y
                    # we check if the movement is inside the labyrinth   
                    if new_x in range(15) and new_y in range(15):
                        # if it is then we call our method which test the mouvement
                        position.testing_position(self,position_x, position_y, new_x, new_y)
                    else:
                        print("sorry you are out of the layout")
                    self.draw_laby() # we call up the method to upddate our labyrinthe
        # we check if the player has won or has lost
        if self.ending_game() is True:
            print("you have won")
        else:
            print("you have lost")

    def ending_game(self):
        "function that checks if Mac gyver has won the game or loose the game"
        # mac gyver has arrived at the exit we check if he has the 3 objects
        if len(self.object_picked_up) == 3:
            return True
        # we check if he hasnt got the 3 objects and then he has lost
        elif len(self.object_picked_up) <= 3:
            return False
    
    def moving_gyver(self, new_x, new_y):
        "function that gives the new coordinates of macgyver"
        # we set the new coordinates
        self.mg[0] = new_x, new_y
             

class Position:
    "classe that checks the mouvement"
    def checking_coordinates(self, labyrinthe, coordinate_x, coordinate_y):
        "function thats checks coordinates"
        # we return what has the coordinates provided
        return labyrinthe.laby_area[coordinate_x, coordinate_y] 
     
    def picking_up(self, labyrinthe, new_x, new_y):
        "function that picks up objects"
        if self.checking_coordinates(labyrinthe, new_x, new_y) == "1":
            # we add to the list object 1
            labyrinthe.object_picked_up.append("object1")
            print("Great! You found object1")
        elif self.checking_coordinates(labyrinthe, new_x, new_y) == "2":
            # we add to the list object 2
            labyrinthe.object_picked_up.append("object2")
            print("Great! You found object 2")
        elif self.checking_coordinates(labyrinthe, new_x, new_y) == "3":
            # we add to the list object 3
            labyrinthe.object_picked_up.append("object3")
            print("Great! You found object 3")   
    
    def testing_position(self, labyrinthe, first_x, first_y, new_x, new_y):
        "function that tests the mouvement"
        if self.checking_coordinates(labyrinthe, new_x, new_y) == "m":  #we check if there is a wall
            labyrinthe.mg[0] = first_x, first_y
            print("sorry you cant walk through a wall")
        else:
            #if the new coordinates are not a wall then we move gyver
            labyrinthe.moving_gyver(new_x, new_y)
            self.picking_up(labyrinthe, new_x, new_y)
            print(labyrinthe.object_picked_up)
            #the former gyver position is becoming a free path
            labyrinthe.laby_area[first_x, first_y] = "0"
            # we put gyver on our dictionnary
            labyrinthe.laby_area[new_x, new_y] = "G"
            labyrinthe.draw_laby()




if __name__ == '__main__':
    main()

