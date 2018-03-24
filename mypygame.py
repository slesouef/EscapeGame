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

    def load_asset(self, asset):
        """method to load graphic assets from file"""
        tile_asset = pygame.image.load(asset).convert_alpha()
        return tile_asset

    def display_asset(self, item, position):
        """method to update displayed tiles"""
        self.window.blit(item, (position[0], position[1]))

    def refresh_display(self):
        """method to update the game window"""
        pygame.display.update()

    def get_events(self):
        """methode to get keyboard events"""
        events = pygame.event.get()
        return events

    def display_text(self, text, position):
        """method to create text image to be displayed"""
        my_font = pygame.font.Font(None, 20)
        text_displayed = my_font.render(text, 1, (0, 0, 0), (255, 255, 255))
        self.window.blit(text_displayed, position)
