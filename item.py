#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""item class for the game with random location at each start and item
counter"""

from mypygame import *
from constants import *


class Item:
    """methods to act on items in game level"""

    def __init__(self, level):
        # refer to current level structure
        self.level = level
        # inventory counter
        self.picked_up_item = 0
        self.mypygame = Mypygame()
        # load items assets
        self.bottle = self.mypygame.load_asset(BOTTLE_IMAGE)
        self.pipe = self.mypygame.load_asset(PIPE_IMAGE)
        self.needle = self.mypygame.load_asset(NEEDLE_IMAGE)
        self.background = self.mypygame.load_asset(BACKGROUND_IMAGE)

    def display_items(self, window):
        """display items not picked up"""
        # display items assets from structure
        nb_line = 0
        for line in self.level.structure:
            nb_tile = 0
            for tile in line:
                pixel_x = nb_tile * TILE_SIZE
                pixel_y = nb_line * TILE_SIZE
                if tile == "B":
                    window.blit(self.bottle, (pixel_x, pixel_y))
                elif tile == "P":
                    window.blit(self.pipe, (pixel_x, pixel_y))
                elif tile == "N":
                    window.blit(self.needle, (pixel_x, pixel_y))
                nb_tile += 1
            nb_line += 1

    def pick_up_item(self, position):
        """method for adding items to inventory when player is on tile"""
        # superimpose background on item image
        self.mypygame.display_asset(self.background, (position[0], position[1]))
        # modify level structure to orignal value
        item_tile_x = int(position[0] / TILE_SIZE)
        item_tile_y = int(position[1] / TILE_SIZE)
        self.level.structure[item_tile_y][item_tile_x] = "O"
        # increment inventory counter
        self.picked_up_item += 1

    def display_counter(self):
        """display the item counter in window"""
        counter = ("items picked up = {}".format(self.picked_up_item))
        self.mypygame.display_text(counter, (0, 430))
