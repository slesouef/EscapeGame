#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""character class with the necessary attributes and a move function"""
from mypygame import *
from constants import *


class Character:
    """character attributes and move function"""

    def __init__(self, level):
        self.mypygame = Mypygame()
        # sprite
        self.image = self.mypygame.load_asset(PLAYER_IMAGE)
        # position
        self.tile_x = 0  # starting tile value
        self.tile_y = 0  # starting line value
        # starting pixel values
        self.pixel_x = 0
        self.pixel_y = 0
        # refer to current level structure
        self.level = level

    def move_right(self):
        """moves player one tile right"""
        # check the move is inside window:
        if self.tile_x + 1 <= (SPRITES_PER_ROW - 1):
            # check tile is not a wall
            if self.level.structure[self.tile_y][self.tile_x + 1] != "M":
                # move character one tile
                self.tile_x += 1
                # update pixel value
                self.pixel_x = self.tile_x * TILE_SIZE

    def move_left(self):
        """moves player one tile left"""
        if self.tile_x - 1 >= 0:
            if self.level.structure[self.tile_y][self.tile_x - 1] != "M":
                self.tile_x -= 1
                self.pixel_x = self.tile_x * TILE_SIZE

    def move_up(self):
        """move player up one tile"""
        if self.tile_y - 1 >= 0:
            if self.level.structure[self.tile_y - 1][self.tile_x] != "M":
                self.tile_y -= 1
                self.pixel_y = self.tile_y * TILE_SIZE

    def move_down(self):
        """move player one tile down"""
        if self.tile_y + 1 <= (SPRITES_PER_ROW - 1):
            if self.level.structure[self.tile_y + 1][self.tile_x] != "M":
                self.tile_y += 1
                self.pixel_y = self.tile_y * TILE_SIZE
