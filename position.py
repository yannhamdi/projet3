from labyrinthe import *



class Position:
    
    @classmethod
    def testing_position(cls, labyrinthe, first_x, first_y, new_x, new_y):
        "function that tests the mouvement"
        # we check if there is a wall
        if labyrinthe.laby_area[new_x, new_y] == "m":
            labyrinthe.mcgyver[0] = first_x, first_y
        elif labyrinthe.laby_area[new_x, new_y] == "1" or "2" or "3":
            labyrinthe.picking_up(new_x, new_y)
            labyrinthe.moving_gyver(new_x, new_y)
            labyrinthe.laby_area[first_x, first_y] = "0"
            labyrinthe.laby_area[new_x, new_y] = "G"
            labyrinthe.draw_laby()
        elif labyrinthe.laby_area[new_x, new_y] == "0":
            labyrinthe.moving_gyver(new_x, new_y)
            labyrinthe.laby_area[first_x, first_y] = "0"
            labyrinthe.laby_area[new_x, new_y] = "G"
            labyrinthe.draw_laby()


if __name__ == '__main__':
    main()
