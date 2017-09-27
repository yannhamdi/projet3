#!/usr/bin/python3
# -*- coding: Utf-8 -*
import labyrinthe

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