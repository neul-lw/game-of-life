""" 
    First Milestone:
        Save interesting starting positions to files and add the ability to reload them into your Life
        Improve the User Interface
        Change the rules of Life
"""
from pprint import pprint as pp
from random import random
import time 

def random_state(cols, rows, freq):
    arr = []
    for row in range(rows):
        col = []
        for j in range(cols):
            dead_or_alive = random()
            if dead_or_alive >= freq:
                cell_state = 1
            else:
                cell_state = 0
            col.append(cell_state)
        arr.append(col)
    return arr


def next_state(init_state):
    new_state = []
    
    for x in range(0, len(init_state)):
        new_state_row = []
        for y in range(0, len(init_state[0])):
            current_cell_value= init_state[x][y]
            next_elements = adjacent_elements(init_state, x, y)
            if current_cell_value == 0 and next_elements.count(1) == 3:
                new_state_row.append(1)
            elif current_cell_value == 1:
                if 0 <= next_elements.count(1) <= 1:
                    new_state_row.append(0)
                if 2 <= next_elements.count(1) <= 3:
                    new_state_row.append(1)
                if next_elements.count(1) > 3:
                    new_state_row.append(0)
            else:
                new_state_row.append(init_state[x][y])
        new_state.append(new_state_row)
    return new_state 


def is_valid_pos(x, y, col_length, row_length):
    if x < 0 or y < 0 or x > col_length - 1 or y > row_length - 1:
        return 0 
    return 1


def adjacent_elements(init_state, x, y):
    col_length = len(init_state)
    row_length = len(init_state[0])

    adj_arr = [] 

    if is_valid_pos(x-1, y-1, col_length, row_length):
        adj_arr.append(init_state[x-1][y-1])
    if is_valid_pos(x-1, y, col_length, row_length):
        adj_arr.append(init_state[x-1][y])
    if is_valid_pos(x-1, y+1, col_length, row_length):
        adj_arr.append(init_state[x-1][y+1])
    if is_valid_pos(x, y-1, col_length, row_length):
        adj_arr.append(init_state[x][y-1])
    if is_valid_pos(x, y+1, col_length, row_length):
        adj_arr.append(init_state[x][y+1])
    if is_valid_pos(x+1, y-1, col_length, row_length):
        adj_arr.append(init_state[x+1][y-1])
    if is_valid_pos(x+1, y, col_length, row_length):
        adj_arr.append(init_state[x+1][y])
    if is_valid_pos(x+1, y+1, col_length, row_length):
        adj_arr.append(init_state[x+1][y+1])

    return adj_arr


def render(board_state):
    print("----------GAME OF LIFE----------")
    for row in board_state:
        arr = []
        for cell in row: 
            if cell == 1:
                arr.append("#")
            else:
                arr.append(" ")
        pp(arr)
        arr.clear()


if __name__=="__main__":
    a_random_state = random_state(15, 25, 0.5)
    #a_random_state = [[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,], [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]]
    render(a_random_state)
    ns = next_state(a_random_state)
    time.sleep(1)
    while True:
        render(ns)
        time.sleep(0.3)
        ne = next_state(ns)
