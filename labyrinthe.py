#!/usr/bin/python3
# -*- coding: Utf-8 -*

"Game where macgyver must collect 3 objects before find the exit"

import random

import sys

import pygame
from pygame.locals import *



from position import *


class Labyrinthe:
    "the class that manages our labyrinthe"
    # the size of our case
    WIDTH_CASE = 40
    # the number of sprite
    SPRITE = 15
    def __init__(self):
        "We initialize our labyrinthe"
        self.laby_area = {} #dictionnary that has all the coordinates of the labyrinthe
        self.mcgyver = [] # mac gyver position
        # the bag that contains the object picked up
        self.object_picked_up = []
        j = 0
        # we open our labyrinthe file
        with open("laby.txt", 'r') as file_laby:
            for line in file_laby:# for each line
                for i in range(len(line)):
                    if line[i] == "m":
                        # we create our dictionnary including coordinates of the wall
                        self.laby_area[i, j] = "m"
                    elif line[i] == "0":
                        self.laby_area[i, j] = "0" # we have our coordinates of our pathway
                    elif line[i] == "E":
                        self.laby_area[i, j] = "E" # we have our coordinates'wayout
                        self.victory = (i, j)
                    elif line[i] == "G":
                        self.laby_area[i, j] = "G"

                        gyver = (i, j)
                        self.mcgyver.append(gyver)

                j += 1
        # we call up our method placing object to place the 3 objects
        self.placing_object()
        # we draw the labyrinthe
        self.draw_laby()
        # we call up the loop to start the game
        self.playing_game()

    def draw_laby(self):
        "function that draws the labyrinthe in the console"
        # we create the labyrinthe frame
        self.fenetre = pygame.display.set_mode((Labyrinthe.WIDTH_CASE * Labyrinthe.SPRITE,
                                                Labyrinthe.WIDTH_CASE * Labyrinthe.SPRITE))
        # we initialize our pictures for the game
        self.wall = pygame.image.load("mur.gif").convert()
        self.pic_object1 = pygame.image.load("bottle.gif").convert()
        self.pic_gyver = pygame.image.load("gyver.png").convert_alpha()
        self.bad_guy = pygame.image.load("bad.png").convert_alpha()
        self.pic_object2 = pygame.image.load("box.gif").convert()
        self.pic_object3 = pygame.image.load("coin.gif").convert()
        # we put the background picture
        fond = pygame.image.load("fond.jpg").convert()
        self.fenetre.blit(fond, (0, 0))
        # for each lines
        for i in range(15):
            # for each columns
            for j in range(15):
                # if we find a wall
                if self.laby_area[i, j] == "m":
                    # we save our wall coordinates and multiply by the size of the cases
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place the picture at the appropiated coordinated
                    self.fenetre.blit(self.wall, (location_x, location_y))
                # if we find object 1
                elif self.laby_area[i, j] == "1":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place the object1
                    self.fenetre.blit(self.pic_object1, (location_x, location_y))
                # if we find a "G" it means we have our macgyver character
                elif self.laby_area[i, j] == "G":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place macgyver picture
                    self.fenetre.blit(self.pic_gyver, (location_x, location_y))
                #for the object 2
                elif self.laby_area[i, j] == "2":
                    location_x = i * Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    #we place the picture of object 2
                    self.fenetre.blit(self.pic_object2, (location_x, location_y))
                # this is the exit and where he is located the bad guy
                elif self.laby_area[i, j] == "E":
                    location_x = i* Labyrinthe.WIDTH_CASE
                    location_y = j * Labyrinthe.WIDTH_CASE
                    # we place the picture of the bad guy
                    self.fenetre.blit(self.bad_guy, (location_x, location_y))
                # object 3
                elif self.laby_area[i, j] == "3":
                    location_x = i* Labyrinthe.WIDTH_CASE
                    location_y = j* Labyrinthe.WIDTH_CASE
                    self.fenetre.blit(self.pic_object3, (location_x, location_y))
        # we update the frame
        pygame.display.flip()

    def placing_object(self):
        "function that places the 3 objects randomly"
        number_object = 1
        while number_object <= 3:
            #we pick up a random number between 0 and 14 in order to pick up a random column
            i = random.randint(0, 14)
            j = random.randint(0, 14)   # random line
            if self.laby_area[i, j] == "0":   # if the coordinate picked up is free
                self.laby_area[i, j] = str(number_object) # we save our object
                number_object += 1

    def playing_game(self):
        "function that catches event"
        pygame.init()
        #while macgyver has not arrived at the exit we have the loop
        while self.mcgyver[0] != self.victory:
            #initial position of macgyver
            position_x, position_y = self.mcgyver[0]
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    # if the player presses keydown
                    if event.key == K_DOWN:
                        # we calculate new coordinates
                        new_x, new_y = position_x, (position_y + 1)
                    # if the player presses the keyup
                    elif event.key == K_UP:
                        #we calculate new coordinates
                        new_x, new_y = position_x, (position_y - 1)
                    # if the player presses the keyleft
                    elif event.key == K_LEFT:
                        new_x, new_y = (position_x - 1), position_y
                    # if the player presses the keyright
                    elif event.key == K_RIGHT:
                        new_x, new_y = (position_x + 1), position_y
                    elif event.key == K_b:
                        continuer = 1
                        while continuer:
                            font = pygame.font.Font(None, 40)
                            text = font.render(str(self.object_picked_up)
                                                  , 1, (255, 255, 255))
                            font_1 = pygame.font.Font(None, 40)
                            text_1 = font_1.render(("Press e to quit"), 1, (165, 38, 10))
                            textrect = text.get_rect(center=(300, 300))
                            textrect_1 = text_1.get_rect(bottomleft=(400, 600))
                            self.fenetre.blit(text, textrect)
                            self.fenetre.blit(text_1, textrect_1)
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_e:
                                        continuer = 0
                    # we check if the movement is inside the labyrinth
                    if new_x in range(15) and new_y in range(15):
                        # if it is then we call our method which test the mouvement
                        Position.testing_position(self, position_x, position_y, new_x, new_y)
                    self.draw_laby() # we call up the method to upddate our labyrinthe
        # we check if the player has won or has lost
        if self.ending_game() is True:
            continuer = 1
            while continuer:
                font = pygame.font.Font(None, 50)
                text = font.render("Congratulations, You have won!", 1,
                                   (255, 255, 255))
                textrect = text.get_rect(center=(300, 300))
                font_1 = pygame.font.Font(None, 40)
                text_1 = font_1.render(("Press r to quit"), 1, (165, 38, 10))
                textrect_1 = text_1.get_rect(bottomleft=(400, 600))
                self.fenetre.blit(text, textrect)
                self.fenetre.blit(text_1, textrect_1)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            continuer = 0
        else:
            continuer = 1
            while continuer:
                font = pygame.font.Font(None, 60)
                text = font.render("Sorry!You have lost!", 1, (255, 255, 255))
                textrect = text.get_rect(center=(300, 300))
                font_1 = pygame.font.Font(None, 40)
                text_1 = font_1.render(("Press r to quit"), 1, (165, 38, 10))
                textrect_1 = text_1.get_rect(bottomleft=(400, 600))
                self.fenetre.blit(text, textrect)
                self.fenetre.blit(text_1, textrect_1)
                self.draw_laby
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            continuer = 0

    def ending_game(self):
        "function that checks if Mac gyver has won the game or loose the game"
        # mac gyver has arrived at the exit we check if he has the 3 objects
        if len(self.object_picked_up) == 3:
            return True
        # we check if he hasnt got the 3 objects and then he has lost
        elif len(self.object_picked_up) <= 3:
            return False

    def moving_gyver(self, new_x, new_y):
        "function that gives the new coordinates of macgyver"
        # we set the new coordinates
        self.mcgyver[0] = new_x, new_y

    def picking_up(self, new_x, new_y):
        "function that picks up objects"
        if self.laby_area[new_x, new_y] == "1":
            # we add to the list object 1
            self.object_picked_up.append("object1")
        #we are checking if there is object 2 at the new_X, new_y coordinates
        elif self.laby_area[new_x, new_y] == "2":
            # we add to the list object 2
            self.object_picked_up.append("object2")
        elif self.laby_area[new_x, new_y] == "3":
            # we add to the list object 3
            self.object_picked_up.append("object3")





if __name__ == '__main__':
    main()
