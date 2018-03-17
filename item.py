#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""item class for the game with random location at each start and item
counter"""
import random
import pygame

from pygame.locals import *

from constants import *

class Item:
    """docsting"""

    def __init__(self, level):
        # refer to current level structure
        self.level = level
        # inventory counter
        self.picked_up_item = 0

    def create_items(self):
        """method to modify level structure with item markers at random location"""
        # create randomization loop counter
        items_set = 0
        while items_set < 3:
            # create random values for x,y item coordinates
            item_x = random.randint(0, (SPRITES_PER_ROW - 1))
            item_y = random.randint(0, (SPRITES_PER_ROW - 1))
            # if check random position is not a wall
            if self.level.structure[item_y][item_x] != "M":
                if items_set == 0:
                    # modify level structure with item marker
                    self.level.structure[item_y][item_x] = "B"
                elif items_set == 1:
                    self.level.structure[item_y][item_x] = "P"
                elif items_set == 2:
                    self.level.structure[item_y][item_x] = "N"
                # increment counter
                items_set += 1
            # else restart loop from random values creation
            else:
                continue

    def display_items(self, window):
        """display items not picked up"""
        # load items assets
        bottle = pygame.image.load(BOTTLE_IMAGE).convert_alpha()
        pipe = pygame.image.load(PIPE_IMAGE).convert_alpha()
        needle = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        # display items assets from structure
        nb_line = 0
        for line in self.level.structure:
            nb_tile = 0
            for tile in line:
                pixel_x = nb_tile * TILE_SIZE
                pixel_y = nb_line * TILE_SIZE
                if tile == "B":
                    window.blit(bottle, (pixel_x, pixel_y))
                elif tile == "P":
                    window.blit(pipe, (pixel_x, pixel_y))
                elif tile == "N":
                    window.blit(needle, (pixel_x, pixel_y))
                nb_tile += 1
            nb_line += 1

    def pick_up_item(self, window, position):
        """method for adding items to inventory when player is on tile"""
        # load background image
        background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
        # superimpose background on item image
        window.blit(background, (position[0], position[1]))
        # modify level structure to orignal value
        item_tile_x = int(position[0] / TILE_SIZE)
        item_tile_y = int(position[1] / TILE_SIZE)
        self.level.structure[item_tile_y][item_tile_x] = "O"
        # increment inventory counter
        self.picked_up_item += 1
