
# -*- coding: Utf-8 -*
import random

import sys

        
class Labyrinthe:
    WIDTH_CASE= 25
    SPRITE= 15
        
    
    def __init__ (self):
        "We initialize our labyrinthe"
        self.laby_area= {}
        self.mg=[]
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
        self.changing_character()

    def draw_laby(self, **laby_area):
        "function that draws the labyrinthe in the console"

        for i in range(15):
            for j in range(15):
                sys.stdout.write(self.laby_area[i,j])

            sys.stdout.write("\n")    
        
    def placing_object(self):
        "function that places the 3 objects randomly"
        x=1 
        while x<=3:
            i= random.randint(0,14)
            j= random.randint(0,14)
            if self.laby_area[i,j]== "0":
                self.laby_area[i,j]= str(x)
                x += 1
            else:
                x=x
        
    def changing_character(self):
        "function that ask direction and place gyver to the new position"
        position=Position()
        while self.ending_game()== False or self.losing_game()== False: #while the game is not terminated win or loose
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
            self.ending_game()
            self.losing_game()
        if self.ending_game()== True:
            print("you have won")
        elif self.losing_game() == True:
            print("you have lost")

   
    
    def ending_game(self):
        "function that checks if Mac gyver has won the game"
        if self.mg[0]== self.victory and len(self.object_picked_up)==3:
            print(self.object_picked_up)
            return True
        else:
            print(self.object_picked_up)
            return False
    
    def losing_game(self):
        "function that checks if we loose the game"
        if self.mg[0]== self.victory and len(self.object_picked_up)<3:
            return True
        else:
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
    
    laby = Labyrinthe()
  

main()






