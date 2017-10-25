"we create our module position"


class Position:
    "class that checks coordinates and manages the game"
    @classmethod
    def testing_position(cls, labyrinthe, first_x, first_y, new_x, new_y):
        "function that tests the mouvement"
        # we check if there is a wall
        if labyrinthe.laby_area[new_x, new_y] == "m":
            labyrinthe.mcgyver[0] = first_x, first_y
        # if we have 1, 2 or 3 on the case we launch the method to pickup the object
        elif labyrinthe.laby_area[new_x, new_y] == "1" \
                       or labyrinthe.laby_area[new_x, new_y] == "2" \
                       or  labyrinthe.laby_area[new_x, new_y] == "3":
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
