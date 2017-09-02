#!/usr/bin/python3
# -*- coding: Utf-8 -*
import random

class Position:
    def __init__(self,x,y):
        coordinate= [x,y]
        self.name= ""
        
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
                        Position(i,j).name= "m" 
                        self.laby_area[i,j]= "m"  # we create our dictionnary including coordinates of the wall
                    elif line[i] == "0":
                        Position(i,j).name= "0"
                        self.laby_area[i,j]= "0" # we have our coordinates of our pathway
                        possible_object= (i,j)
                        self.free_cases.append(possible_object)
                    elif line[i] == "E":
                        self.laby_area[i,j]= "E" # we have our coordinates'wayout
                    elif line[i]== "G":
                        self.laby_area[i,j]= "G"

                        gyver=(i,j)
                        self.mg.append(gyver)

                j += 1


           
            

    def draw_laby(self):
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
class Character(Labyrinthe):

    def __init( self):
        self.x=x
        self.y=y
        
        


    def move_right(self):    
        x,y= self.mg[0]
        self.mg[0]= ((x+1), y)
    
    def move_left(self):
        x,y= self.mg[0]
        self.mg[0]= (x-1), y
    
    def move_up(self):
        x,y= self.mg[0]
        self.mg[0]= x, (y+1)

    def move_down(self):
        x,y= self.mg[0]
        self.mg[0]= x, (y-1)


    



    def changing_character(self):
        
        a,b = self.mg[0]
        self.object_pickep_up=[]
        while self.ending_game(a,b)!= "true":
            event=input("veuillez entrer la direction")
            if event == "droite":
                self.move_right()
                new_x, new_y= self.mg[0]
                if 0<=new_x<=14 and 0<=new_y<=14:
                    if self.checking_coordinates(new_x, new_y)=="m":
                        print("sorry you cant walk through a wall")
                        self.mg[0]=a,b 
                    else:
                        self.mg[0]=new_x, new_y
                        if self.laby_area[new_x, new_y]=="1":
                            self.object_pickep_up.append("object1")
                            print("congrats, you have found object1")
                        elif self.laby_area[new_x, new_y]=="2":
                            self.object_pickep_up.append("object2")
                            print("congrats! You have found object 2")
                        elif self.laby_area[new_x,new_y]=="3":
                            self.object_pickep_up.append("object3") 
                            print("congrats! You have found object3")       
            
                        self.laby_area[a,b]= "0"
                        self.mg[0]= (new_x, new_y)
                        self.laby_area[new_x, new_y]= "G"
                        self.draw_laby()
                        
                        if self.ending_game(new_x, new_y) == "true":
                            break
            elif event == "gauche":
                self.move_left()
                new_x, new_y= self.mg[0]
                if 0<=new_x<=14 and 0<=new_y<=14:
                    if self.checking_coordinates(new_x, new_y)=="m":
                        print("sorry you cant walk through a wall")
                        self.mg[0]=a,b 
                    else:
                        self.mg[0]=new_x, new_y
                        print(self.l)
                        if self.laby_area[new_x, new_y]=="1":
                            self.object_pickep_up.append("object1")
                        elif self.laby_area[new_x, new_y]=="2":
                            self.object_pickep_up.append("object2")
                        elif self.laby_area[new_x,new_y]=="3":
                            self.object_pickep_up.append("object3")        
            
                        self.laby_area[a,b]= "0"
                        self.mg[0]= (new_x, new_y)
                        self.laby_area[new_x, new_y]= "G"
                        self.draw_laby()
                        
                        if self.ending_game(new_x, new_y) == "true":
                            break
            elif event == "haut":
                    self.move_up()
                    new_x, new_y= self.mg[0]
                    if 0<=new_x<=14 and 0<=new_y<=14:
                        if self.checking_coordinates(new_x, new_y)=="m":
                            print("sorry you cant walk through a wall")
                            self.mg[0]=a,b 
                        else:
                            self.mg[0]=new_x, new_y
                            if self.laby_area[new_x, new_y]=="1":
                                self.object_pickep_up.append("object1")
                            elif self.laby_area[new_x, new_y]=="2":
                                self.object_pickep_up.append("object2")
                            elif self.laby_area[new_x,new_y]=="3":
                                self.object_pickep_up.append("object3")        
            
                            self.laby_area[a,b]= "0"
                            self.mg[0]= (new_x, new_y)
                            self.laby_area[new_x, new_y]= "G"
                            self.draw_laby()
                            
                            if self.ending_game(new_x, new_y) == "true":
                                break
                 
            elif event == "bas":
                    self.move_down()
                    new_x, new_y= self.mg[0]
                    if 0<=new_x<=14 and 0<=new_y<=14:
                        if self.checking_coordinates(new_x, new_y)=="m":
                            print("sorry you cant walk through a wall")
                            self.mg[0]=a,b 
                        else:
                            self.mg[0]=new_x, new_y

                        
                            if self.laby_area[new_x, new_y]=="1":
                                self.object_pickep_up.append("object1")
                            elif self.laby_area[new_x, new_y]=="2":
                                self.object_pickep_up.append("object2")
                            elif self.laby_area[new_x,new_y]=="3":
                                self.object_pickep_up.append("object3")        
            
                            self.laby_area[a,b]= "0"
                            self.mg[0]= (new_x, new_y)
                            self.laby_area[new_x,new_y]= "G"
                            self.draw_laby()
                            print(self.l)
                            if self.ending_game(new_x, new_y) == "true":
                                print("you have won")
                                break              
                    else:
                        print("Vous êtes hors zone")
               


    def checking_coordinates(self,x, y):
        "function that checks coordinates"
        return self.laby_area[x,y]
        
        
    



    def ending_game(self,x,y):
        "function that checks if Mac gyver has won the game"
        if self.checking_coordinates(x,y)== "E" and len(self.object_pickep_up)==3:
            return "true"  



            





    

    





def main():
    laby=Labyrinthe()
    laby.draw_laby()
    print(laby.l)
    laby.placing_object()

    macgyver= Character()
    macgyver.changing_character()
    

          
    

    

    
    

    

main()








        



