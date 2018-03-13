#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""level class with the methods to create and display a level"""
import pygame

from pygame.locals import *

from constants import WALL_IMAGE, GUARDIAN_IMAGE, TILE_SIZE

class Level:
    """level structure must be imported from an external file"""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def create_level(self):
        """create level structure from file"""
        with open(self.file, "r") as level_file: # open file from hdd
            grid = [] # initialize main layout array
            for line in level_file:
                grid_line = [] # initialize array for single line
                for box in line:
                    if box != "\n":
                        grid_line.append(box) # add wall element to line array
                grid.append(grid_line) # add line array to main array
        self.structure = grid

    def display_level(self, window):
        """display level in pygame from structure"""
        # load assets
        wall = pygame.image.load(WALL_IMAGE).convert_alpha()
        guardian = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()

        # integrate assets on structure
        nb_line = 0
        for line in self.structure:
            nb_tile = 0
            for tile in line:
                tile_x = nb_tile * TILE_SIZE # set x pixel value to be displayed from tile size
                tile_y = nb_line * TILE_SIZE # set y pixel value to be displayed from tile size
                if tile == "M":
                    window.blit(wall, (tile_x, tile_y))
                elif tile == "A":
                    window.blit(guardian, (tile_x, tile_y))
                nb_tile += 1
            nb_line += 1
