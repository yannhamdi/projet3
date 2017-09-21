#!/usr/bin/python3
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
                        possible_object= (i,j)
                        self.free_cases.append(possible_object)
                    elif line[i] == "E":
                        self.laby_area[i,j]= "E" # we have our coordinates'wayout
                        self.victory=(i,j)
                    elif line[i]== "G":
                        self.laby_area[i,j]= "G"

                        gyver=(i,j)
                        self.mg.append(gyver)

                j += 1

        self.draw_laby()
           
            

    def draw_laby(self, **laby_area):
        "function that draws the labyrinthe in the console"

        for i in range(15):
            for j in range(15):
                sys.stdout.write(self.laby_area[i,j])

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

    def changing_character(self,event):
        "function that ask direction and place gyver to the new position"
        self.placing_object()
        if event == "haut":
            self.move_up() # we call the up moving method
            self.new_x, self.new_y= self.mg[0] #new coordinates of gyver under the condition no wall
        elif event == "bas":
            self.move_down() # we call the up moving method
            self.new_x, self.new_y= self.mg[0]
        elif event == "droite":
            self.move_right() # we call the up moving method
            self.new_x, self.new_y= self.mg[0]
        elif event == "gauche":
            self.move_left() # we call the up moving method
            self.new_x, self.new_y= self.mg[0]
                
                
        
   
    


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
        
    
    def checking_layout(self, x,y):
        "function thats checks if macgyver is moving inside the layout"
        x,y = self.mg[0]
        if x in range(15) and y in range(15):
            return True
        else:
            return False
            

    def testing_position(self, first_x, first_y, new_x, new_y):
        "we change coordinates if possible"
        
        if self.checking_coordinates(new_x,new_y)=="m":
            self.mg[0]= first_x, first_y
            print("Sorry, you can't walk through a wall")
        elif self.checking_layout(new_x, new_y)== False:
            self.mg[0]= first_x, first_y
            return self.mg[0]
            print("Sorry, you are out of the layout")
        else:
            self.mg[0]= new_x, new_y
            self.laby_area[first_x, first_y]= "0"
            self.laby_area[new_x, new_y]="G"
            self.picking_up(new_x, new_y)
            print(self.object_picked_up)
            self.draw_laby()
            self.ending_game()


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






    

    





def main():
    
    laby=Labyrinthe()
    position=Position()
    while laby.ending_game()== False: #while the game is not terminated
        a,b=laby.mg[0]
        event=input("veuillez entrer la direction")
        laby.changing_character(event)
        position.testing_position(a,b, laby.new_x, laby.new_y)
        if laby.mg[0]== laby.victory and len(laby.object_picked_up)<3:
            break
                         
    if laby.ending_game()== True:
        print("you have won")
    else:
        print("you have lost")

    

    

          
    

    

    
    

    

main()








        



