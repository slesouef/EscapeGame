#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""Main function of the game """

def import_level(file):
    """import level from file"""
    # TODO : refactor using with command (with open(file, arg) as var)
    level_file = open(file, "r") # open file from hdd
    level = level_file.read() # read level content
    level_file.close()
    level = level.split("\n") # split file by lines (sep \n)
    level_matrix = []
    for line in level:
        level_line = []
        for box in line:
            level_line.append(int(box))
        level_matrix.append(level_line)
    return level_matrix

def create_map(layout):
    """take level data and create layout matrix"""
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
    position = []
    for i, line in enumerate(matrix):
        for j, box in enumerate(line):
            if box == "M":
                position.append(i)
                position.append(j)
    return position

def available_moves(position, matrix):
    """pre-check what moves are available from current position"""
    # create list of possible next position from current position
    available_move = []
    row = position[0]
    column = position[1]
    if not row - 1 < 0:
        move = [row - 1, column]
        available_move.append(move)
    if not row + 1 > len(matrix):
        move = [row + 1, column]
        available_move.append(move)
    if not column - 1 < 0:
        move = [row, column - 1]
        available_move.append(move)
    if not column + 1 > len(matrix):
        move = [row, column + 1]
        available_move.append(move)
    return available_move

def possible_moves(matrix, character_moves):
    """check which move are valid from list of available moves"""
    # create list of all tiles the player can move to
    moves = []
    for i, line in enumerate(matrix):
        for j, box in enumerate(line):
            if box == " ":
                moves.append([i, j])
    # return list of allowed positions
    valid_moves = []
    for move in moves:
        if move in character_moves:
            valid_moves.append(move)
    return valid_moves

def character_move(position, available_moves):
    """update map representation to move character"""
    # receive input value (wasd?)
    # verifiy that it is in list of allowed positions
    # change current box value to empty space
    # change box moved to value to character
    # refresh display (?)
    pass

def main():
    """main function"""
    level = import_level(input("file location"))
    level_map = create_map(level)
    display_map(level_map)
    position = character_position(level_map)
    print(position)
    moves = available_moves(position, level_map)
    next_moves = possible_moves(level_map, moves)
    print(next_moves)
    # continue_playing = True
    # while continue_playing:
    #     move = input("use wasd to move")
    #     move = str(move.lower())
    #     if move == "w":
    #         # move up
    #     elif move == "s":
    #         # move down
    #     elif move == "a":
    #         # move right
    #     elif move == "d":
    #         # move left
    #     else:
    #         print("insert valid input")
    #         continue
    #     pass


if __name__ == "__main__":
    main()
