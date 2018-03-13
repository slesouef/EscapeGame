#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""run the game"""
import pygame

from pygame.locals import *

from constants import *
from classes import *

# initiate pygame
pygame.init()
window = pygame.display.set_mode((window_size, window_size))

# set window caption
pygame.display.set_caption(caption)

# refresh display
pygame.display.flip()

def main():
    """main game function with menu and level subloops"""
   
    # initiate game loops
    keep_open = 1
    
    # MAIN GAME LOOP
    while keep_open == 1:
        # setup game menu
        landing = pygame.image.load(menu_image)
        window.blit(landing, (0, 0))

        #refresh display
        pygame.display.flip()

        # initiate sub-loops
        menu_open = 1
        playing = 1

        # MENU SUB-LOOP
        while menu_open == 1:
            # cap refresh rate
            pygame.time.Clock.tick(30)

            #game exit
            for events in pygame.event.get():
                if events.type == QUIT:
                    playing = 0
                    menu_open = 0
                    keep_open = 0
                if events.type == KEYDOWN and events.key == K_RETURN:
                    menu_open = 0
                    file = "map.txt"

        # LEVEL SUB-LOOP
        while playing == 1:
            # cap refresh rate
            pygame.time.Clock.tick(30)

            #game exit
            for events in pygame.event.get():
                if events.type == QUIT:
                    playing = 0
                    menu_open = 0
                    keep_open = 0
                if events.type == KEYDOWN and events.key == K_ESCAPE:
                    playing = 0





if __name__ == "__main__":
    main()
