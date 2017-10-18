from labyrinthe import *



class Position:
    "classe that checks the mouvement"
    @classmethod
    def checking_coordinates(cls, labyrinthe, coordinate_x, coordinate_y):
        "function thats checks coordinates"
        # we return what has the coordinates provided
        return labyrinthe.laby_area[coordinate_x, coordinate_y]
    @classmethod
    def testing_position(cls, labyrinthe, first_x, first_y, new_x, new_y):
        "function that tests the mouvement"
        # we check if there is a wall
        if Position.checking_coordinates(labyrinthe, new_x, new_y) == "m":
            labyrinthe.mcgyver[0] = first_x, first_y
        elif Position.checking_coordinates(labyrinthe, new_x, new_y) == "1" or "2" or "3":
            labyrinthe.picking_up(new_x, new_y)
            labyrinthe.moving_gyver(new_x, new_y)
            labyrinthe.laby_area[first_x, first_y] = "0"
            labyrinthe.laby_area[new_x, new_y] = "G"
            labyrinthe.draw_laby()
        elif Position.checking_coordinates(labyrinthe, new_x, new_y) == "0":
            labyrinthe.moving_gyver(new_x, new_y)
            labyrinthe.laby_area[first_x, first_y] = "0"
            labyrinthe.laby_area[new_x, new_y] = "G"
            labyrinthe.draw_laby()


if __name__ == '__main__':
    main()
