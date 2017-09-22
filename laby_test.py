
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
        self.draw_laby()
        position=Position()
        while self.ending_game()== False: #while the game is not terminated
            a,b=self.mg[0]
            event=input("veuillez entrer la direction") # we ask for the direction
            if event == "haut":
                self.move_up() # we call the up moving method
                new_x, new_y= self.mg[0] #new coordinates of gyver under the condition no wall
            elif event == "bas":
                self.move_down() # we call the up moving method
                new_x, new_y= self.mg[0]
            elif event == "droite":
                self.move_right() # we call the up moving method
                new_x, new_y= self.mg[0]
            elif event == "gauche":
                self.move_left() # we call the up moving method
                new_x, new_y= self.mg[0]
            try:
                position.testing_position(a, b, new_x, new_y) 
            except:
                self.mg[0]= a,b
                print("sorry you are out of the layout")    
                
            if self.mg[0]== self.victory and len(self.object_picked_up)<3:
                break
        if self.ending_game()== True:
            print("you have won")
        else:
            print("you have lost")

    def picking_up(self,new_x, new_y):
        "function that picks up objects"
        position=Position()
        if position.checking_coordinates(new_x, new_y)== "1":
            self.object_picked_up.append("object1")
            print("Great! You found object1")
        elif position.checking_coordinates(new_x, new_y)== "2":
             self.object_picked_up.append("object2")
             print("Great! You found object 2")
        elif position.checking_coordinates(new_x, new_y)== "3":
             self.object_picked_up.append("object3")
             print("Great! You found object 3")
    
    def ending_game(self):
        "function that checks if Mac gyver has won the game"
        if self.mg[0]== self.victory and len(self.object_picked_up)==3:
            print(self.object_picked_up)
            return True
        else:
            print(self.object_picked_up)
            return False
        
    def move_right(self):  
        "function that move gyver to the right and check if the movement is in the layout"
        x,y= self.mg[0]
        self.mg[0]= x, (y+1)
    
    def move_left(self):
        "function that move gyver to the left and check if the movement is in the layout"
        x,y= self.mg[0]
        self.mg[0]= x, (y-1)  
          
    
    def move_up(self):
        "function that move up gyver and check if the movement is in the layout"
        x,y=self.mg[0]
        self.mg[0]= (x-1), y

    def move_down(self):
        "function that move down gyver and check if the movement is in the layout"
        x,y= self.mg[0]
        self.mg[0]= ((x+1), y)
             

class Position(Labyrinthe):
    def checking_coordinates(self,x,y):
        "function thats checks coordinates"
        return self.laby_area[x,y] 
        
    
    def testing_position(self, first_x, first_y, new_x, new_y):
        "function that tests the mouvement"
        if self.checking_coordinates(new_x, new_y)== "m":  #we check if there is a wall
            self.mg[0]= first_x, first_y
            print("sorry you cant walk through a wall")
        else:
            self.mg[0]= new_x, new_y
            self.laby_area[first_x, first_y]= "0"
            self.laby_area[new_x, new_y]="G"
            self.picking_up(new_x, new_y)
            print(self.object_picked_up)
            self.draw_laby()
            self.ending_game()


def main():
    
    laby=Labyrinthe()
    laby.placing_object()
    laby.changing_character()
  

main()






