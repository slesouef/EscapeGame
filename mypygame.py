#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""wrapper for pygame"""
import pygame

from pygame.locals import *

from constants import *

class Mypygame:
    """centralize the calls made to pygame in this class"""

    def __init__(self):
        # initiate pygame
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        # set window caption
        pygame.display.set_caption(CAPTION)

    def display_landing(self):
        """method to display landing screen"""
        # setup game menu
        landing = pygame.image.load(MENU_IMAGE)
        self.window.blit(landing, (0, 0))

        #refresh display
        pygame.display.update()

    def display_asset(self, item, position):
        """method to update displayed tiles"""
        self.window.blit(item, (position[0], position[1]))

    def refresh_display(self):
        """method to update the game window"""
        pygame.display.update()
