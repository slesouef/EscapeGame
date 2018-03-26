#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""menu display loop"""
from mypygame import *
from constants import *


class Menu:
    """class containing the main loops necessary to run the game"""

    def __init__(self):
        # initiate loop
        self.menu_open = 1
        self.choice = 0
        self.file = 0
        # load wrapper
        self.mypygame = Mypygame()
        # load landing asset
        self.landing = self.mypygame.load_asset(MENU_IMAGE)

    def load_menu(self):
        """method to display landing screen"""
        # setup game menu
        self.mypygame.display_asset(self.landing, (0, 0))
        self.mypygame.refresh_display()

    def close_menu(self):
        """menu sub loop for the game"""
        # game events in menu
        for events in self.mypygame.get_events():
            if events.type == QUIT or events.type == KEYDOWN \
            and events.key == K_ESCAPE:  # game exit
                self.menu_open = 0
                break
            elif events.type == KEYDOWN and events.key == K_RETURN:
                self.choice = 1
                self.file = GAME_MAP
                break
            else:
                continue
