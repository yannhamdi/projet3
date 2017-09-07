#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random


        
class Labyrinthe:
    WIDTH_CASE= 25
    SPRITE= 15
        
    
    def __init__ (self):
        "We initialize our labyrinthe"
        self.laby_area= {}
        self.mg=[]
        self.free_cases =[]

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

        self.l=""
        for i in range(15):
            for j in range(15):
                if self.laby_area[i,j]== "m":
                    self.l+="m"
                elif self.laby_area[i,j]=="0":
                    self.l+="0"
                elif self.laby_area[i,j]=="E":
                    self.l+="E"
                elif self.laby_area[i,j]=="G":
                    self.l+="G"
                elif self.laby_area[i,j]== "1":
                    self.l+="1"
                elif self.laby_area[i,j]== "2":
                    self.l+="2"
                elif self.laby_area[i,j]== "3":
                    self.l+="3"    
                
            self.l+="\n"
        print(self.l)    



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
        self.draw_laby()


    def changing_character(self):
        "function that ask direction and place gyver to the new position"
        self.object_pickep_up=[]
        
        self.placing_object()
        while self.ending_game(self.object_pickep_up)== False: #while the game is not terminated
            
            a,b=self.mg[0]
            event=input("veuillez entrer la direction") # we ask for the direction
            if event == "haut":
                self.move_up() # we call the up moving method
                new_x, new_y= self.mg[0]
                if self.checking_coordinates(new_x, new_y)=="m": # we check if it is not a wall
                    self.mg[0]=a,b
                    print("sorry you cant walk through a wall") # we go back to the former position of macgyver
                    self.draw_laby()
                else:
                    self.mg[0]=new_x, new_y # if it is not a wall we move forward to the new coordinates
                    if self.checking_coordinates(new_x, new_y)== "1":
                        self.object_pickep_up.append("object1")
                        print("Great! You found object1")
                    elif self.checking_coordinates(new_x, new_y)== "2":
                        self.object_pickep_up.append("object2")
                        print("Great! You found object 2")
                    elif self.checking_coordinates(new_y, new_y)== "3":
                        self.object_pickep_up.append("object3")
                        print("Great! You found object 3")
                    self.laby_area[new_x, new_y]= "G" # we change our dictionnary with the new mac gyver position
                    self.laby_area[a,b]="0" #we change G by the pathway in order to draw the new labyrinthe
                    self.draw_laby() 
                    self.ending_game(self.object_pickep_up)   
                    print(self.ending_game(self.object_pickep_up))
                        
                         
            if event == "bas":
                self.move_down() # we call the up moving method
                new_x, new_y= self.mg[0]
                if self.checking_coordinates(new_x, new_y)=="m": # we check if it is not a wall
                    self.mg[0]=a,b
                    print("sorry you cant walk through a wall") # we go back to the former position of macgyver
                    self.draw_laby()
                else:
                    self.mg[0]=new_x, new_y # if it is not a wall we move forward to the new coordinates
                    if self.checking_coordinates(new_x, new_y)== "1":
                        self.object_pickep_up.append("object1")
                        print("Great! You found object1")
                    elif self.checking_coordinates(new_x, new_y)== "2":
                        self.object_pickep_up.append("object2")
                        print("Great! You found object 2")
                    elif self.checking_coordinates(new_y, new_y)== "3":
                        self.object_pickep_up.append("object3")
                        print("Great! You found object 3") 
                    self.laby_area[new_x, new_y]= "G" # we change our dictionnary with the new mac gyver position
                    self.laby_area[a,b]="0" #we change G by the pathway in order to draw the new labyrinthe
                    self.draw_laby()
                    self.ending_game(self.object_pickep_up)   
                    print(self.ending_game(self.object_pickep_up))      
                    
            if event == "droite":
                self.move_right() # we call the up moving method
                new_x, new_y= self.mg[0]
                if self.checking_coordinates(new_x, new_y)=="m": # we check if it is not a wall
                    self.mg[0]=a,b
                    print("sorry you cant walk through a wall") # we go back to the former position of macgyver
                    self.draw_laby()
                else:
                    self.mg[0]=new_x, new_y # if it is not a wall we move forward to the new coordinates
                    if self.checking_coordinates(new_x, new_y)== "1":
                        self.object_pickep_up.append("object1")
                        print("Great! You found object1")
                    elif self.checking_coordinates(new_x, new_y)== "2":
                        self.object_pickep_up.append("object2")
                        print("Great! You found object 2")
                    elif self.checking_coordinates(new_y, new_y)== "3":
                        self.object_pickep_up.append("object3")
                        print("Great! You found object 3") #we check if there is an object in new mac gyver position
                    self.laby_area[new_x, new_y]= "G" # we change our dictionnary with the new mac gyver position
                    self.laby_area[a,b]="0" #we change G by the pathway in order to draw the new labyrinthe
                    self.draw_laby()
                    self.ending_game(self.object_pickep_up)   
                    print(self.ending_game(self.object_pickep_up))    
                        
                      
            if event == "gauche":
                self.move_left() # we call the up moving method
                new_x, new_y= self.mg[0]
                if self.checking_coordinates(new_x, new_y)=="m": # we check if it is not a wall
                    self.mg[0]=a,b
                    print("sorry you cant walk through a wall") # we go back to the former position of macgyver
                    self.draw_laby()
                else:
                    self.mg[0]=new_x, new_y 
                    if self.checking_coordinates(new_x, new_y)== "1":
                        self.object_pickep_up.append("object1")
                        print("Great! You found object1")
                    elif self.checking_coordinates(new_x, new_y)== "2":
                        self.object_pickep_up.append("object2")
                        print("Great! You found object 2")
                    elif self.checking_coordinates(new_y, new_y)== "3":
                        self.object_pickep_up.append("object3")
                        print("Great! You found object 3")
                    self.laby_area[new_x, new_y]= "G" # we change our dictionnary with the new mac gyver position
                    self.laby_area[a,b]="0" #we change G by the pathway in order to draw the new labyrinthe
                    self.draw_laby()   
                    self.ending_game(self.object_pickep_up)   
                    print(self.ending_game(self.object_pickep_up))
            if self.mg[0]== self.victory and len(self.object_pickep_up)<3:
                break
                         
        if self.ending_game(self.object_pickep_up)== True:
            print("you have won")
        else:
        	print("you have lost")

    def checking_coordinates(self,x, y):
        "function that checks coordinates"
        return self.laby_area[x,y]
    
    
class Character(Labyrinthe):

    def __init( self):
        self.x=x
        self.y=y

        
        


    def move_right(self):  
        "function that move gyver to the right and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=(x+1)<=14 and 0<=y<=14:  
            self.mg[0]= ((x+1), y)
        else:
            print("you are out of the layout")
    
    def move_left(self):
        "function that move gyver to the left and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=(x-1)<=14 and 0<=y<=14:
            self.mg[0]= (x-1), y
        else:
            print("you are out of the layout")    
    
    def move_up(self):
        "function that move up gyver and check if the movement is in the layout"
        x,y=self.mg[0]
        if 0<=x<=14 and 0<=(y+1)<=14:
            self.mg[0]= x, (y+1)
        else:
            print("you are out of the layout")    

    def move_down(self):
        "function that move down gyver and check if the movement is in the layout"
        x,y= self.mg[0]
        if 0<=x<=14 and 0<=(y-1)<=14:
            self.mg[0]= x, (y-1)
            
        else:
            print("you are out of the layout")       
    



    def ending_game(self, bag=[]):
        "function that checks if Mac gyver has won the game"
        
        if self.mg[0]== self.victory and len(bag)==3:
            return True
        else:
            return False


            





    

    





def main():
    
    laby=Labyrinthe()
    laby.draw_laby()
    laby.placing_object()

    macgyver= Character()
    
    macgyver.changing_character()
  

    

          
    

    

    
    

    

main()








        



