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
        self.mypygame = pygame
        # fix pygame bug #331 (100% CPU utilization)
        self.mypygame.mixer.quit()
        # create game window
        self.window = self.mypygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        # set window caption
        self.mypygame.display.set_caption(CAPTION)

    def load_asset(self, asset):
        """method to load graphic assets from file"""
        tile_asset = self.mypygame.image.load(asset).convert_alpha()
        return tile_asset

    def display_asset(self, item, position):
        """method to update displayed tiles"""
        self.window.blit(item, (position[0], position[1]))

    def refresh_display(self):
        """method to update the game window"""
        self.mypygame.display.update()

    def get_events(self):
        """methode to get keyboard events"""
        events = self.mypygame.event.get()
        return events

    def display_text(self, text, position):
        """method to create text image to be displayed"""
        my_font = self.mypygame.font.Font(None, 20)
        text_displayed = my_font.render(text, 1, (0, 0, 0), (255, 255, 255))
        self.window.blit(text_displayed, position)
