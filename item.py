#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""item class for the game with random location at each start and item
counter"""
import random
import pygame

from pygame.locals import *

class Item:
    """docsting"""

    def __init__(self, level):
        # refer to current level structure
        self.level = level
        # inventory counter
        self.picked_up_item = 0

    def create_items(self):
        """method for inserting item in level map at random location"""
        # load items assets
        # create randomization loop counter
        # create random values for x,y item coordinates
        # if check random position is not a wall
            # insert item in game
            # modify level structure with item marker
            # increment counter
        # else restart loop from random values creation
        pass

    def pick_up_item(self, position):
        """method for adding items to inventory when player is on tile"""
        # remove item from level map (blit background at item position)
        # increment counter
        pass
