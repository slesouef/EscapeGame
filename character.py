#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""module containing the classes necessary for the game to play
 - a level class with the methods to create and display a level
 - a character class with the necessary attributes and a move function"""
import pygame
from pygame.locals import *

from constants import *

class Character:
    """character attributes and move function"""

    def __init__(self, level):
        # sprite
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        # position
        self.tile_x = 0 # starting tile value
        self.tile_y = 0 # starting line value
        # starting pixel values
        self.pixel_x = 0
        self.pixel_y = 0
        # refer to current level structure
        self.level = level

    def move(self, direction):
        """update player location by tile depending on direction input"""

        # move character right
        if direction == "right":
            # check the move is inside window:
            if self.tile_x + 1 <= (SPRITES_PER_ROW - 1):
                # check tile is not a wall
                if self.level.structure[self.tile_y][self.tile_x + 1] != "M":
                    # move character one tile
                    self.tile_x += 1
                    # update pixel value
                    self.pixel_x = self.tile_x * TILE_SIZE

        # move character left
        if direction == "left":
            if self.tile_x - 1 >= 0:
                if self.level.structure[self.tile_y][self.tile_x - 1] != "M":
                    self.tile_x -= 1
                    self.pixel_x = self.tile_x * TILE_SIZE

        # move character up
        if direction == "up":
            if self.tile_y - 1 >= 0:
                if self.level.structure[self.tile_y - 1][self.tile_x] != "M":
                    self.tile_y -= 1
                    self.pixel_y = self.tile_y * TILE_SIZE

        # move character down
        if direction == "down":
            if self.tile_y + 1 <= (SPRITES_PER_ROW - 1):
                if self.level.structure[self.tile_y + 1][self.tile_x] != "M":
                    self.tile_y += 1
                    self.pixel_y = self.tile_y * TILE_SIZE
