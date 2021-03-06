#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""level class with the methods to create and display a level"""
import random

from mypygame import *
from constants import *


class Level:
    """level structure must be imported from an external file"""

    def __init__(self, file):
        # class elements
        self.file = file
        self.structure = []
        self.items = ["B", "P", "N"]
        # initiate wrapper
        self.mypygame = Mypygame()
        # load assets
        self.wall = self.mypygame.load_asset(WALL_IMAGE)
        self.guardian = self.mypygame.load_asset(GUARDIAN_IMAGE)

    def create_level(self):
        """create level structure from file"""
        with open(self.file, "r") as level_file:  # open file from hdd
            grid = []  # initialize main layout array
            for line in level_file:
                grid_line = []  # initialize array for single line
                for box in line:
                    if box != "\n":
                        grid_line.append(box)  # add wall element to line array
                grid.append(grid_line)  # add line array to main array
        self.structure = grid

    def create_items(self):
        """method to modify level structure with item markers at random location"""
        for item in self.items:
            # create random values for x,y item coordinates
            item_x = random.randint(1, (SPRITES_PER_ROW - 1))
            item_y = random.randint(1, (SPRITES_PER_ROW - 1))
            # if check random position is not a wall
            if self.structure[item_y][item_x] != "M":
                # modify level structure with item marker
                self.structure[item_y][item_x] = item
            else:
                # add item back to array until 3 items are placed
                self.items.append(item)
        return self.structure

    def display_level(self):
        """display level in pygame from structure"""
        # integrate assets on structure
        nb_line = 0
        for line in self.structure:
            nb_tile = 0
            for tile in line:
                pixel_x = nb_tile * TILE_SIZE  # set x pixel value to be displayed from tile size
                pixel_y = nb_line * TILE_SIZE  # set y pixel value to be displayed from tile size
                position = [pixel_x, pixel_y]
                if tile == "M":
                    self.mypygame.display_asset(self.wall, position)
                elif tile == "A":
                    self.mypygame.display_asset(self.guardian, position)
                nb_tile += 1
            nb_line += 1
