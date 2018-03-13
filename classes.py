#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""module containing the classes necessary for the game to play
 - a level class with the methods to create and display a level
 - a character class with the necessary attributes and a move function"""
import pygame
from pygame.locals import *

from constants import *

class Level:
    """level structure must be imported from an external file"""

    def __init__(self, file):
        self.file = file
        self.structure = []

    def create_level(self, file):
        """create level structure from file"""
        with open(self.file, "r") as level_file: # open file from hdd
            grid = [] # initialize main layout array
            for line in level_file:
                grid_line = [] # initialize array for single line
                for box in line:
                    if box != "\n":
                        grid_line.append() # add wall element to line array
                grid.append(grid_line) # add line array to main array
        self.structure = grid

    def display_level(self, structure):
        """display level in pygame from structure"""
        # load assets
        wall = pygame.image.load(wall_image).convert_alpha()
        player = pygame.image.load(player_image).convert_alpha()
        guardian = pygame.image.load(guardian_image).convert_alpha()

        # 

class Character:
    """character attributes and move function"""
    def __init__(self, level):
        # position 
        self.tile_x = 0
        self.tile_y = 0
        self.x = 0
        self.y = 0
        self.level = level

    def move(self, direction):
        """update player location by tile depending on direction input"""
        

