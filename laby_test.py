#!/usr/bin/python3
# -*- coding: Utf-8 -*

class Labyrinthe:
    WIDTH_CASE= 25
    SPRITE= 15
        
    
    def __init__ (self):
        "We initialize our labyrinthe"
        self.laby_area= {}
        self.mg=[]

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
            
            self.l+="\n"

    def changing_character(self):
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
        
        

        
            





    

    





def main():
    laby=Labyrinthe()
    laby.draw_laby()
    print(laby.l)
    laby.changing_character()
    

    
    

    

main()








        



