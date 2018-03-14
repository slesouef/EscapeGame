#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""run the game"""
import pygame

from pygame.locals import *

from constants import WINDOW_SIZE, CAPTION, MENU_IMAGE, BACKGROUND_IMAGE
from character import *
from level import *

def main():
    """main game function with menu and level subloops"""

    # initiate pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    # set window caption
    pygame.display.set_caption(CAPTION)

    # refresh display
    pygame.display.update()

   
    # initiate game loops
    keep_open = 1
    
    # MAIN GAME LOOP
    while keep_open == 1:
        # setup game menu
        landing = pygame.image.load(MENU_IMAGE)
        window.blit(landing, (0, 0))

        #refresh display
        pygame.display.update()

        # initiate sub-loops
        menu_open = 1
        playing = 1

        # MENU SUB-LOOP
        while menu_open == 1:
            # cap refresh rate
            pygame.time.Clock().tick(30)

            #game exit
            for events in pygame.event.get():
                if events.type == QUIT or events.type == KEYDOWN and events.key == K_ESCAPE:
                    playing = 0
                    menu_open = 0
                    keep_open = 0
                if events.type == KEYDOWN and events.key == K_RETURN:
                    menu_open = 0
                    file = "map.txt"
                    level_choice = 1

        # load game assets only if the user has selected a level
        if level_choice != 0:
            # initiate background
            background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()

            # create level
            level = Level(file)
            level.create_level()
            level.display_level(window)

            # initiate player
            mcg = Character(level)

        # LEVEL SUB-LOOP
        while playing == 1:
            # cap refresh rate
            pygame.time.Clock().tick(30)

            #game exit
            for events in pygame.event.get():
                if events.type == QUIT:
                    playing = 0
                    keep_open = 0

                elif events.type == KEYDOWN:
                    # return to menu
                    if events.key == K_ESCAPE:
                        playing = 0
                    # move player actions
                    elif events.key == K_UP:
                        mcg.move("up")
                    elif events.key == K_DOWN:
                        mcg.move("down")
                    elif events.key == K_RIGHT:
                        mcg.move("right")
                    elif events.key == K_LEFT:
                        mcg.move("left")

            # pickup item
            # if level.structure[mcg.tile_y][mcg.tile_x] == "I":
                # items.pick_up_item(position)

            # refresh play window values
            window.blit(background, (0, 0))
            level.display_level(window)
            window.blit(mcg.image, (mcg.pixel_x, mcg.pixel_y))

            # refresh display window
            pygame.display.update()

            # victory condition
            if level.structure[mcg.tile_y][mcg.tile_x] == "A": # and items.picked_up_item == 3:
                playing = 0


if __name__ == "__main__":
    main()
