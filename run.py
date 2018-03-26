#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""run the game"""
from menu import *
from play import *


def main():
    """main game function with menu and level subloops"""
    # initiate menu
    menu = Menu()
    # menu loop
    while menu.menu_open == 1:
        menu.load_menu()
        menu.close_menu()
        while menu.choice == 1:
            # load play loop
            play = Play(menu.file)
            play.initiate_level()
            play.refresh()
            # play loop
            while play.playing == 1:
                # reset menu loop
                menu.menu_open = 1
                menu.choice = 0
                # player interaction
                play.play_level()
                # refresh window
                play.refresh()
                # victory condition
                play.victory_check()
                # pickup item
                play.on_item()


if __name__ == "__main__":
    main()
