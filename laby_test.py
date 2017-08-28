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
                    elif line[i]== "G":
                        self.laby_area[i,j]= "G"
                        wall=(i,j)
                        self.mg.append(wall)
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

    def changing_character(self):
        self.object_pickep_up=[]
        while len(self.object_pickep_up)!= 3:
            x=int(input("veuillez entrer x"))
            y=int(input("veuillez entrer y"))
            if 0<=x<=14 and 0<=y<=14:
                a, b = self.mg[0]
                print(self.laby_area[x,y])
                if self.checking_coordinates(x,y)=="m":
                    print("sorry you cant walk through a wall")
                else:
                    a,b= self.mg[0]
                    print(self.laby_area[x,y])
                    if self.laby_area[a,b]=="1":
                        self.object_pickep_up.append("object1")
                    elif self.laby_area[a,b]=="2":
                        self.object_pickep_up.append("object2")
                    elif self.laby_area[a,b]=="3":
                        self.object_pickep_up.append("object3")        
            
                    self.laby_area[a,b]= "0"
                    self.mg[0]= (x,y)
                    self.laby_area[x,y]= "G"
                    self.draw_laby()
                    print(self.l)

            else:
                print("Vous êtes hors zone")


    def checking_coordinates(self,x, y):
        "function that checks coordinates"
        return self.laby_area[x,y]
        
        
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

        



            





    

    





def main():
    laby=Labyrinthe()
    laby.draw_laby()
    print(laby.l)
    laby.placing_object()
    laby.changing_character()
    print(laby.l)
    

    
    

    

main()








        



