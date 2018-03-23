#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
"""play loop"""
import time

from level import *
from character import *
from item import *
from mypygame import *
from constants import *

class Play:

    def __init__(self, file):
        # initiate loop
        self.playing = 1
        # load wrapper
        self.mypygame = Mypygame()
        # initiate level elements
        self.level = Level(file)
        self.mcg = Character(self.level)
        self.items = Item(self.level)
        # load background
        self.background = self.mypygame.load_asset(BACKGROUND_IMAGE)
        # load win splash
        self.won = self.mypygame.load_asset(WON_IMAGE)
        # load lose splash
        self.lost = self.mypygame.load_asset(LOST_IMAGE)


    def initiate_level(self):
        """build level display"""
        # create level
        self.level.create_level()
        self.level.create_items()
        self.level.display_level()
        self.mypygame.refresh_display()

    def play_level(self):
        """level sub loop for the game"""
        # game events in level
        for events in self.mypygame.get_events():
            if events.type == QUIT:
                # game exit
                pass
            elif events.type == KEYDOWN:
                if events.key == K_ESCAPE:
                    # return to menu
                    self.playing = 0
                    break
                # move player actions
                elif events.key == K_UP:
                    self.mcg.move_up()
                    break
                elif events.key == K_DOWN:
                    self.mcg.move_down()
                    break
                elif events.key == K_RIGHT:
                    self.mcg.move_right()
                    break
                elif events.key == K_LEFT:
                    self.mcg.move_left()
                    break
                else:
                    break
            else:
                continue

    def refresh(self):
        """refresh window method"""
        # refresh play window values
        self.mypygame.display_asset(self.background, [0, 0])
        self.level.display_level()
        self.items.display_items(self.mypygame.window)
        self.mypygame.display_asset(self.mcg.image, [self.mcg.pixel_x, self.mcg.pixel_y])
        # refresh display window
        self.mypygame.refresh_display()


    def victory_check(self):
        """check if user has fufilled victory condition"""
        if self.level.structure[self.mcg.tile_y][self.mcg.tile_x] == "A":
            if self.items.picked_up_item == 3: # game won
                # display splash screen
                self.mypygame.display_asset(self.won, [0, 0])
                self.mypygame.refresh_display()
                # freeze splash for a few seconds
                time.sleep(3)
                self.playing = 0
            else:
                # lost game
                self.mypygame.display_asset(self.lost, [0, 0])
                self.mypygame.refresh_display()
                time.sleep(3)
                self.playing = 0

    def on_item(self):
        """pick up item when player is on item tile"""
        if self.level.structure[self.mcg.tile_y][self.mcg.tile_x] != "O":
            position = [self.mcg.pixel_x, self.mcg.pixel_y]
            self.items.pick_up_item(position)
