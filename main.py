#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""Main function of the game """


SCHEMA = [
    [0, 0, 0, 2, 0], \
    [0, 1, 1, 1, 0], \
    [0, 1, 0, 0, 0], \
    [0, 1, 1, 1, 0], \
    [0, 1, 0, 0, 0]
    ]


def create_map(layout):
    """take level file and create layout matrix"""
    grid = [] # initialize main layout array
    for line in layout:
        grid_line = [] # initialize array for single line
        for box in line:
            if box == 0:
                grid_line.append("#") # add wall element to line array
            elif box == 2:
                grid_line.append("M") # add character start point to line array
            else:
                grid_line.append(" ") # add path tile to line array
        grid.append(grid_line) # add line array to main array
    return grid

def display_map(matrix):
    """take layout matrix and display it"""
    for line in matrix:
        row = "".join(line) # for each line in main array, extract element \
                            # into displayable string
        print(row)

def character_position(matrix):
    """calculate current position"""
    # if grid[][] == "M" in grid:
        # print(int(i, j))
    pass

def character_move(position, move):
    """update map representation to move character"""
    # receive input value (wasd?)
    # change current box value to empty space
    # change box moved to value to character
    # refresh display (?)
    pass

def validate_move(position, move):
    """check that the move is valid"""
    # validate move (if box value == 0 => break)
    pass


def main():
    """main function"""
    level = create_map(SCHEMA)
    display_map(level)


if __name__ == "__main__":
    main()
